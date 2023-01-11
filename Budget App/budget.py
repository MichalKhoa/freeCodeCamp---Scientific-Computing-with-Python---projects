class Category:
    budget_category = None
    balance = 0.0
    ledger = []
    spent = 0.0

    def __init__(self, category):
        self.budget_category = category
        self.ledger = []
        self.balance = 0.0
        self.spent = 0.0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += float(amount)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is True:
            self.ledger.append({"amount": -amount, "description": description})
            self.balance -= float(amount)
            self.spent -= float(amount)
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, target_category):
        if self.check_funds(amount) is True:
            self.balance -= amount
            target_category.balance += float(amount)
            self.ledger.append({"amount": -amount, "description": "Transfer to %s" % target_category.budget_category})
            target_category.ledger.append({"amount": amount, "description": "Transfer from %s" % self.budget_category})
            return True
        else:
            return False

    def check_funds(self, amount):
        if float(amount) > self.balance:
            return False
        else:
            return True

    def __str__(self):
        display = ('*'*((30-len(self.budget_category))//2) + self.budget_category +
                   '*'*((30-len(self.budget_category))//2) + "\n")
        for i in range(len(self.ledger)):
            extracted_amount = self.ledger[i].get("amount")
            extracted_descr = self.ledger[i].get("description")
            display += extracted_descr.ljust(23)[:23] + ("{:.2f}".format(extracted_amount).rjust(7)[:7]) + "\n"
        display += "Total: {0}".format(self.balance)

        return str(display)


def create_spend_chart(categories):
    spent_sum = 0.0
    for category in categories:
        spent_sum += category.spent
    spend_chart = "Percentage spent by category"
    percentage = 100
    while percentage >= 0:
        spend_chart += "\n"
        spend_chart += str(percentage).rjust(3) + "|"
        for category in categories:
            spent_percentage = category.spent*100/spent_sum
            if spent_percentage >= percentage:
                spend_chart += " o "
            else:
                spend_chart += "   "
        percentage -= 10
        spend_chart += " "
    spend_chart += "\n" + " "*4 + "-"*10
    categories_in_str = []
    for category in categories:
        categories_in_str.append(category.budget_category)
    longest_category = max(categories_in_str, key=len)
    for i in range(len(longest_category)):
        spend_chart += "\n" + " "*4
        for str_category in categories_in_str:
            if i in range(len(str_category)):
                spend_chart += str_category[i].center(3)
            else:
                spend_chart += " "*3
        spend_chart += " "
    return spend_chart
