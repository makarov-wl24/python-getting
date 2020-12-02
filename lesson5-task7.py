# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.
import json

result = [{}, {}]
gross_profit = 0
profit_firms = 0

with open('lesson5-task7.txt', 'r', encoding='utf-8') as file:
    print('Прочитан файл:\n', file.read(), sep='')
    file.seek(0)
    for line in file:
        firm = line.split()
        profit = float(firm[2]) - float(firm[3])
        result[0][firm[0]] = profit
        if profit > 0:
            gross_profit += profit
            profit_firms += 1
result[1]['average_profit'] = gross_profit / profit_firms
print(f'Создан список: {result}')

with open('text.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file)
