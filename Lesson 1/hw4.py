# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите число: '))
total = number % 10
number = number // 10

while number > 0:
    last = number % 10
    if last > total:
        total = last
    number = number // 10
print(total)
