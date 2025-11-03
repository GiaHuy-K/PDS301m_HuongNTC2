# Creating a set with curly braces
languages = {"python", "java", "go", "python"}
print(f"Languages set: {languages}")  # Notice 'python' only appears once

# Creating a set from a list to get unique items
numbers = [1, 2, 2, 3, 4, 3, 5]
unique_numbers = set(numbers)
print(f"Unique numbers: {unique_numbers}")

# Creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)
# Add a single item
languages.add("rust")
print(f"After adding 'rust': {languages}")

# Remove an item
# .remove() will raise an error if the item is not found
languages.remove("java")

# .discard() will NOT raise an error if the item is not found
languages.discard("c++") # No error, even though 'c++' is not in the set
print(f"After removing items: {languages}")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union (|): All unique items from both sets
union_set = set_a | set_b
print(f"Union: {union_set}")

# Intersection (&): Items that are in BOTH sets
intersection_set = set_a & set_b
print(f"Intersection: {intersection_set}")

# Difference (-): Items in set_a but NOT in set_b
difference_set = set_a - set_b
print(f"Difference (A - B): {difference_set}")

# Symmetric Difference (^): Items in either set, but NOT in both
symmetric_diff_set = set_a ^ set_b
print(f"Symmetric Difference: {symmetric_diff_set}")


# Exercises---------------------------------------------------------------------
print(f"Exercise 1: Comparing Student Enrollments:") 
# 1. Define the lists of students
robotics_club = ["Alice", "Bob", "Charlie", "David"]
debate_club = ["Charlie", "Eve", "Frank", "Alice"]

# 2. Convert lists to sets
robotics_set = set(robotics_club)
debate_set = set(debate_club)
print(f"Robotics Club Members: {robotics_set}")
print(f"Debate Club Members: {debate_set}")

# 3. Perform analysis using set operations
all_students = robotics_set | debate_set
both_clubs = robotics_set & debate_set
robotics_only = robotics_set - debate_set

print("\n--- Club Enrollment Analysis ---")
print(f"All unique students: {all_students}")
print(f"Students in both clubs: {both_clubs}")
print(f"Students only in the Robotics Club: {robotics_only}")
print("--------------------------------\n")
print(f"Exercise 2: Data Deduplication :")
def deduplicate_emails(email_list):
    """Removes duplicate emails from a list using a set."""
    # Convert the list to a set to automatically remove duplicates
    unique_email_set = set(email_list)
    # Convert the set back to a list
    return list(unique_email_set)

# --- Test the function ---
emails = [
    "user1@example.com",
    "user2@example.com",
    "user1@example.com", # Duplicate
    "user3@example.com",
    "user2@example.com"  # Duplicate
]

unique_emails = deduplicate_emails(emails)
print(f"Original list: {emails}")
print(f"Unique list: {unique_emails}")
print("--------------------------------\n")

print(f"Exercise 3: Comparing Tag Similarities :")

article1_tags = {"python", "data science", "pandas", "machine learning"}
article2_tags = {"python", "web development", "django", "data science"}

# 1. Find common tags using intersection (&)
common_tags = article1_tags & article2_tags
print(f"Common Tags: {common_tags}")

# 2. Find tags unique to the first article using difference (-)
unique_to_article1 = article1_tags - article2_tags
print(f"Tags unique to Article 1: {unique_to_article1}")

print("--------------------------------\n")
print(f"Exercise 4: Checking User Permissions :")
def can_access_dashboard(user_permissions, required_permissions):
    """Checks if the user's permissions contain all required permissions."""
    # .issubset() checks if all items in one set exist in another
    return required_permissions.issubset(user_permissions)

# --- Test the function ---
required = {"view_users", "edit_content"}

user_admin_perms = {"view_users", "edit_content", "delete_users", "admin_access"}
user_editor_perms = {"edit_content", "view_users"}
user_viewer_perms = {"view_users"}

print(f"Admin can access? {can_access_dashboard(user_admin_perms, required)}")
print(f"Editor can access? {can_access_dashboard(user_editor_perms, required)}")
print(f"Viewer can access? {can_access_dashboard(user_viewer_perms, required)}")