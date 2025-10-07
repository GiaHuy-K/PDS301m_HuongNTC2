
# Arbitrary arguments
# *args → allows multiple positional arguments (tuple).
# **kwargs → allows multiple keyword arguments (dictionary).
# When the number of arguments are unknown for a function, They can all be packed into a tuple as shown:
def printAll(*args):
    print("No of arguments:",len(args))
    for argument in args:
        print(argument)
# printAll with 3 arguments
printAll('Thit', 'Bo','Kobe')
# printAll with 4 arguments
printAll('LongBeach','Hehe','Baria','Vungtau')

print("\n============================================")
def printDictionary(**args):
    for key in args:
        print(key +" : " + args[key])
printDictionary(Country = 'VietNam',Province = 'Ho Chi Minh', City = 'Ho Chi Minh')


