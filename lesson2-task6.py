# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

product_counter = 0
product_quantity = int(input('Сколько товаров желаете добавить? '))

products = []
while product_counter < product_quantity:
    product = dict()
    product['название'] = input('Введине название товара: ')
    product['цена'] = input('Введине цену товара: ')
    product['количество'] = input('Введине количество товара: ')
    product['ед'] = input('Введине единицу измерения товара: ')
    products.append((product_counter + 1, product))
    product_counter += 1

print('Ваши товары оргинизованны следующим образом: ')
print(products)

analytic = {}
products_name = []
for i in range(len(products)):
    products_name.append(products[i][1]['название'])
analytic['название'] = products_name

products_price = []
for i in range(len(products)):
    products_price.append(products[i][1]['цена'])
analytic['цена'] = products_price

products_count = []
for i in range(len(products)):
    products_count.append(products[i][1]['количество'])
analytic['количество'] = products_count

products_unit = set()
for i in range(len(products)):
    products_unit.add(products[i][1]['ед'])
analytic['ед'] = list(products_unit)
print('Ваша аналитика готова: ')
print(analytic)
