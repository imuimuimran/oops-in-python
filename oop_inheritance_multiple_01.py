class Father:
    father_name = "Mohd. Abul Kashem"
    def father_info(self):
        print(self.father_name)
        
class Mother:
    mother_name = ""
    def mother_info(self):
        print(self.mother_name)
        
class Son(Father, Mother):
    son_name = ""
    def son_info(self):
        print("Son Name: ", self.son_name)
    def parents_info(self):
        print("Father Name:", self.father_name)
        print("Motther Name:", self.mother_name)
        
fat1 = Father()
#fat1.father_name = "Mohd. Abul Kashem"
fat1.father_info()
son1 = Son()
son1.son_name = "Imran Hossain"
#son1.father_name = "Abul Kashem"
son1.mother_name = "Aleya Begum"
son1.son_info()
son1.parents_info()
