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

# petShop code......................

data=Data("Database")

def saveTest():
    cat1=Pet("Tom")
    dog1=Pet("Coco")
    dog1.speak("woof")
    
    data.insert("Pet Table",cat1)
    data.insert("Pet Table",dog1)

def savePetShop():
    cat4=Pet()
    data.insert("Pet Table",cat4)
    dog4=Pet()
    data.insert("Pet Table",dog4)
    cat2=Pet()
    data.insert("Pet Table",cat2)
    dog2=Pet()
    data.insert("Pet Table",dog2)
    cat3=Pet()
    data.insert("Pet Table",cat3)
    dog3=Pet()
    data.insert("Pet Table",dog2)

def logStats():
    print("Transaction steps are: \n")
    data.beginTran()
    data.commit()
    data.display()

    
    
saveTest()
savePetShop()
logStats()