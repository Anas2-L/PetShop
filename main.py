
import pet
import data
cat1=pet.Pet("Tom")
dog1=pet.Pet()
cat1.setName("Garfield")
print("name is currently",cat1.getName())
print("Name has been changed to ", cat1.getName())
data1=data.Data("database")
print("Age of the cat is: ",cat1.getAge())

cat1.speak()
print(cat1.getNames())
dog1.speak("woof")
print("Age of the dog is: ",dog1.getAge())
print("Average length is: ",cat1.getAverageNameLength())
data1.insert("Pet table",cat1)
