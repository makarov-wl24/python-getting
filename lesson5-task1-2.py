# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('text.txt', 'w+', encoding='utf-8') as file:
    line = None
    while line != '':
        line = (input('Введите строку для записи в файл (для завершения введите пустую строку): '))
        file.write(f'{line}\n')
    file.seek(0)
    lines_count = 0
    for line in file:
        if line != '\n':
            lines_count += 1
            words_count = len(line.split())
            print(f'Строка {lines_count} (слов: {words_count}): {line}', end='')
