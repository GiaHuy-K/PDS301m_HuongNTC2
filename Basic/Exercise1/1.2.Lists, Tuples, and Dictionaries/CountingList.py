# .count(x) returns a count of the value x specified.
from random import random as rnd
mylist = []
for i in range(20):
 mylist.append(int(rnd()*10))
print(mylist)
for i in range(10):
 print("frequency of {}: {}".format(i, mylist.count(i)))
