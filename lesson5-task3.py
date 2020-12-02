# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('lesson5-task3.txt', 'r+', encoding='utf-8') as file:
    line = None
    while line != '':
        line = (input('Введите фамилию сотрудника и зарплату через пробел (для завершения введите пустую строку): '))
        file.write(f'{line}\n')
    file.seek(0)
    workers = [line.split() for line in file if line != '\n']
print('Вы ввели следующие данные:', workers)
try:
    salaries = list(map(lambda el: float(el[1]), workers))
except IndexError:
    print('Необходимо вводить фамилию сотрудника и его зарплату через пробел')
except ValueError:
    print('Зарплата должна представлять число')
else:
    print('Средняя зарплата сотрудников:', round(sum(salaries) / len(salaries), 2))
    low_salary_workers = [workers[el][0] for el in range(len(salaries)) if salaries[el] < 20000]
    print('Сотрудники с ЗП < 20 000:', low_salary_workers)
