# .sort sorts a list. If we have a random list
from random import random as rnd
myList =[]
for i in range(20):
    myList.append(int(rnd()*100))
print(myList)
myList.sort()
print(myList)