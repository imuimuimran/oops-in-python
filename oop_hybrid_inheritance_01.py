class PlstinumSchool:
    stu_name = ""
    def plt_school(self):
        print("Platinum School")
       
    
class RotarySchool:
    stu_name = ""
    def rot_school(self):
        print(self.stu_name)
        
class MohoshinCollege:
    stu_name = ""
    def moh_college(self):
        print(self.stu_name)
        
class DayNightCollege:
    stu_name = ""
    def day_night_college(self):
        print("Day Night college")
        
class Student1(PlstinumSchool, MohoshinCollege):
    def stu1(self):
        print(self.stu_name, "was both Platinum and Mohoshin student")
class Student2(PlstinumSchool, DayNightCollege):
    def stu2(self):
        print(self.stu_name, "was both Platinum and Day Night student")

class Student3(RotarySchool, MohoshinCollege):
    def stu3(self):
        print(self.stu_name, "was both Rotary and Mohoshin student")
        
class Student4(RotarySchool, DayNightCollege):
    def stu4(self):
        print(self.stu_name, "was both Rotary and Day Night student")

s1 = Student1()
s2 = Student2()
s3 = Student3()
s4 = Student4()
s1.stu_name = "Imran Hossain"
s2.stu_name = "Ikram Hossain"
s3.stu_name = "Akram Hossain"
s4.stu_name = "Tahseen Akram"
s1.stu1()
s2.stu2()
s3.stu3()
s4.stu4()
print(f"{s2.stu_name}")
s2.plt_school()
s2.day_night_college()