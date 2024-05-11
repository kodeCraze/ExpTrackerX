import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.balance = 0

    def add_income(self, amount):
        self.income += amount
        self.balance += amount

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def get_expenses(self):
        return self.expenses

    def get_income(self):
        return self.income

    def set_budget(self, category, budget_amount):
        self.expenses[category] = 0
        self.balance -= budget_amount

    def generate_expense_report(self):
        total_expenses = sum(self.expenses.values())
        return total_expenses

    def get_category_expenses(self, category):
        return self.expenses.get(category, 0)

    def get_total_budget(self):
        return self.balance

    def get_remaining_balance(self):
        return self.balance - sum(self.expenses.values())

    def visualize_spending(self):
        sns.set()
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(self.expenses.keys()), y=list(self.expenses.values()))
        plt.title('Spending Breakdown')
        plt.xlabel('Category')
        plt.ylabel('Amount')
        plt.show()

    def optimize_budget(self):
        optimized_expenses = {}
        for category, amount in self.expenses.items():
            if amount > self.balance / len(self.expenses):
                optimized_expenses[category] = self.balance / len(self.expenses)
            else:
                optimized_expenses[category] = amount
        self.expenses = optimized_expenses

    def get_optimized_expenses(self):
        return self.expenses

# Example usage:
budget = BudgetTracker()

while True:
    print("1. Add income")
    print("2. Add expense")
    print("3. Set budget")
    print("4. Generate expense report")
    print("5. Visualize spending")
    print("6. Optimize budget")
    print("7. Exit")

    choice = int(input("Enter your choice in No : "))

    if choice == 1:
        amount = float(input("Enter income amount: "))
        budget.add_income(amount)
    elif choice == 2:
        category = input("Enter category: ")
        amount = float(input("Enter expense amount: "))
        budget.add_expense(category, amount)
    elif choice == 3:
        category = input("Enter category: ")
        amount = float(input("Enter budget amount: "))
        budget.set_budget(category, amount)
    elif choice == 4:
        print(f"Total Expenses: {budget.generate_expense_report()}")
    elif choice == 5:
        budget.visualize_spending()
    elif choice == 6:
        budget.optimize_budget()
        print(f"Optimized Expenses: {budget.get_optimized_expenses()}")
    elif choice == 7:
        break
    else:
        print("Invalid choice. Please try again.")

print(f"Final Balance: {budget.get_balance()}")
print(f"Final Expenses: {budget.get_expenses()}")
print(f"Final Income: {budget.get_income()}")
