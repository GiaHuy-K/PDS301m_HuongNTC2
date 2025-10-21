import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
print("Directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day10.21.2025")

# 1. Khởi tạo Chrome driver
print("🚀 Đang khởi tạo trình duyệt...")
options = Options()
options.add_argument('--headless')  # Chạy ẩn browser
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Chuẩn bị list để lưu dữ liệu
all_products_data = []
html_content = None # Khởi tạo biến html_content

# 2. Truy cập website và cuộn trang để load hết sản phẩm
try:
    print("🔎 Đang truy cập website...")
    driver.get("https://nhasachphuongnam.com/van-hoc-duong-dai.html")

    # Chờ trang Load hoàn tất
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Cuộn trang để Load tất cả sản phẩm
    print("📜 Đang cuộn trang để load tất cả sản phẩm...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Chờ 2 giây để nội dung mới load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("...Đã cuộn đến cuối trang.")
            break
        last_height = new_height

    # Lấy HTML content sau khi đã load hết
    html_content = driver.page_source
    print("✅ Đã lấy HTML content thành công.")

finally:
    driver.quit()
    print("💨 Đã đóng browser.")

# 3. Dùng BeautifulSoup với HTML đã render
soup = BeautifulSoup(html_content, 'html.parser')

# 4. Tìm tất cả sản phẩm - phân tích cấu trúc HTML thực tế
print("🔄 Đang phân tích sản phẩm...")

# Thử các selector khác nhau để tìm sản phẩm
products = []

# Cách 1: Tìm theo class thông thường
products = soup.find_all('div', class_=re.compile(r'product|item|prod', re.I))

# Cách 2: Nếu không tìm thấy, thử tìm theo data-product-type
if not products:
    print("...Cách 1 không thành công, thử Cách 2 (data-product-type)")
    products = soup.find_all(attrs={"data-product-type": True})

# Cách 3: Tìm tất cả div/li có chứa thông tin sản phẩm
if not products:
    print("...Cách 2 không thành công, thử Cách 3 (selector CSS)")
    products = soup.select('div[class*="product"], li[class*="product"], div[class*="item"], li[class*="item"]')

print(f"📊 Tìm thấy {len(products)} sản phẩm")

# 5. Thu thập dữ liệu
for i, product in enumerate(products):
    try:
        # --- Tên sách ---
        name = "N/A"
        name_selectors = [
            product.find('h2', class_=re.compile(r'product|name|title', re.I)),
            product.find('h3', class_=re.compile(r'product|name|title', re.I)),
            product.find('a', class_=re.compile(r'product|name|title', re.I)),
            product.find(attrs={"data-product-name": True}),
            product.find('div', class_=re.compile(r'name|title', re.I)),
        ]
        for selector in name_selectors:
            if selector and selector.text.strip():
                name = selector.text.strip()
                break
        
        # --- Giá ---
        price = "N/A"
        price_selectors = [
            product.find('span', class_=re.compile(r'price|special', re.I)),
            product.find('div', class_=re.compile(r'price', re.I)),
            product.find(attrs={"data-price": True}),
            product.find('span', class_=re.compile(r'money|currency', re.I)),
        ]
        for selector in price_selectors:
            if selector and selector.text.strip():
                price = selector.text.strip()
                # Làm sạch giá
                price = re.sub(r'\s+', ' ', price).strip()
                break

        # --- Tác giả ---
        author = "N/A"
        author_selectors = [
            product.find('div', class_=re.compile(r'author|writer', re.I)),
            product.find('span', class_=re.compile(r'author|writer', re.I)),
            product.find('p', class_=re.compile(r'author|writer', re.I)),
        ]
        for selector in author_selectors:
            if selector and selector.text.strip():
                author = selector.text.strip()
                break

        # --- Link chi tiết ---
        link = "N/A"
        link_selectors = [
            product.find('a', href=True),
            product.find('a', class_=re.compile(r'product|link', re.I)),
        ]
        for selector in link_selectors:
            if selector and selector.get('href'):
                href = selector['href']
                if href and not href.startswith('javascript:'):
                    link = "https://nhasachphuongnam.com" + href if not href.startswith('http') else href
                    break

        # --- Hình ảnh ---
        image = "N/A"
        img_selectors = [
            product.find('img', src=True),
            product.find('img', class_=re.compile(r'product|image', re.I)),
        ]
        for selector in img_selectors:
            if selector and selector.get('src'):
                img_src = selector['src']
                if img_src and not img_src.startswith('data:image'):
                    image = "https://nhasachphuongnam.com" + img_src if not img_src.startswith('http') else img_src
                    break

        # Chỉ Lưu nếu có tên sách
        if name != "N/A":
            product_data = {
                'STT': i + 1,
                'Tên sách': name,
                'Tác giả': author,
                'Giá': price,
                'Link chi tiết': link,
                'Hình ảnh': image
            }
            all_products_data.append(product_data)
            print(f"✓ Đã thu thập: {name}")
            
    except Exception as e:
        print(f"❌ Lỗi khi xử lý sản phẩm {i+1}: {e}")
        continue

# 6. Lưu vào CSV
if all_products_data:
    df = pd.DataFrame(all_products_data)

    # Lưu file CSV
    csv_filename = 'nhasachphuongnam_vanhoc_duongdai.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

    print(f"\n✅ ĐÃ HOÀN THÀNH!")
    print(f"Đã thu thập được {len(all_products_data)} sản phẩm")
    print(f"Dữ liệu đã được lưu vào file: {csv_filename}")

    # Hiển thị preview
    print(f"\n📊 Preview dữ liệu:")
    print(df.head(10).to_string(index=False))

else:
    print("\n❌ Không tìm thấy sản phẩm nào!")
    
    # Debug: Lưu HTML để phân tích
    if html_content:
        with open('debug_page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())
        print("Đã lưu file debug_page.html để phân tích cấu trúc HTML")