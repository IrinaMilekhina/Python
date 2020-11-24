# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def tissue_expense(self):
        pass


class Clothes(MyAbstractClass):
    def __init__(self, name, param):
        self.name = name
        self.__t = ''
        self.param = param
        self.all_expense = 0

    @property
    def tissue_expense(self):
        if self.__t == 'coat':
            current_expense = self.param / 6.5 + 0.5
            self.all_expense += current_expense
            return f'Расход на пальто: {round(current_expense, 2)}\nОбщий расход: {round(self.all_expense, 2)}'
        elif self.__t == 'suit':
            current_expense = 2 * self.param + 0.3
            self.all_expense += current_expense
            return f'Расход на костюм: {round(current_expense, 2)}\nОбщий расход: {round(self.all_expense, 2)}'

    @tissue_expense.setter
    def tissue_expense(self, t):
        if t != 'coat' and t != 'suit':
            raise ValueError('расчет только для пальто или костюма (тип coat или suit)')
        else:
            self.__t = t


b = Clothes('m', 6.5)
b.tissue_expense = 'coat'
print(b.tissue_expense)
b.tissue_expense = 'suit'
print(b.tissue_expense)
b.param = 1
b.tissue_expense = 'coat'
print(b.tissue_expense)
b.tissue_expense = 'else'
print(b.tissue_expense)
