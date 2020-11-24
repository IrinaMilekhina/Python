# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, param):
        self.param = param

    def __str__(self):
        res_str = ''
        for string in self.param:
            for num in string:
                space = ' '
                space *= 4 - len(f'{num}')
                res_str += f'{num}{space}'
            res_str += f'\n'
        return res_str

    def __add__(self, other):
        new_matrix = []
        for string in range(max([len(self.param), len(other.param)])):
            str_matrix_3 = []
            for num in range(max([len(self.param[0]), len(other.param[0])])):
                try:
                    str_matrix_3.append(self.param[string][num] + other.param[string][num])
                except IndexError:
                    if len(self.param[0]) >= len(other.param[0]):
                        str_matrix_3.append(self.param[string][num])
                    else:
                        str_matrix_3.append(other.param[string][num])
            new_matrix.append(str_matrix_3)
        return Matrix(new_matrix)


matrix_1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix_2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])

print(matrix_1)
print(matrix_2)
print(matrix_3)

print(matrix_1 + matrix_2)
print(matrix_1 + matrix_2)
