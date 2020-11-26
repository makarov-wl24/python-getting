# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
num_list = []


def num_sum(raw_string, result=0):
    """
    Функция подсчитывает сумму чисел в строке, разделенных пробелом, после ввода q подсчет завершается.
    При передаче аргумента result сумму чисел добавляет к нему.

    num_sum('1 2 3', 5)
    11

    """
    global num_list
    num_list = raw_string.split()
    for num in num_list:
        if num == 'q':
            break
        result += int(num)
    print(f'Результат сложения чисел {result}')
    return result

last_sum = 0
while 'q' not in num_list:
    last_sum = num_sum(input('Введите строку чисел, разделенных пробелом (когда закончите, введите q): '), last_sum)

print('Работа программы завершена')