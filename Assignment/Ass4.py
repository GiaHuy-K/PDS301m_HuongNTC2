# Exercise 4: Build a modular grocery store system that handles
# inventory, shopping carts, and purchases with proper error handling
# and user interaction.
# 1. Conditions & Branching
# Implement a main menu with options:
# 1. Browse Inventory
# 2. Add to Cart
# 3. Remove from Cart
# 4. Checkout
# Use if-elif-else to navigate between options.
# Apply discounts conditionally based on item categories (e.g., 10% off fruits).

# 2. Loops
# Use a while loop to keep the program running until checkout.
# Iterate through inventory/cart with for loops to display items

# 3. Functions
# Define functions for modular tasks:
# show_menu(): Display options.
# browse_inventory(): List all items.
# apply_discount(item): Return discounted price.
# Use parameters and return values to pass data.

# 4. Exception Handling:
# Handle errors for:
# Invalid menu inputs (ValueError).
# Out-of-stock items (custom exception).
# Item not found in cart (StopIteration).

# 5. Classes & Objects
# Design classes:
# GroceryItem: Attributes like name, price, category, stock.
# ShoppingCart: Methods to add_item(), remove_item(), calculate total.
# Store: Manages inventory (list of GroceryItem objects).
# Use encapsulation (e.g., item.stock updated only via methods).

# 6. Additional Challenges
# File I/O: Save receipts to a .txt file.
# Admin Mode: Restock inventory or add new items.
# Purchase History: Log transactions with timestamps