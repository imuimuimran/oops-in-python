# Inheritance
class parent:
    def __init__(self):
        print("This is parent class")
        
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("This is child class")
        
print("Parent class block: ")
parent1 = parent()

print("\nChild class block: ")
child1 = child()

