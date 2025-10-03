# 1
words = ["one", "two", "three"]
for x in words:
  print(x)

# 2
zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''
for char in zen:
   if char not in 'e': # thiếu e :<<
      print (char, end='')

# 3
numbers = [34,54,67,21,78,97,45,44,80,19]
total = 0
for num in numbers:
   if num%2 == 0:
      print (num)
      
# làm tí range nào bae 
# range(start, stop, step)
for num in range(5):
   print (num, end=' ')
print()
for num in range(10, 20):
   print (num, end=' ')
print()
for num in range(1, 10, 2):
   print (num, end=' ')