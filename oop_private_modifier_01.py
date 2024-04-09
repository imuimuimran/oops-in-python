# Private Modifier
class account_information:
    def __init__(self, account_name, opening_date, deposit):
        self.__account_name = account_name
        self.opening_date = opening_date
        self.deposit = deposit
        
    def account_info(self, account_name, opening_date, deposit):
        self.__account_name = account_name
        self.opening_date = opening_date
        self.deposit = deposit
        
    __account_name = "Rahim" # Inside the class private modifier can work
    print(__account_name)

# # Outside of the class private modifier can not work
# account1 = account_information("Mr. Karim", 2010, 175300)
# account2 = account_information("Parthib Kundu", 1999, 350600)

# print(account1.__account_name, account1.opening_date, account1.deposit)
# print(account2.__account_name, account2.opening_date, account2.deposit)