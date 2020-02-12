posl = input("Введите последовательность чисел:")
list = posl.split()
print ("Полученный список: ", list)
for i in range(len(list)):
    list[i] = int(list[i])
print(list[0], list[-1])