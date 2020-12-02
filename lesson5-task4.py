# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
en_ru_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('lesson5-task4.txt', 'r', encoding='utf-8') as source_file:
    print('Прочитан файл:\n', source_file.read(), sep='')
    source_file.seek(0)
    numerals = [line.split(' — ') for line in source_file]

with open('result.txt', 'w+', encoding='utf-8') as result_file:
    el = 0
    while el < len(numerals):
        numerals[el][0] = en_ru_dict.get(numerals[el][0])
        result_file.write(' — '.join(numerals[el]))
        el += 1
    result_file.seek(0)
    print('Записан файл:\n', result_file.read(), sep='')
