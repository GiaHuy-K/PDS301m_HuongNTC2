import scrapy
import csv
import json
from datetime import datetime
from scrapy.crawler import CrawlerProcess
import os
print("Directory:", os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lesson\Day10.21.2025")
# ----- CÁCH 1: SPIDER NÂNG CAO TỰ LƯU FILE -----
class AdvancedQuotesSpider(scrapy.Spider):
    name = "advanced_quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def __init__(self):
        """Khởi tạo spider, tạo file và ghi header"""
        super().__init__()
        self.csv_file = 'quotes_data.csv'
        self.json_file = 'quotes_data.json'
        self.data_count = 0

        # Khởi tạo CSV với header
        with open(self.csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Quote', 'Author', 'Tags', 'URL', 'Timestamp'])

        # Khởi tạo JSON file
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)

    def save_to_csv(self, data):
        """Lưu dữ liệu vào CSV"""
        with open(self.csv_file, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                data['id'],
                data['quote'],
                data['author'],
                ', '.join(data['tags']), # Join list tags thành string
                data['url'],
                data['timestamp']
            ])

    def save_to_json(self, data):
        """Lưu dữ liệu vào JSON"""
        with open(self.json_file, 'r+', encoding='utf-8') as file:
            existing_data = json.load(file)
            existing_data.append(data)
            file.seek(0) # Quay về đầu file
            json.dump(existing_data, file, ensure_ascii=False, indent=4)

    def closed(self, reason):
        """Được gọi khi spider kết thúc"""
        print(f"🕷️ Spider đã kết thúc: {reason}")
        print(f"📊 Tổng số quotes đã crawl: {self.data_count}")

    def parse(self, response):
        """Hàm parse chính để trích xuất dữ liệu"""
        for quote in response.css('div.quote'):
            self.data_count += 1
            quote_data = {
                'id': self.data_count,
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
                'url': response.url,
                'timestamp': datetime.now().isoformat()
            }
            
            # Lưu vào cả CSV và JSON
            self.save_to_csv(quote_data)
            self.save_to_json(quote_data)
            
            yield quote_data

        # Pagination (Phân trang)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)


# ----- CÁCH 2: SỬ DỤNG BUILT-IN FEEDS CỦA SCRAPY -----
class QuotesSpiderWithFeeds(scrapy.Spider):
    name = "quotes_feeds"
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    # Cấu hình để Scrapy tự động xuất file
    custom_settings = {
        'FEEDS': {
            'quotes.csv': {
                'format': 'csv',
                'fields': ['quote', 'author', 'tags', 'url'], # Chọn các trường
                'encoding': 'utf8',
            },
            'quotes.json': {
                'format': 'json',
                'encoding': 'utf8',
                'indent': 4,
            },
        },
        'FEED_EXPORT_ENCODING': 'utf-8',
    }

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'quote': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': ', '.join(quote.css('div.tags a.tag::text').getall()),
                'url': response.url,
            }
        
        # Pagination (Phân trang)
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)


# ----- KHỐI LỆNH ĐỂ CHẠY SPIDER -----
if __name__ == "__main__":
    print("🚀 Bắt đầu crawling quotes...")
    
    # Cấu hình process
    process = CrawlerProcess(settings={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'CONCURRENT_REQUESTS': 1, # Số request đồng thời
        'DOWNLOAD_DELAY': 1,      # Độ trễ giữa các request
        'ROBOTSTXT_OBEY': True,   # Tuân thủ file robots.txt
        'LOG_LEVEL': 'INFO',      # Mức độ log
    })
    
    # Chọn spider bạn muốn chạy
    process.crawl(AdvancedQuotesSpider)  # Hoặc chạy: QuotesSpiderWithFeeds
    process.start() # Script sẽ dừng ở đây cho đến khi crawl xong

    # Đọc và hiển thị kết quả (Phần này chỉ hoạt động tốt với AdvancedQuotesSpider)
    try:
        import pandas as pd
        df = pd.read_csv('quotes_data.csv')
        print("\n📄 Preview dữ liệu CSV:")
        print(df.head())
    except Exception as e:
        print(f"\n✅ Dữ liệu đã được lưu thành công! (Không thể preview: {e})")