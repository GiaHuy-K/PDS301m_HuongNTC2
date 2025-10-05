# Exercise 1: Grocery Shopping Budget Tracker
# You’re at the supermarket and want to ensure you don’t overspend. Your program will:
# 1. Ask for the user’s total budget.
# 2. Let them enter item prices one by one.
# 3. Stop when the budget is exhausted and give a summary.
# Key Python Concepts Covered: Input/Output (input(), print()), Loops (while),
# Conditionals (if-else), Basic Arithmetic (updating totals), Data Types (float, string)
budget_input = float(input("What's your total budget for groceries? $"))
total_spent = 0.0
while True:
    item_price = float(input("Enter item price (or '0' to finish) : $"))
    if item_price == 0:
        break
    total_spent += item_price
    if total_spent > budget_input:
        print(f"Warning: You're ${total_spent - budget_input:.2f} over your budget!")
        print(f"\nTotal spent: ${total_spent:.2f}")
        print("You exceeded your budget!")
        break
print(f"Total spent so far: ${total_spent:.2f}. Remaining budget: ${budget_input - total_spent:.2f}")
        