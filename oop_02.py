class Student:
    def set_name(self, name, roll): #This is method or function
        self.name = name
        self.roll = roll
        
    def get_name(self, name1, roll1): #This is method or function
        self.name1 = name1
        self.roll1 = roll1
        return self.name1, self.roll1
    
student1 = Student() # Here student1 is an object
student1.set_name("Mohd. Imran Hossain", 12)

# We can print now the student name
print(student1.name)
print(student1.roll)

# we can print student name another way
print(student1.get_name("Hi", 2))