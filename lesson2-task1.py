# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [1, 2.3, False, None, 'строка', 0x11, 5+6j, [1, 2], (3, 2), {'a', 'b'}, {'key_1': 'val_1', 'key_2': 'val_2'}]
for i in my_list:
    print(type(i))
