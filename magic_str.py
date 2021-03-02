class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def __str__(self):
        return f"{self.amount:5} {self.currency:3}"

#####################################################
salary = Money(1000, "EUR")
expense = Money(300, "EUR")

print(salary)
print(expense)