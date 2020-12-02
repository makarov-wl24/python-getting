# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint

with open('text.txt', 'w+', encoding='utf-8') as file:
    file.write(' '.join(map(str, [randint(0, 100) for el in range(randint(10, 20))])))
    file.seek(0)
    print('Записан файл:', file.read(), sep='\n')
    file.seek(0)
    print('Сумма всех чисел в файле:', sum(map(int, file.read().split())))
