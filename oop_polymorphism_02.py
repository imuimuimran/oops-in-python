# Polymorphism with class methods: 

class Bangladesh():
    def info(self):
        print("Information of Bangladesh")
    def language(self):
        print("Bangla")
    def capital(self):
        print("Dhaka")
    def money(self):
        print("Taka")
        
class India():
    def info(self):
        print("\nInformation of India")
    def language(self):
        print("Hindi")
    def capital(self):
        print("Delhi")
    def money(self):
        print("Rupi")
        
bd = Bangladesh()
ind = India()

for country in (bd, ind):
    country.info()
    country.language()
    country.capital()
    country.money()
        