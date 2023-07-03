class Account:
    def __init__(self, account_number, holder_name, balance):
        self.account = account_number
        self.name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            # print("WITHDRAW")
            self.balance -= amount
        else:
            print("HAUNA HELA !!!")

    def display_balance(self):
        print(f"Account number: {self.account}")
        print(f"Holder name : {self.name}")
        print(f"Balance : {self.balance}")


my_acc = Account("56478764568913", "Alex", 40000000)
my_acc.display_balance()
my_acc.withdraw(5000)
