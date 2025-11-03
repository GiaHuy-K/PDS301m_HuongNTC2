import json 
import os
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Assignment\Data_Assignment")
print("Đang đọc inventory.txt...")
inventory_list = [] # List để chứa các dict
try:
    with open('inventory.txt', 'r') as f:
        for line in f:
            
            line = line.strip() 
            if line: # Bỏ qua các dòng trống
                # Tách chuỗi bằng dấu phẩy
                name, price, category, stock = line.split(',')
                
                
                item_dict = {
                    'name': name,
                    'price': float(price), # Chuyển "1.50" thành số 1.50
                    'category': category,
                    'stock': int(stock) # Chuyển "100" thành số 100
                }
                inventory_list.append(item_dict)
                
    print(" -> Đã đọc xong inventory.txt. Dữ liệu:")
    print(inventory_list)

except FileNotFoundError:
    print("LỖI: Không tìm thấy file 'inventory.txt'.")
    exit() # Thoát chương trình nếu không có file
except Exception as e:
    print(f"LỖI khi đọc inventory.txt: {e}")
    exit()


# --- Phần 2: Đọc file discounts.json ---
print("\nĐang đọc discounts.json...")
try:
    with open('discounts.json', 'r') as f:
        # Dùng json.load() để tự động chuyển file JSON thành dict Python
        discounts_dict = json.load(f)
        print(" -> Đã đọc xong discounts.json. Dữ liệu:")
        print(discounts_dict)
        
except FileNotFoundError:
    print("LỖI: Không tìm thấy file 'discounts.json'.")
    exit()
except json.JSONDecodeError:
    print("LỖI: File 'discounts.json' có nội dung không hợp lệ.")
    exit()


# --- Phần 3: Xử lý và Ghi ra file summary.txt ---
print("\nĐang xử lý và ghi ra 'inventory_summary.txt'...")
try:
    with open('inventory_summary.txt', 'w', encoding='utf-8') as f:
        f.write("--- TÓM TẮT KHO HÀNG ---\n")
        
        total_value = 0
        for item in inventory_list:
            category = item['category']
            
            # Lấy % giảm giá. Dùng .get() để an toàn (nếu category không có thì trả về 0)
            discount_percent = discounts_dict.get(category, 0)
            
            # Tính toán
            item_value = item['price'] * item['stock']
            total_value += item_value
            
            # Ghi vào file
            f.write(f"Món hàng: {item['name']} ({item['category']})\n")
            f.write(f"  Giá: ${item['price']:.2f}\n")
            f.write(f"  Tồn kho: {item['stock']}\n")
            f.write(f"  Giảm giá: {discount_percent}%\n")
            f.write(f"  Tổng giá trị món: ${item_value:.2f}\n")
            f.write("---------------------\n")
            
        f.write(f"\nGIÁ TRỊ TỔNG CỘNG CỦA KHO HÀNG: ${total_value:.2f}\n")
        
    print(" -> Đã ghi file summary thành công!")

except IOError:
    print("LỖI: Không thể ghi file 'inventory_summary.txt'.")
    
import pandas as pd 
print("\n--- BẮT ĐẦU BÀI 6: PANDAS ---")

try:
    df = pd.DataFrame(inventory_list)
    print(" -> Đã tải dữ liệu vào Pandas DataFrame:")
    print(df.to_string()) 
except NameError:
    print("LỖI: Không tìm thấy 'inventory_list'. Cưng đã thực sự code Bài 5 chưa?")
    exit()
except Exception as e:
    print(f"LỖI khi tạo DataFrame: {e}")
    exit()

# --- 2. Tính toán Giá đã giảm (Discounted prices) ---
print("\n -> Đang tính toán giá đã giảm...")
df['discount_percent'] = df['category'].map(discounts_dict).fillna(0)

# Tính giá cuối cùng (tạo cột mới)
df['discounted_price'] = df['price'] * (1 - df['discount_percent'] / 100)
print("\nDataFrame sau khi tính giảm giá:")
print(df.to_string())

# --- 3. Tính toán Tổng giá trị tồn kho (Total value) ---
print("\n -> Đang tính toán tổng giá trị tồn kho...")
df['total_value'] = df['price'] * df['stock']

print("\nDataFrame cuối cùng (với total_value):")
print(df.to_string())

# In ra tổng giá trị của toàn bộ kho hàng
total_inventory_value = df['total_value'].sum()
print("\n-------------------------------------------")
print(f"TỔNG GIÁ TRỊ TOÀN BỘ KHO (PANDAS): ${total_inventory_value:.2f}")
print("--- KẾT THÚC BÀI 6 ---")