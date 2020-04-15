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
        return self
    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance += (self.interest_rate * self.account_balance)
        return self

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bankaccount(.02,0)
    def deposit(self, amount):
        self.account.deposit(amount)
        print(self.name + "'s balance is now " + str(self.account.account_balance))
        return self
    def withdrawal(self, amount):
        self.account.withdrawal(amount)
        print(self.name + "'s balance is now " + str(self.account.account_balance))
        return self
    def display_balance(self):
        print(self.account.account_balance)
        return self
    
brandon = User("Brandon", "brandon@gamil.com")
marcelo = User("Marcelo", "marcelo@gmail.com")
zach = User("Zach", "zach@gmail.com")
brandon.deposit(150).deposit(50).deposit(100).withdrawal(1000)
marcelo.deposit(270).deposit(300).withdrawal(150).withdrawal(100)
zach.deposit(12998).withdrawal(227).withdrawal(300).withdrawal(1000)
brandon.deposit(1000)