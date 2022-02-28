import random
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
        

  