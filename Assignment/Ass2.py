# Exercise 2: Advanced Grocery Shopping Tracker
# Based on an exercise 1, write a program to enhance the budget tracker to include item names,
# categorize purchases, apply discounts, and generate a detailed receipt.
# Key Python Concepts Covered: Lists: Track multiple purchases dynamically; Tuples: Immutable
# (item, price, category) records; Dictionaries: Look up prices/discounts efficiently; String
# Formatting: Align receipt columns (:<10 for left-align); Logical Operators(discount); Boolean
# Flag: within_budget controls loop exit

item_list = ['Apple','Milk','Chips','Carrot','Bread']
category_list = ['Fruit','Dairy','Snacks','Vegetable','Bakery']
budget_input = input("Enter your budget: $")
while True:
    print(f"Available items: {item_list}")
    item = input("Enter item name (or 'done' to finish): ")
    item = item.capitalize()
    if item == 'done':
        break
    if item not in item_list:
        print("Item not found.")
        continue
    # category = category_list[item_list.index(item)]
    print(f"Enter category ({category_list} ): ")
    category = input().capitalize()
    if category not in category_list:
        print("Category not found.")
        continue
    match category:
        case 'Fruit':
            discount = 0.1
            print("Applied 10% discount! ")
        case 'Dairy':
            discount = 0.05
            print("Applied 5% discount! ")
        case 'Snacks':
            discount = 0.2
            print("Applied 20% discount!")
        case 'Vegetable':
            discount = 0.15
            print("Applied 15% discount!")
        case 'Bakery':
            discount = 0.1
            print("Applied 10% discount!")
        case _:
            discount = 0
        
        
