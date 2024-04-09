class parent:
    def __init__(self):
        print("This is parent class")
        
class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("This is child class")
        
parent1 = parent()

child1 = child()

