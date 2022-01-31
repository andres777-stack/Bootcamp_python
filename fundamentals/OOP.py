class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdraw(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("Usuario: " + self.name, "," + " Saldo: " + str(self.account_balance))
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

monty = User(username="Monty Python", email_address="monty@gmail.com")
montys_wife = User(username = "Alice Python", email_address = "apython@gmail.com")
montys_son = User(username = "Monty Junior", email_address = "junior@gmail.com")

monty.make_deposit(600)
monty.make_deposit(600)
monty.make_deposit(600)
monty.make_withdraw(550)
monty.display_user_balance()

montys_wife.make_deposit(600)
montys_wife.make_deposit(600)
montys_wife.make_withdraw(400)
montys_wife.make_withdraw(400)
montys_wife.display_user_balance()

montys_son.make_deposit(600)
montys_son.make_withdraw(100)
montys_son.make_withdraw(100)
montys_son.make_withdraw(100)
montys_son.display_user_balance()
