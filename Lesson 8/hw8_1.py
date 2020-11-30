# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import time


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def numbering(cls, user_date):
        day, month, year = map(int, user_date.split('-'))
        numbered_date = cls(day, month, year)
        return numbered_date

    @staticmethod
    def date_valid(user_date):

        try:
            time.strptime(user_date, '%d-%m-%Y')
        except ValueError:
            print('Некорректная дата!')

        return user_date


print(Date.numbering('02-12-2021'))
print(Date.date_valid('02-22-2021'))
