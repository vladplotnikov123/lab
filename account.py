class Account:
    def __init__(self, name: str) -> str:
        """
        creating an object for acocunt
        """
        self.__account_balance=0
        self.name = name
        self.__account_name = name

 
    def deposit(self, amount: int) -> int:
        """
        This function takes in a number and adds it to the 
        account balance and returns true if the amount entered is higher than 0
        if amount less than 1 it doesnt do any changes and returns flase
        """
        if amount >= 1:
            self.__account_balance += amount
            return True
        else:
            return False
            
 
    def withdraw(self, amount: int) -> int:
        """
        This function withdraws an amount given
        if the amount is not bigger than available balance and returns true
        otherwise nothing happens and the function returns false 
        """
        if self.__account_balance >= int(amount):
            self.__account_balance-=amount
            return True
        else:
            return False
 

    def get_balance(self):
        """
        returns balance of the account
        """
        return self.__account_balance


    def get_name(self):
        """
        returns name of the acocunt
        """
        return self.__account_name
 

