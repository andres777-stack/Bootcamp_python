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

bankAccount1 = Bankaccount(saldo = 500, tasa_interes = 0.05)
bankAccount2 = Bankaccount(saldo = 600, tasa_interes = 0.02)

bankAccount1.deposit(100).deposit(100).deposit(100).withdraw(100).yield_interest().display_account_info()
bankAccount2.deposit(100).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(40).yield_interest().display_account_info()

