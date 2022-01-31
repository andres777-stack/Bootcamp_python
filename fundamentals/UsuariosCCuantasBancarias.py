class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = Bankaccount(saldo = 0, tasa_interes = 0.05)
    def make_deposit(self, amount):
        self.account += amount
        return self
    def make_withdraw(self, amount):
        self.account -= amount
        return self
    def display_user_balance(self):
        print("Usuario: " + self.name, "," + " Saldo: " + str(self.account_balance))
    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        return self

class Bankaccount:
    def __init__(self, saldo, tasa_interes):
        self.saldo = saldo
        self.tasa_interes = tasa_interes
    def deposit(self, amount):
        self.saldo += amount
        return self
    def withdraw(self, amount):
        if self.saldo >= amount:
            self.saldo -= amount
        else:
            print("Fondos insuficientes:cobrar una tarifa de $5 y deduzca $5")
        return self
    def display_account_info(self):
        print("Saldo: ", self.saldo)
    def yield_interest(self):
        if self.saldo > 0:
            x = self.saldo * self.tasa_interes
            self.saldo += x
        return self

monty = User(username="Monty Python", email_address="monty@gmail.com")
monty.account.deposit(100).display_account_info()
