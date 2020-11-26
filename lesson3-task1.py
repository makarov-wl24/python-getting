# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(dividend, divider):
    """
    Принимает два числа и выполняет их деление.

    (dividend, divider) —> делимое, делитель
    division(10, 2)
    5

    """
    try:
        return float(dividend) / float(divider)
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    except ValueError:
        return 'Необходимо передавать числа!'


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')
print(division(dividend, divider))
