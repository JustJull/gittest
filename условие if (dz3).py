a = int(input("Введите значение а "))
b = int(input("Введите значение б "))
c = int(input("введите значение в "))
if a > b: print("Свершилось!")
elif b > a: print("Да ну!")
else:
    print("А если так?")
    a = a + c
    b = b - c
    if a > b: print("Свершилось!")
    elif b > a: print("Да ну!")

