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

# Main code......................

cat1=Pet("Tom")
dog1=Pet()
cat1.setName("Garfield")
print("name is currently",cat1.getName())
print("Name has been changed to ", cat1.getName())
data1=Data("database")
print("Age of the cat is: ",cat1.getAge())

cat1.speak()
print(cat1.getNames())
dog1.speak("woof")
print("Age of the dog is: ",dog1.getAge())
print("Average length is: ",cat1.getAverageNameLength())
data1.insert("Pet table",cat1)
