class bankaccount:
    def __init__(self, int_rate, balance):
        self.interest_rate = int_rate
        self.account_balance = balance
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return self
    def withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print(self.account_balance)
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.interest_rate * self.account_balance)
        return self

account_1 = bankaccount(.12,1000)
account_2 = bankaccount(.11,1000)
account_1.deposit(100).deposit(100).deposit(100).withdrawal(300).yield_interest().display_account_info()
account_2.deposit(300).deposit(100).withdrawal(100).withdrawal(100).withdrawal(100).withdrawal(100).yield_interest().display_account_info()