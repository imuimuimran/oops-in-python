class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername
        
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        
        Grandfather.__init__(self, grandfathername)
        
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Father.__init__(self, fathername, grandfathername)
    
    def print_name(self):
        print("Grand Father Name:", self.grandfathername)
        print("Father Name:", self.fathername)
        print("Son Name:", self.sonname)
        
son1 = Son("Imran Hossain", "Abul Kashem", "Intaj Matubbar")

son1.print_name()

print(son1.grandfathername)