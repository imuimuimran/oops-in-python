class Student:
    def set_name(self, name): #This is method or function
        self.name = name
        
    def get_name(self): #This is method or function
        return self.name
    
student1 = Student() # Here student1 is an object
student1.set_name("Mohd. Imran Hossain")

# We can print now the student name
print(student1.name)

# we can print student name another way
print(student1.get_name())