# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')

try:
    dividend = int(dividend)
    divider = int(divider)
    if divider == 0:
        raise MyZeroDivision("Вообще-то так нельзя, но для тебя будет 0.")
except ValueError:
    print("Вы ввели не число")
except MyZeroDivision as err:
    print(err)
else:
    print(f"{dividend / divider}")
