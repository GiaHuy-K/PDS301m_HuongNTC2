#Exercise 1
raw_name = "   Nguc trung vo tuu diec vo hoa    "
print(raw_name.strip().title())  # Expected Output: Nguc Trung Vo Tuu Diec Vo Hoa

#Exercise 2
quote = "The only way to do great work is to love what you do."
# 1. Print the total number of characters in the quote.
print(f"Length: {len(quote)}")

# 2. Print the first character of the quote.
print(f"First char: {quote[0]}")

# 3. Print the last character of the quote.
print(f"Last char: {quote[-1]}")
# 4. Using slicing, extract and print the word "love".
# Hint: Find the start and end index of the word first.
print(f"Slice: {quote[36:40]}")

#Exercise 3
print("Exercise 3")
template = "Hello, my name is {name} and I am {age} years old."
name = input("Enter your name: ")
age = input("Enter your age: ")
update_template = template.format(name=name, age=age)
#update_template = template.replace("{name}", name).replace("{age}", age)
print(update_template)