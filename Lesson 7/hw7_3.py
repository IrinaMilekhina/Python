# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы
# методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение.
# Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание.
# Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
# иначе выводить соответствующее сообщение.
# Умножение.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
# Деление.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек
# этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.

class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        if type(quantity) == int:
            self.__quantity = quantity
        else:
            raise ValueError('Количество может быть только целым числом')

    def __str__(self):
        return f'Клетка из {self.quantity} ячеек'

    def __add__(self, other):
        res_quantity = self.quantity + other.quantity
        return Cell(res_quantity)

    def __sub__(self, other):
        res_quantity = self.quantity - other.quantity
        if res_quantity > 0:
            return Cell(res_quantity)
        else:
            return 'разность количества ячеек двух клеток меньше или равна нулю'

    def __mul__(self, other):
        res_quantity = self.quantity * other.quantity
        return Cell(res_quantity)

    def __truediv__(self, other):
        res_quantity = self.quantity // other.quantity
        return Cell(res_quantity)

    def make_order(self, cells_in_line):
        stars_line = '*' * self.quantity
        count = 1
        order_lines = ''
        for star in stars_line:
            if count <= cells_in_line:
                order_lines += star
            else:
                order_lines += '\n'
                count = 0
            count += 1
        return order_lines


c_1 = Cell(4)
c_2 = Cell(2)
c_3 = Cell(5)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 - c_3)
print(c_1 * c_2)
print(c_1 / c_2)
print(c_1 / c_3)

c_4 = Cell(15)
print(c_4.make_order(5))
