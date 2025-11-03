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
import sys # Dùng để thoát chương trình

# --- 1. ĐỊNH NGHĨA CÁC KHUÔN (CLASSES) ---

class GroceryItem:

    def __init__(self, name, price, category, stock):
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def __str__(self):
        """Hàm này giúp khi mình print(item) nó sẽ ra chuỗi đẹp hẹ hẹ hẹ"""
        return f"{self.name} (${self.price:.2f}) - [Còn lại: {self.stock}]"

class ShoppingCart:

    def __init__(self):
        self.items = [] # Giỏ hàng là một list rỗng lúc đầu

    def add_item(self, item, quantity):
        """Thêm một (hoặc nhiều) món hàng vào giỏ"""
        # (Trong bài toán thực tế, ta nên kiểm tra 'item' có trong kho không)
        print(f"   -> Đã thêm {quantity} x {item.name} vào giỏ.")
        # Tạm thời đơn giản hóa: thêm 'quantity' lần
        for _ in range(quantity):
            self.items.append(item)
            item.stock -= 1 # Giảm tồn kho
        
    def remove_item(self, item_name):
        """Xóa MỘT món hàng khỏi giỏ bằng tên"""
        # Dùng 'next' để tìm item đầu tiên trong giỏ có tên khớp
        # Đây là ví dụ về Exception Handling (StopIteration)
        try:
            item_to_remove = next(item for item in self.items if item.name.lower() == item_name.lower())
            self.items.remove(item_to_remove)
            item_to_remove.stock += 1 # Hoàn trả lại hàng vào kho
            print(f"   -> Đã xóa 1 x {item_to_remove.name} khỏi giỏ.")
            return True
        except StopIteration:
            print(f"   LỖI: Không tìm thấy '{item_name}' trong giỏ của bạn.")
            return False

    def calculate_total(self):
        """Tính tổng tiền trong giỏ, có áp dụng giảm giá"""
        total = 0
        if not self.items:
            return total # Trả về 0 nếu giỏ rỗng

        print("\n--- Hóa đơn chi tiết ---")
        for item in self.items:
            discounted_price = apply_discount(item) # Gọi hàm giảm giá
            total += discounted_price
            if discounted_price < item.price:
                print(f" - {item.name}: ${discounted_price:.2f} (đã giảm giá 10%)")
            else:
                print(f" - {item.name}: ${discounted_price:.2f}")
                
        print("-------------------------")
        return total

class Store:
    """
    Khuôn (Class) cho cửa hàng. Quản lý kho hàng (inventory).
    """
    def __init__(self):
        # Khởi tạo kho hàng (list các đối tượng GroceryItem)
        self.inventory = [
            GroceryItem("Apple", 1.50, "Fruits", 100),
            GroceryItem("Milk", 2.00, "Dairy", 50),
            GroceryItem("Bread", 3.25, "Bakery", 30),
            GroceryItem("Banana", 0.75, "Fruits", 150)
        ]

    def browse_inventory(self):
        """In ra tất cả các món hàng trong kho"""
        print("\n--- 🥑 Hàng trong kho (Inventory) ---")
        for item in self.inventory:
            print(f" - {item.category} | {item.name} (${item.price:.2f}) - [Còn lại: {item.stock}]")
            
    def find_item(self, item_name):
        """Tìm một món hàng trong kho bằng tên"""
        try:
            # Dùng 'next' để tìm item đầu tiên
            item = next(item for item in self.inventory if item.name.lower() == item_name.lower())
            
            # Xử lý lỗi tồn kho (Custom Exception)
            if item.stock <= 0:
                raise ValueError(f"   LỖI: {item.name} đã hết hàng!")
                
            return item
        except StopIteration:
            print(f"   LỖI: Không tìm thấy món hàng '{item_name}' trong kho.")
            return None
        except ValueError as e:
            # Bắt lỗi hết hàng (out-of-stock)
            print(e)
            return None


# --- 2. ĐỊNH NGHĨA CÁC HÀM HỖ TRỢ (FUNCTIONS) ---

def show_menu():
    """Hàm này chỉ để in ra menu cho đẹp"""
    print("\n--- 🛒 Siêu thị Nice-Nice của Yuhai🛒 ---")
    print("1. Xem hàng trong kho (Browse)")
    print("2. Thêm hàng vào giỏ (Add)")
    print("3. Xóa hàng khỏi giỏ (Remove)")
    print("4. Thanh toán (Checkout)")
    print("0. Thoát (Exit)")
    print("----------------------------")

def apply_discount(item):
    """
    Hàm nhận vào 1 'item' (Object) và trả về giá (return)
    Áp dụng giảm giá 10% nếu là 'Fruits'.
    """
    if item.category == "Fruits":
        return item.price * 0.90  # Giảm 10%
    return item.price # Trả về giá gốc


# --- 3. CHƯƠNG TRÌNH CHÍNH (MAIN LOGIC) ---

def main():
    # Khởi tạo các đối tượng
    my_store = Store()
    my_cart = ShoppingCart()

    # Vòng lặp chính của chương trình
    while True:
        show_menu()
        
        # Xử lý lỗi Exception Handling (ValueError) khi nhập menu
        try:
            choice = int(input("Vui lòng chọn (0-4): "))
        except ValueError:
            print("   LỖI: Vui lòng nhập SỐ (0-4).")
            continue # Quay lại đầu vòng lặp

        # Điều hướng (Branching) dùng if-elif-else
        if choice == 1:
            # 1. Xem hàng
            my_store.browse_inventory()

        elif choice == 2:
            # 2. Thêm vào giỏ
            my_store.browse_inventory() # Cho khách xem hàng trước
            item_name = input("   Nhập tên món hàng muốn thêm: ")
            
            # Gọi phương thức của Store để tìm
            item_to_add = my_store.find_item(item_name)
            
            if item_to_add: # Nếu tìm thấy (không phải None)
                try:
                    quantity = int(input(f"   Nhập số lượng '{item_name}' muốn mua (còn {item_to_add.stock}): "))
                    if quantity <= 0:
                        print("   LỖI: Số lượng phải > 0.")
                    elif quantity > item_to_add.stock:
                        print(f"   LỖI: Chỉ còn {item_to_add.stock} món, không đủ hàng.")
                    else:
                        # Gọi phương thức của Cart để thêm
                        my_cart.add_item(item_to_add, quantity)
                except ValueError:
                    print("   LỖI: Vui lòng nhập SỐ.")

        elif choice == 3:
            # 3. Xóa khỏi giỏ
            if not my_cart.items:
                print("   Giỏ hàng của bạn đang rỗng.")
            else:
                item_name = input("   Nhập tên món hàng muốn XÓA khỏi giỏ: ")
                # Gọi phương thức của Cart để xóa
                my_cart.remove_item(item_name)

        elif choice == 4:
            # 4. Thanh toán
            total_cost = my_cart.calculate_total()
            print(f"💰 TỔNG TIỀN CẦN THANH TOÁN: ${total_cost:.2f}")
            print("--- Cảm ơn đã mua sắm! ---")
            break # Thoát vòng lặp while

        elif choice == 0:
            # 0. Thoát
            print("--- Tạm biệt! Hẹn gặp lại! ---")
            break # Thoát vòng lặp while
            # sys.exit() # Hoặc dùng cách này để thoát hẳn
            
        else:
            print("   LỖI: Lựa chọn không hợp lệ, vui lòng chọn lại (0-4).")

# --- Kích hoạt chương trình ---
if __name__ == "__main__":
    main()