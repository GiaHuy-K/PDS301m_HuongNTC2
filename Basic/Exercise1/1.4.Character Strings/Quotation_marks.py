# It's often useful to be able to include quotation marks in a string, such as when you might specify a variable in a
# query. Single quotes are paired with other single quotes, and double quotes are paired with other double quotes.
# Alternatively, you can use the escape method \" or \' to include that quotation mark within a string; or you
# can use triple quotation marks to do the same thing. The following three examples (and you could come up with
# more) are equivalent.
selstr1 = '"elev" > 1000'
selstr2 = "\"elev\" > 1000"
selstr3 = """"elev" > 1000"""
print(selstr1 + "\n" + selstr2 + "\n" + selstr3)

print("\n")
print("Other example:")
name1 = '"huy" said, "I\'ll be back."'
name2 = "'huy' said, \"I'll be back.\""
name3 = '''"huy" said, "I'll be back."'''
print(name1 + "\n" + name2 + "\n" + name3)

print("\n")
print("Using positions in strings:")
# The .find() method is useful for finding the first occurrence of a substring. Explore Python help on .find()
# to find ways of finding something other than the first occurrence
p = 'd:/work/lu.shp.'
print(p.find('.'))

print(p[p.find('.'):])
print(p.split("/"))
pos2 = p.find(".", p.find('.')+1)
print(pos2)  # from the second "." to the end

#Raw strings for dealing with backslashes

p = "Jerry's Kids"
print(p)
p1 = p.split(" ")
print(p1[0])
print(p1[1])