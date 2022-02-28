import random

#Pet class..........................

class Pet:
    
    def __init__(self,name=None):
        self.name=name
        self.age=random.randint(5, 10)
        self.favouriteFood=None
        self.namelist=[]
        if(self.name!=None):
            self.namelist.append(name)
        self.speakfreq=0

    def getName(self):
        return self.name    

    def getNames(self):
        return self.namelist

    def getAge(self):
        return self.age
    
    def getFavouriteFood(self):
        return self.favouriteFood

    def setName(self,newName):
        
        self.name=newName
        if(len(self.namelist)==0 or self.namelist[-1]!=newName):
            self.namelist.append(self.name)

    def setAge(self,newAge):
        self.age=newAge
    
    def setFavouriteFood(self,newFavouriteFood):
        self.favouriteFood=newFavouriteFood

    def speak(self,sound="meow"):
        if(self.speakfreq==4):
            self.age+=1
            self.speakfreq=0
        self.sound=sound
        print(self.sound)
        self.speakfreq+=1
        return self.sound
    
    def getAverageNameLength(self):
        lengths = [len(i) for i in self.namelist]
        return 0 if len(lengths) == 0 else (round((sum(lengths)) / len(lengths)))
        

#Data class...................

class Data:
    def __init__(self,database):
        print("Connecting to Database")
        self.table={}
        self.count=1

    def beginTran(self):
        print("Beginning transaction")
     
    def commit(self):
        print("committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def insert(self,table,object):
        print("Inserting ",object.getName()," into "+table)
        list1=[object.getName(),object.getAge(),object.getFavouriteFood(),object.getNames()]
        self.table[self.count]=list1
        self.count+=1
    
    def display(self):
        print("\nSuccessfully committed transactions: ")

        for key, value in self.table.items():
            print(key, ' : ', value)
        
        print("End of LOG Stats")

# Test code......................

import unittest

class TestAge(unittest.TestCase):

    #Test that age is a random number between 5 to 10 and value is returned
    def test_catAge(self):
        cat1=Pet()
        print(cat1.getAge())
        x=cat1.getAge()
        self.assertTrue(x>=5&x<=10)

    #Test that age is a random number between 5 to 10 and value is returned
    def test_catAge2(self):
        cat1=Pet()
        print(cat1.getAge())
        x=cat1.getAge()
        self.assertTrue(x>=5&x<=10)

class TestSpeak(unittest.TestCase):


    def test_Speak1(self):
        cat1=Pet()

        #Test that default value of speak is meow
        self.assertTrue(cat1.speak()=="meow")

        
    def test_Speak2(self):
        cat1=Pet()

        #Test that value is changed to desired value
        self.assertTrue(cat1.speak("purr")=="purr")

    def test_Speak3(self):
        cat1=Pet()
        print("\nBefore speaking 5 times the age of the pet is ",cat1.getAge())
        y=cat1.getAge()
        for x in range(5):
            cat1.speak()
        print("After speaking 5 times the age of the pet is ",cat1.getAge())

        #Test that age increases by 1 when the pet speaks 5 times
        self.assertTrue(y+1==cat1.getAge())


if __name__ == '__main__':
    unittest.main()