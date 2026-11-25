class Account:
    def __init__(self,account_number,owner,balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    def withdraw(self,amount):
         return self.balance - amount
class SavingsAccount(Account):
     def __init__(self, account_number, owner, balance):
          super().__init__(account_number, owner, balance)

     def withdraw(self, amount):
         if((self.balance - amount) > 1000):
           return super().withdraw(amount)
     def add_money(self,rate):
        return self.balance * rate
class CurrentAccount(Account):
    def __init__(self, account_number, owner, balance):
        super().__init__(account_number, owner, balance)
    def withdraw(self, amount):
        return super().withdraw(amount)
    