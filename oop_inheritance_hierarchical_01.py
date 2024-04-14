class Parent:
    def func1(self):
        print("This is func1 parent class")
        
class Child1(Parent):
    def func2(self):
        print("This is func2 child1 class")

class Child2(Parent):
    def func3(self):
        print("This is func3 child 2 class")
        
parent1 = Parent()
child1 = Child1()
child2 = Child2()

parent1.func1()
child1.func1()
child1.func2()
child2.func1()
child2.func3()