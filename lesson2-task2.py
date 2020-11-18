# Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = []
list_len = int(input('Сколько элементов будем добавлять в список? '))
el_count = 1
while el_count <= list_len:
    my_list.append(input(f'Введите {el_count}-й элемент списка: '))
    el_count += 1
first_el = 0
second_el = 1
while second_el < len(my_list):
    my_list[first_el], my_list[second_el] = my_list[second_el], my_list[first_el]
    first_el += 2
    second_el += 2
print('Ваш список был изменен следующим образом: ', my_list)
