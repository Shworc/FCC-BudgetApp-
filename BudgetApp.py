class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})
        #print(self.ledger)

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        else:
            self.ledger.append({'amount': -amount, 'description': description})
            return True

    def get_balance(self):
        balance = 0
        for b in self.ledger:
            print(b["amount"])
            balance += b["amount"]
        return balance
        #return sum(amount for amount in self.ledger)

    def transfer(self, amount, description=""):
        if amount >= self.check_funds(amount):
            amount = self.withdraw(amount, description)
            print(f"Transfer to {description}")
            amount.deposit(amount, 'transfer over')
        return True

    def check_funds(self, amount):
        return self.get_balance() >= amount         

def create_spend_chart(self,category=""):
    self.category = category

test = Category('Food')
test.deposit(1000, 'pizza')
test.withdraw(10,'pizza')
#test.transfer(test.get_balance(), test)
test.transfer(200, '')
print(test.get_balance())

create_spend_chart(test)