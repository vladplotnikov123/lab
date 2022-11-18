class Account:
    def __init__(self, name: str) -> str:
        self.__account_balance=0
        self.name = name
        self.__account_name = name

 
    def deposit(self, amount: int) -> int:
        if amount >= 1:
            self.__account_balance += amount
            return True
        else:
            return False
            
 
    def withdraw(self, amount: int) -> int:
        if self.__account_balance >= int(amount):
            self.__account_balance-=amount
            return True
        else:
            return False
 

    def get_balance(self):
        return self.__account_balance


    def get_name(self):
        return self.__account_name
 

