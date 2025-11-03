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
    
print("==" *40 )
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

print("==" *40 )

import numpy as np 

print("\n--- BẮT ĐẦU BÀI 7: NUMPY ---")

try:
    prices_array_1d = df['price'].values
    stock_array_1d = df['stock'].values
    
    print(" -> Đã chuyển cột 'price' thành 1D NumPy array:")
    print(prices_array_1d)
    print(" -> Đã chuyển cột 'stock' thành 1D NumPy array:")
    print(stock_array_1d)

except NameError:
    print("LỖI: Không tìm thấy DataFrame 'df'. Cưng có thực sự đã chạy code Bài 6 chưa?")
    exit()
except Exception as e:
    print(f"LỖI khi chuyển đổi sang NumPy: {e}")
    exit()

# --- 2. Tính toán trên 1D array (Average Price) ---
print("\n -> Tính toán trên 1D array...")

avg_price = np.mean(prices_array_1d)

print(f"Giá trung bình (dùng NumPy): ${avg_price:.2f}")

# --- 3. Tính toán trên 2D array (Total Inventory Value) ---
print("\n -> Tính toán trên 2D array (Matrix)...")

total_value_per_item_array = prices_array_1d * stock_array_1d

print("Mảng 1D chứa tổng giá trị của từng món (Price * Stock):")
print(total_value_per_item_array)

# Tính tổng của cái mảng đó
total_inventory_value_numpy = np.sum(total_value_per_item_array)

print("\n-------------------------------------------")
print(f"💰 TỔNG GIÁ TRỊ TOÀN BỘ KHO (NUMPY): ${total_inventory_value_numpy:.2f}")
print("--- KẾT THÚC BÀI 7 ---")


print("==" *40 )
print("\n--- BẮT ĐẦU BÀI 8: TÍCH HỢP ---")

# --- 1. Tải dữ liệu Bán hàng (Sales) ---
try:
    # Đọc file CSV mới vào một DataFrame khác
    sales_df = pd.read_csv('sales.csv')
    print(" -> Đã tải file 'sales.csv':")
    print(sales_df.to_string())
except FileNotFoundError:
    print("LỖI: Không tìm thấy file 'sales.csv'. Anh đã tạo file này chưa?")
    exit()

# --- 2. Xử lý Giao dịch và Tính toán (Merge) ---
print("\n -> Đang gộp (merge) sales và inventory để lấy giá...")

try:
    # sales_with_details_df sẽ là bảng sales_df nhưng có thêm cột 'price', 'category', 'stock'...
    sales_with_details_df = pd.merge(
        sales_df, 
        df, 
        left_on='product', 
        right_on='name',
        how='left' # Giữ tất cả sales, kể cả nếu không tìm thấy trong kho
    )
except NameError:
    print("LỖI: Không tìm thấy DataFrame 'df'. Anh đã chạy code Bài 6 chưa?")
    exit()

# Áp dụng giảm giá (lấy từ Bài 6)
sales_with_details_df['discount_percent'] = sales_with_details_df['category'].map(discounts_dict).fillna(0)
sales_with_details_df['final_price'] = sales_with_details_df['price'] * (1 - sales_with_details_df['discount_percent'] / 100)

# Tính tổng tiền cho mỗi giao dịch
sales_with_details_df['total_sale'] = sales_with_details_df['final_price'] * sales_with_details_df['quantity']

print("\nBảng Sales sau khi gộp và tính toán:")
print(sales_with_details_df.to_string())

# --- 3. Tính toán Thống kê (NumPy) ---
print("\n -> Tính toán thống kê sales (dùng NumPy)...")

# Chuyển cột 'total_sale' thành NumPy array
total_sales_array = sales_with_details_df['total_sale'].values

# Dùng NumPy để tính
total_revenue = np.sum(total_sales_array)
avg_transaction_value = np.mean(total_sales_array)
total_items_sold = np.sum(sales_with_details_df['quantity'].values)

print(f"Tổng doanh thu (NumPy): ${total_revenue:.2f}")
print(f"Giá trị giao dịch trung bình (NumPy): ${avg_transaction_value:.2f}")
print(f"Tổng số món đã bán (NumPy): {total_items_sold}")

# --- 4. Cập nhật Tồn kho (Stock) (Pandas GroupBy) ---
print("\n -> Đang cập nhật tồn kho...")

# Tính tổng số lượng đã bán cho TỪNG món hàng
sales_summary_df = sales_df.groupby('product')['quantity'].sum().reset_index()
# Đổi tên cột 'quantity' thành 'quantity_sold' để không bị nhầm lẫn
sales_summary_df = sales_summary_df.rename(columns={'quantity': 'quantity_sold'})

print("\nBảng tổng hợp số lượng đã bán:")
print(sales_summary_df.to_string())

# Gộp bảng tổng hợp sales này vào bảng kho hàng (df)
updated_df = pd.merge(
    df,
    sales_summary_df,
    left_on='name',
    right_on='product',
    how='left' # Quan trọng: Giữ lại cả những món không bán được
)

# Điền 0 cho những món không bán (fillna)
updated_df['quantity_sold'] = updated_df['quantity_sold'].fillna(0).astype(int)

# Tính tồn kho MỚI
updated_df['new_stock'] = updated_df['stock'] - updated_df['quantity_sold']

print("\nBảng kho hàng (df) sau khi cập nhật stock:")
# In ra các cột quan trọng
print(updated_df[['name', 'stock', 'quantity_sold', 'new_stock']].to_string())

# --- 5. Lưu kết quả ra file MỚI ---
print("\n -> Đang lưu kho hàng đã cập nhật ra file...")

# Chuẩn bị 1 DataFrame sạch để lưu (chỉ lấy các cột cần thiết)
final_inventory_df = updated_df[['name', 'price', 'category', 'new_stock']]
final_inventory_df = final_inventory_df.rename(columns={'new_stock': 'stock'})

# Lưu ra CSV
try:
    final_inventory_df.to_csv('updated_inventory.csv', index=False, encoding='utf-8')
    print(" -> Đã lưu 'updated_inventory.csv' thành công!")
    final_inventory_df.to_json('updated_inventory.json', orient='records', indent=4)
    print(" -> Đã lưu 'updated_inventory.json' thành công!")

except IOError as e:
    print(f"LỖI khi ghi file: {e}")

print("\n--- HOÀN THÀNH TOÀN BỘ ASSIGNMENT (5-8) ---")