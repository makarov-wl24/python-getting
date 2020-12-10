# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
from random import randint


class Matrix:
    """Класс, принимающий на вход список списков,
    умеющий печатать матрицы в привычном виде и
    складывать матрицы"""

    def __init__(self, data):
        if isinstance(data, list):
            self.data = data
        else:
            print("Принимает только список списков на вход!")

    def __str__(self):
        """Переводит матрицу в строку для удобства вывода"""
        matrix_string = ""
        for row in self.data:
            for value in row:
                matrix_string += f"{value:>7}"
            matrix_string += "\n"
        return matrix_string

    def __add__(self, other):
        """Складывает две матрицы одинакового размера"""
        self.rows = len(self.data)
        self.columns = len(self.data[0])
        other.rows = len(other.data)
        other.columns = len(other.data[0])
        if self.rows == other.rows and self.columns == other.columns:
            return Matrix([[x + y for x, y in zip(el1, el2)] for el1, el2 in zip(self.data, other.data)])
        else:
            return "Можно сложить только матрицы одинаковой размерности!"


def generate_matrix(rows=3, cols=3):
    return [[randint(-100, 100) for __ in range(cols)] for _ in range(rows)]


matrix1 = Matrix(generate_matrix(2, 3))
matrix2 = Matrix(generate_matrix())
matrix3 = Matrix(generate_matrix())
matrix4 = Matrix(generate_matrix())

print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)

print(matrix1 + matrix2)
print(matrix2 + matrix3)
print(matrix2 + matrix3 + matrix4)
