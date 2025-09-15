print("\nRandom numbers")
import random
print(random.random())
rnd = random.random
for i in range(5):
    print(rnd())
print("\nRandom numbers")
rndi = random.randint
for i in range(5):
    print(rndi(0,100))
for i in range(5):
    print(int(rnd()*100))
    
mu = 50
s = 10
for i in range(10):
    print(random.gauss(mu, s))
    print(int(random.gauss(mu, s)))