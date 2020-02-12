my_dict = {'a':645, 'b':3987, 'c': 93,'d': 111, 'e': 646, 'f': 20}
print("Наш словарь - ", my_dict)
max_keys = sorted(my_dict, key = my_dict.get, reverse = True)

print('Наибольшое значение в ключе: ', max_keys[0])
print('2-е наибольшое значение в ключе: ', max_keys[1])
print('3-е наибольшое значение в ключе: ', max_keys[2])