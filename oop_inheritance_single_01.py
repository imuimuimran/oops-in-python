class Parent:
    i = 50
    def func1(self):
        i = 40
        print("parent i value", i)
        print(f"This is pareant class whose age is {i}")
        
class Child(Parent):
    i = 20
    def func2(self):
        i = 15
        print("child i value", i)
        print(f"This is child class whose age is {i}")
        
par1 = Parent()
chi1 = Child()

par1.func1()
chi1.func2()
chi1.func1()

print("Value of parent age:", par1.i)
print("value of child age:", chi1.i)


