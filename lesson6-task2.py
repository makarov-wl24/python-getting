# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, width, length, weight=25, thickness=5):
        self._width = width
        self._length = length
        self.weight = weight
        self.thickness = thickness

    def asphalt_mass_calculation(self):
        return f'Необходимо асфальта: {self._width * self._length * self.weight * self.thickness / 1000} тонн.'


road = Road(20, 5000)
print(road.asphalt_mass_calculation())
