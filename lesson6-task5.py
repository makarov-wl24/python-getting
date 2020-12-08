# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью ручки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью карандаша {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки с помощью маркера {self.title}')


stationery_1 = Pen('Parker')
stationery_1.draw()
stationery_2 = Pencil('Brauberg')
stationery_2.draw()
stationery_3 = Handle('Attache')
stationery_3.draw()
