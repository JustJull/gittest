from random import randint

lst = []
for i in range(10):
    lst.append(randint(0, 100))
del lst[-1]
