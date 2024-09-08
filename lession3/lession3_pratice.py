class BankAccount:

    def __init__(self, balance):
        self.totalBalance = balance

    @property
    def balance(self):
        """Getter method"""
        return self.totalBalance

    @balance.setter
    def balance(self, value):
        """Setter method"""
        if value < 0:
            raise ValueError("Balance must be positive")
        self.totalBalance = value

    @balance.deleter
    def balance(self):
        """Deleter method"""
        print("Deleting balance...")
        self.totalBalance = None


# Test
account = BankAccount(1000)

# Sử dụng getter
print(account.balance)  # Output: 1000

# Sử dụng setter
account.balance = 1500
print(account.balance)  # Output: 1500

# Sử dụng deleter
del account.balance
