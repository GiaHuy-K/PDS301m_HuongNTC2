inventory = {
    "Laptop" : 12,
    "Mouse" : 55,
    "Keyboard": 30
}
print("Initial Inventory:", inventory)

#2. Add a new product
inventory ["Webcam"] = 20
print("After adding Webcam:", inventory )

#3. Update stock (shipment of 15 laptops arrived)
inventory ["Laptop"] += 15
print("After updating Laptop stock: ", inventory)

#4. Process a sale (customer bought 5 mice)
inventory["Mouse"] -= 5

#5. Print the final stock report 
print("\n--- Final Inventory Report ---")
for product, stock in inventory.items():
    print(f"Product: {product }, Stock Remaining: {stock}")
    
# tìm giá trị lớn nhất và nhỏ nhất trong dictionary

max_value = max(inventory.values())
min_value = min(inventory.values())
print("Original Dictionary:")
print(inventory)
print(max_value)
print(min_value)
