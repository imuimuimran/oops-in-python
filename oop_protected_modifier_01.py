# Protected Modifier 
class account_information:
    def __init__(self, account_name, opening_date, deposit):
        self._account_name = account_name
        self.opening_date = opening_date
        self.deposit = deposit
        
    def account_info(self, account_name, opening_date, deposit):
        self._account_name = account_name
        self.opening_date = opening_date
        self.deposit = deposit
        
# Outside of the class protected modifier also can work but it should not be done. 
account1 = account_information("Mr. Karim", 2010, 175300)
account2 = account_information("Parthib Kundu", 1999, 350600)

print(account1._account_name, account1.opening_date, account1.deposit)
print(account2._account_name, account2.opening_date, account2.deposit)

# Implementing inheritance with protected attributes
class ac_info(account_information):
    def __init(self, account_name, opening_date, deposit):
        account_information.__init__(self, account_name, opening_date, deposit)
    def print_protected(self):
        print(self._account_name)
        self.account_info("Mr Y", 2024, 500)  # Calling the base class method
        
account3 = ac_info("Mr X" , 2007, 1500)
account3.print_protected() # This will print "Mr X" and then update the account info
print(account3._account_name, account3.opening_date, account3.deposit)  # Printing updated info