class MpesaTransaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def process(self):
        return NotImplementedError()


class DepositTransaction(MpesaTransaction):
    def process(self):
        print(f"Deposit transaction ith ID {self.transaction_id} processed.amount {self.amount}")


class WithdrawTransaction(MpesaTransaction):
    def process(self):
        print(f"Withdraw transaction with ID {self.transaction_id} processed.amount {self.amount}")


class PaymentTransaction(MpesaTransaction):
    def __init__(self, transaction_id, amount, recipient):
        super().__init__(transaction_id, amount)
        self.recipient = recipient

    def process(self):
        print(
            f"Payment transaction with ID {self.transaction_id} processed.Amount {self.amount} ."
            f"Recipient {self.recipient}")


deposit = DepositTransaction("Romeo", 5000)
deposit.process()
withdraw = WithdrawTransaction("Romeo", 4000)
withdraw.process()
payment = PaymentTransaction("Romeo", 5000, "Emobilis")
payment.process()
