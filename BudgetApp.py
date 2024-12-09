class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output

    def getTotals(categories): ###Helper method
        total = 0
        breakdown = []
        for category in categories:
            total += category.get_withdrawls()
            breakdown.append(category.get_withdrawals())
        rounded = list(map(lambda x: truncate(x/total), breakdown))
        return rounded

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

    def transfer(self, amount, other_category):
        if (self.check_funds(amount)):
            self.withdraw(amount, f"Transfer to {self.category}")
            other_category.deposit(amount, "Transfer from " + self.category)
            return True
        return False

    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False

def create_spend_chart(categories):
    res = "Percentage spent by category\n"
    i = 100
    totals = getTotals(categories)
    while i >= 0:
        cat_spaces = " "
        for total in totals:
            if total * 100 >= i:
                cat_spaces += "o "
            else:
                cat_spaces += "  "
        res += str(i).rjust(3) + "|" + cat_spaces + ("\n")
        i -= 10
    dashes = "-" + "---" * len(categories)
    names = []
    x_axis = ""
    for category in categories:
        names.append(category.name)

    maxi = max(names, key=len)

    for x in range(len(maxi)):
        nameStr = '     '
        for name in names:
            if x >= len(name):
                nameStr += "   "
            else:
                nameStr += name[x] + " "
        if(x != len(maxi)-1 ):
            nameStr += '\n'

        x_axis += nameStr

    res += dashes.rjust(len(dashes)+4) + "\n" + x_axis

test = Category('Food')
print("creating object test")
print(test.deposit(1000, 'pizza'), "deposit to object test")
print(repr(test.withdraw(10,'pizza')),"withdrawal from object test, pizza")
clothing = Category('Clothing')
print("creating object clothing")
#test.transfer(test.get_balance(), test)
print((test.transfer(200, clothing))) ###f"transfering from object test to {clothing}"))
print(test.get_balance(), "test balance")
print(test)
print(clothing)
#create_spend_chart(test)