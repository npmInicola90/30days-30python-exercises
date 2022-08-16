class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fee = 0
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance += amount
    def withdraw(self, amount):
        
         self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            self.fee += 5
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fee

my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()
