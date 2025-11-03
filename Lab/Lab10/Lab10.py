import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Directory",os.getcwd())
os.chdir(r"C:\Users\Admin\Desktop\PDS301m_HuongNTC2\PDS301m_HuongNTC2-\Lab\Lab10")
print("Exercise 1: ")

# 1. Create a sample dataset for the A/B test
data = {
    'user_id': range(1, 201),
    'group': ['A']*100 + ['B']*100,
    'converted': np.random.choice([0, 1], 200, p=[0.8, 0.2]) # Dummy data for Group A
}
# Make Group B slightly better
data['converted'][100:] = np.random.choice([0, 1], 100, p=[0.75, 0.25])
ab_test_df = pd.DataFrame(data)

# 2. Handle potential complex data issues (e.g., custom methods)
# Let's say we want a text label for conversion
def get_status(n):
    return 'Converted' if n == 1 else 'Not Converted'

# Apply a custom function to create a new column
ab_test_df['status'] = ab_test_df['converted'].apply(get_status)

# 3. Aggregate the data to calculate conversion rates
conversion_rates = ab_test_df.groupby('group')['converted'].mean()
print("\nConversion Rates by Group:\n", conversion_rates)

# 4. Analyze the result
if conversion_rates['B'] > conversion_rates['A']:
    print("\nConclusion: Group B performed better.")
else:
    print("\nConclusion: Group A performed better.")

print("\n")
print("=="*20)

print("Exercise 2: ")
customers = pd.DataFrame({
    'customer_id': range(1, 11),
    'customer_name': [f'Customer_{i}' for i in range(1, 11)]
})

# Create products data
products = pd.DataFrame({
    'product_id': range(101, 106),
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    'category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Accessories']
})

# Create orders data
orders = pd.DataFrame({
    'order_id': range(1001, 1021),
    'customer_id': np.random.randint(1, 11, 20),
    'order_date': pd.to_datetime(pd.date_range(start='2025-01-15', periods=20, freq='D'))
})

# Create order items data
order_items = []
for order_id in orders['order_id']:
    num_items = np.random.randint(1, 4)
    for _ in range(num_items):
        product_id = np.random.randint(101, 106)
        quantity = np.random.randint(1, 5)
        price_per_item = products.loc[products['product_id'] == product_id, 'product_id'].iloc[0] * 2.5 + np.random.uniform(0, 50)
        order_items.append([order_id, product_id, quantity, round(price_per_item, 2)])

order_items_df = pd.DataFrame(order_items, columns=['order_id', 'product_id', 'quantity', 'price_per_item'])

# Save to CSV
customers.to_csv('customers.csv', index=False)
products.to_csv('products.csv', index=False)
orders.to_csv('orders.csv', index=False)
order_items_df.to_csv('order_items.csv', index=False)

print("Sample data files created successfully.")

# Load data
orders = pd.read_csv('orders.csv')
order_items = pd.read_csv('order_items.csv')
products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')

# --- Data Preparation ---
# Convert order_date to datetime objects
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Calculate the total price for each order item
order_items['total_price'] = order_items['quantity'] * order_items['price_per_item']

# Merge DataFrames to create a single master view
# Merge orders with order_items
df = pd.merge(orders, order_items, on='order_id')
# Add product information
df = pd.merge(df, products, on='product_id')
# Add customer information
df = pd.merge(df, customers, on='customer_id')

print("Data loaded and merged successfully. Here is a sample:")
print(df.head())


# Set order_date as the index
df.set_index('order_date', inplace=True)

# Resample data by month and sum the total_price
monthly_sales = df['total_price'].resample('M').sum()

# Plot the results
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o')
plt.title('Total Monthly Sales for Jan 2025')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.grid(True)
plt.show()

print("Monthly Sales:\n", monthly_sales)

# Group by product name and sum the quantities
top_products = df.groupby('product_name')['quantity'].sum().nlargest(5)

# Plot the results
plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind='barh', color='skyblue')
plt.title('Top 5 Best-Selling Products by Quantity')
plt.xlabel('Total Quantity Sold')
plt.ylabel('Product Name')
plt.show()

print("Top 5 Products:\n", top_products)

# Group by customer and sum their total spending
top_customers = df.groupby('customer_name')['total_price'].sum().nlargest(5)

print("Top 5 Highest-Spending Customers:\n", top_customers)

# Group by category and sum the total price
category_revenue = df.groupby('category')['total_price'].sum().sort_values(ascending=False)

print("\nRevenue by Product Category:\n", category_revenue)
