a = int(input("Введите длину списка "))
b = int(input("Введите максимально возможное значение списка "))


def function1():
    from random import randint
    list = [randint(a, b) for i in range(a)]
    if b > 7:
        list = [i for i in list if i > 7]
        print("Значения больше 7: ", list)
    else: print("Спробуй ще!")


function1()
