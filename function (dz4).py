a = int(input("Введите длину списка "))
b = int(input("Введите максимально возможное значение списка "))


def function1():
    from random import randint
    list = [randint(a, b) for i in range(a)]
    print(list)


function1()
