from pet import Pet
from data import Data

data=Data("Database")

def saveTest():
    cat1=Pet("Tom")
    dog1=Pet("Coco")
    dog1.speak("woof")
    
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

