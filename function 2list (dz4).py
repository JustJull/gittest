a = int(input("Введите длину списка 1 "))
b = int(input("Введите максимально возможное значение списка 1 "))
c = int(input("Введите длину списка 2 "))
d = int(input("Введите максимально возможное значение списка 2 "))

from random import randint
list1 = [randint(a, b) for i in range(a)]
list2 = [randint(c, d) for i in range(c)]

def lists():
    a_set = set(list1)
    b_set = set(list2)
    if a_set & b_set:
        print("Совпадающие числа списка 1 и списка 2: ", a_set & b_set)
    else:
        print("Спробуй ще!")

lists()