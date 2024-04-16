# Method overriding
class Animal:
    def speaks(self):
        print("Generic Noise")
    
class Dog(Animal):
    def speaks(self):
        print("Barks")
        
class Cat(Animal):
    def speaks(self):
        print("Meow Meow")
        
class Cow(Animal):
    def speaks(self):
        print("Moo Moo")
        
animal = Animal()
dog = Dog()
cat = Cat()
cow = Cow()

animal.speaks()
dog.speaks()
cat.speaks()
cow.speaks()