# Strings can be dealt with as a list of characters, with the first one having a zero index. A set of string characters
# can be defined with a format like 1:3, meaning "from the beginning of 1 to the beginning of 3" -- so it doesn't
# display the character that is at index 3.
s = "the science of where"
print(s[0])      # first character
s1 = s[1]
print(s1)
print(s[2])
print(s[-5:])
print(s[4:11])
print(s.split(" ")[1])
print("String splitting and using len(): ")
# As we just saw, strings are indexed like lists, and another similarity is what you get with the len() function. The
# .split() method is very useful for breaking apart a string into components based on a separator. Note how
# len() is used here
words = s.split(" ")
print(words)
print(len(words))
print(len(words)-1)
print(words[len(words)-1])
print(len(words[len(words)-1]))
print(len(s))

print("\n")
print("Concatenating strings")
print(words[3] + words[1])
print(words[3] + " " + words[1])

print("\n")
print("The escape character (\\)")
# The backslash is an "escape character" which is used for special needs that can't be easily typed. For instance,
# you can include a single quote alone with \' , a new line with \n and a tab with \t .
print('Jerry\'s Kids')
print('\nJerry\'s\nKids')

print('d:\\work\\soil.shp')
print(r'd:\work\soil.shp')  # raw string ignores escape characters