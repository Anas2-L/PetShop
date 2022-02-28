import unittest
import pet

class TestAge(unittest.TestCase):

    #Test that age is a random number between 5 to 10 and value is returned
    def test_catAge(self):
        cat1=pet.Pet()
        print(cat1.getAge())
        x=cat1.getAge()
        self.assertTrue(x>=5&x<=10)

    #Test that age is a random number between 5 to 10 and value is returned
    def test_catAge2(self):
        cat1=pet.Pet()
        print(cat1.getAge())
        x=cat1.getAge()
        self.assertTrue(x>=5&x<=10)

class TestSpeak(unittest.TestCase):


    def test_Speak1(self):
        cat1=pet.Pet()
        print("\nBefore speaking 5 times the age of the pet is ",cat1.getAge())

        #Test that default value of speak is meow
        self.assertTrue(cat1.speak()=="meow")

        
    def test_Speak2(self):
        cat1=pet.Pet()
        print("\nBefore speaking 5 times the age of the pet is ",cat1.getAge())

        #Test that value is changed to desired value
        self.assertTrue(cat1.speak("purr")=="purr")

    def test_Speak3(self):
        cat1=pet.Pet()
        print("\nBefore speaking 5 times the age of the pet is ",cat1.getAge())
        y=cat1.getAge()
        for x in range(5):
            cat1.speak()
        print("After speaking 5 times the age of the pet is ",cat1.getAge())

        #Test that age increases by 1 when the pet speaks 5 times
        self.assertTrue(y+1==cat1.getAge())


if __name__ == '__main__':
    unittest.main()