# Encapsulation 
class BankAccount:
    def __init__(self):
        self.__balance = 0
        
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            
    def get_balance(self):
        return self.__balance 

b = BankAccount()
b.deposit(1000)
print("Your total deposit is:", b.get_balance())
b.withdraw(500)
print("Your total balance is:", b.get_balance())