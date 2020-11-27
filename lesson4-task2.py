# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123]
from random import randint

raw_list = [randint(1, 300) for el in range(randint(10, 20))]
print('Сгенерирован исходный список:', raw_list)
print('Результат работы:', [raw_list[ind] for ind in range(1, len(raw_list)) if raw_list[ind] > raw_list[ind - 1]])