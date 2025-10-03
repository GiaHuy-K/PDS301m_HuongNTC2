def create_products():
    n = int(input("How many products you wanna add? "))
    products = []
    for i in range(n):
        name = input(f"Enter the {i+1} item name: ")
        price = float(input(f"Enter the {i+1} item price: "))
        products.append((name, price))
    return products

def add_to_cart(cart, products):
    cart.extend(products)
    return cart

def track_unique_items(unique_items, products):
    for p in products:
        unique_items.add(p[0])
    return unique_items

def store_product(products_dict, products):
    for name, price in products:
        products_dict[name] = price
    return products_dict

def calculate_total(cart):
    return sum(price for _, price in cart)


# --- Main program ---
cart = []
unique_items = set()
products_dict = {}


while True:
    print("\n--- Menu ---")
    print("1. Add new products")
    print("2. View cart")
    print("3. View unique items")
    print("4. View product dictionary")
    print("5. Calculate total and exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        products = create_products()
        add_to_cart(cart, products)
        track_unique_items(unique_items, products)
        store_product(products_dict, products)
    elif choice == "2":
        print("Cart:", cart if cart else "empty")
    elif choice == "3":
        print("Unique items:", unique_items if unique_items else "empty")
    elif choice == "4":
        print("Products dict:", products_dict if products_dict else "empty")
    elif choice == "5":
        print("Total:", calculate_total(cart))
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1-5.")


