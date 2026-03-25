class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance 
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

    def get_owner(self):
        return self.owner
    

    def __str__(self):
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.__balance == other.__balance
        return NotImplemented
    
    def __hash__(self):
        return hash((self.owner, self.__balance))
    
    

acc = BankAccount("Sonit", 1000)
acc.deposit(500)
print(acc.get_balance())   # works: 1500
print(acc.__balance)       # AttributeError — try it
print(acc._BankAccount__balance)  # this works — name mangling, not true privacy
acc.withdraw(200)
print(acc.get_balance())   # works: 1300
print(acc)  # uses __str__
print(repr(acc))  # uses __repr__
acc2 = BankAccount("Sonit", 1300)
print(acc == acc2)  # True, uses __eq__
acc3 = BankAccount("Sonit", 1500)
print(acc == acc3)  # False, different balance
acc4 = BankAccount("Alice", 1300)
print(acc == acc4)  # False, different owner
accounts_set = {acc, acc2, acc3, acc4}
print(accounts_set)  # uses __hash__ to store unique accounts in a set
print(acc in accounts_set)  # True, acc is in the set
print(acc2 in accounts_set)  # True, acc2 is in the set
print(acc3 in accounts_set)  # True, acc3 is in the set
print(acc4 in accounts_set)  # True, acc4 is in the set

