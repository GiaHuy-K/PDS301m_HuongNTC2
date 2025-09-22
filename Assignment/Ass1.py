# Exercise 1: Grocery Shopping Budget Tracker
# You’re at the supermarket and want to ensure you don’t overspend. Your program will:
# 1. Ask for the user’s total budget.
# 2. Let them enter item prices one by one.
# 3. Stop when the budget is exhausted and give a summary.
# Key Python Concepts Covered: Input/Output (input(), print()), Loops (while),
# Conditionals (if-else), Basic Arithmetic (updating totals), Data Types (float, string)
new_list = []
budget_input = input("What's your total budget for groceries: $")
sum_budget = 0
while True:
    user_input = input("Enter item price (or '0' to finish): $")
    if user_input == '0':
        break
    new_list.append(user_input)
    sum_budget += float(user_input)
    if sum_budget > float(budget_input):
        over_budget = sum_budget - float(budget_input)
        print(f"You're ${over_budget} over your budget!")
        print(f"\n\nTotal spent: ${sum_budget}")
        print(f"You have exceeded your budget!")
        break
print(sum_budget)