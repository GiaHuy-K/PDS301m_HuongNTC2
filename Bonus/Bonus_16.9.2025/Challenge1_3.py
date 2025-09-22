
# 1. Create a tuple containing the names of five countries and display the whole tuple. 
# Ask the user to enter one of the countries that have been shown to them and then display
# the index number (i.e. position in the list) of that item in the tuple. 
Country_name = ("VietNam", "France", "China", "Laos", "ThaiLand")
print(Country_name)

x = input("Enter country name and I will show u the index number: ")
if x in Country_name:
    print("Index:", Country_name.index(x))
else:
    print("Not in tuple")
    
# 2. Add to program 01 to ask the user to enter a number and display the country in that position
y = int(input("Enter a number and I will show u country: "))
if 0 <= y < len(Country_name):
    print("Country:", Country_name[y])
else:
    print("Out of range")
    
# 3. Create a list of two sports. Ask the user what their favorite sport is and add this to the end of the list. 
# Sort the list and display it.
Sports = ["Football","Basketball"]
print("Current list of sports: ", Sports)

z = input("Enter your favourite sport:")
Sports.append(z)
Sports.sort()
print("List after add new sport:", Sports)



