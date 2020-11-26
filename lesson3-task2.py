# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def one_string(**kwargs):
    """
    Функция принимает именованные данные о пользователе и возвращает их одной строкой

    (**kwargs) -> данные о пользователе

    """
    return ' '.join(kwargs.values())


print(one_string(name='Анатолий', last_name='Вассерман', year_of_birth='1952', city='Moscow', email='Anatoly_Wasserman@yandex.ru', tel='+79991002030'))
