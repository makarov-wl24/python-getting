# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), они должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Появилась {"полицейская" if is_police else ""} {self.name} (цвет {self.color}), скорость: {self.speed}')

    def go(self):
        print(f'{self.name} начала следовать по маршруту')

    def stop(self):
        print(f'{self.name} добралась до пункта назначения')

    def turn(self, direction):
        print(f'{self.name} повернула {"налево" if direction == 0 else "налево"}')

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed} км/ч'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name} превышет' if self.speed > 60 else f'{self.name} двигается с разрешенной скоростью'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        return f'{self.name} превышет' if self.speed > 40 else f'{self.name} двигается с разрешенной скоростью'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def go(self):
        print(f'{self.name} выехала на дежурство')

    def stop(self):
        print(f'{self.name} закончила дежурство')

    def turn(self, direction):
        print(f'{self.name} {"начала" if direction == 0 else "закончила"} преследование')


car_1 = TownCar(60, 'белый', 'Renault')
car_1.go()

car_2 = WorkCar(60, 'серый', 'MAN')
car_2.go()

car_3 = SportCar(200, 'серый', 'Lamborghini')
car_3.go()

car_4 = PoliceCar(60, 'серый', 'BMW')
car_4.go()

print(car_1.show_speed())
print(car_2.show_speed())
print(car_3.show_speed())
print(car_4.show_speed())

car_1.turn(0)
car_1.turn(1)
car_2.turn(0)
car_2.turn(1)
car_3.turn(0)
car_3.turn(1)
car_4.turn(0)
car_4.turn(1)

car_1.stop()
car_2.stop()
car_3.stop()
car_4.stop()
