class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("Usuario: " + self.name, "," + " Saldo: " + str(self.account_balance))
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

monty = User(username="Monty Python", email_address="monty@gmail.com")
montys_wife = User(username = "Alice Python", email_address = "apython@gmail.com")
montys_son = User(username = "Monty Junior", email_address = "junior@gmail.com")

monty.make_deposit(600).make_deposit(600).make_deposit(600).make_withdraw(550).display_user_balance()

montys_wife.make_deposit(600).make_deposit(600).make_withdraw(400).make_withdraw(400).display_user_balance()

montys_son.make_deposit(600).make_withdraw(100).make_withdraw(100).make_withdraw(100).display_user_balance()