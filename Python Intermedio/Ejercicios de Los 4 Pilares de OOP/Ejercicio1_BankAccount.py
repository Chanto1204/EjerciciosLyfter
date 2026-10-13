class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        

    def deposit(self):
        new_deposit = float(input("Ingrese un monto a depositar: "))
        self.balance = new_deposit + self.balance


    def withdraw(self):
        new_withdraw = float(input("Ingrese un monto a retirar: "))
        self.balance = self.balance - new_withdraw 


class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance


    def withdraw(self):
        new_withdraw = float(input("Ingrese un monto a retirar: "))
        if self.balance - new_withdraw >= self.min_balance:
            self.balance = self.balance - new_withdraw
        else:
            raise ValueError("El retiro supera el saldo mínimo permitido")



savings = SavingsAccount(1000, 200)

print(f"Balance inicial: {savings.balance}")

savings.withdraw()

print(f"Balance final: {savings.balance}")

