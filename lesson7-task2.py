# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property
from abc import abstractmethod


class Clothes:
    """ Рассчет ткани для пошива"""
    def __init__(self, prod_name, size=0.0, height=0.0, num=1):
        self.prod_name = prod_name
        self.size = size
        self.height = height
        self.number = num

    @abstractmethod
    def textile(self):
        global sum_textile
        if str.lower(self.prod_name) == 'пальто':
            num_textile = (self.size/6.5 + 0.5) * self.number
        elif str. lower(self.prod_name) == 'костюм':
            num_textile = (self.height * 2 + 0.3) * self.number
        else:
            return f'Не умею считать расход ткани на "{self.prod_name}"'
        if isinstance(num_textile, (float, int)):
            sum_textile += num_textile
        return f'{self.prod_name}: {round(num_textile, 1)}'

    @property
    def about(self):
        return f"Программа для расчета ткани"


sum_textile = 0
txl1 = Clothes("Пальто", size=45, num=5)
txl2 = Clothes("Костюм", height=1.8)
txl3 = Clothes("Сюртук", 42)

print(txl1.textile())
print(txl2.textile())
print(txl3.textile())
print(f'Всего потребуется ткани: {round(sum_textile, 1)}')
print(txl1.about)
