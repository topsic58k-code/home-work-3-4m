class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number  # Номер рахунку
        self.balance = balance                # Баланс рахунку

    def deposit(self, amount):
        if amount <= 0:
            print("Сума поповнення має бути додатною.")
            return

        self.balance += amount
        print(f"Рахунок поповнено на {amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття має бути додатною.")
        elif amount > self.balance:
            print("Недостатньо коштів на рахунку.")
        else:
            self.balance -= amount
            print(f"Знято {amount}. Баланс: {self.balance}")


# Приклад використання
account = BankAccount("123456789", 1000)

account.deposit(500)    # Поповнення на 500
account.withdraw(200)   # Зняття 200
account.withdraw(2000)  # Недостатньо коштів

print("Номер рахунку:", account.account_number)
print("Поточний баланс:", account.balance)