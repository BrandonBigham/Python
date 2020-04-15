class User:
    def __init__(self, name, email, starting_balance):
        self.name = name
        self.email = email
        self.account_balance = starting_balance
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(self.name + "'s balance is now " + str(self.account_balance))
        #update
        return self
    def withdrawal(self, amount):
        self.account_balance -= amount
        print(self.name + "'s balance is now " + str(self.account_balance))
        return self
    def display_balance(self):
        print(self.account_balance)
        return self
    def transfer(self, my_money, second_user, second_money):
        if my_money > 0:
            self.account_balance += my_money
            second_user.account_balance -= second_money
        else:
            self.account_balance += my_money
            second_user.account_balance += second_money
        print(self.name + "'s balance is now " + str(self.account_balance) + ", and " + second_user.name + "'s account balance is now " + str(second_user.account_balance))
        return self
    
brandon = User("Brandon", "brandon@gmail.com", 1000)
marcelo = User("Marcelo", "marcelo@gmail.com", 6273)
zach = User("Zach", "zach@gmail.com", 10000)
# brandon.deposit(150).deposit(50).deposit(100).withdrawal(1000)
# marcelo.deposit(27).deposit(200).withdrawal(1500).withdrawal(1000)
# zach.deposit(12998).withdrawal(227).withdrawal(300).withdrawal(953245)
brandon.transfer(-500, zach, 500)