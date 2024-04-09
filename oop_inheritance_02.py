# Inheritance
class parent:
    def __init__(self, par_name):
        self.par_name = par_name
        print("This is parent class")
        
class child(parent):
    def __init__(self, par_name, chi_name):
        super().__init__(par_name)
        self. chi_name = chi_name
        print("This is child class")
        
    def print_chi_info(self):
        print("Child-Name: ", self.chi_name)
        
        
        
print("Parent class block: ")
parent1 = parent("Dad")
print(parent1.par_name)

print("\nChild class block: ")
child1 = child("Dud", "Son")
print(child1.par_name, child1.chi_name)
child1.print_chi_info()
