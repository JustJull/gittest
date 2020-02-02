var1 = "Пока что нет!"
var2 = "Дождались!"
a = int(input("Введите значение а "))
b = int(input("Введите значение б "))
c = int(input("введите значение в "))
while a < b:
    print("Значение", a, var1)
    a = a + c
print(var2, "Финальный", a)
