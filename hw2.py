# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_sec = int(input('Введите время в секундах: '))
hour = str(user_sec // 3600)
minute = str((user_sec -(user_sec // 3600 * 3600)) // 60)
second = str((user_sec -(user_sec // 3600 * 3600))  % 60)

#я еще не усею писать функции, но дальше я бы я ее применила

if len(hour) == 1:
    hour = '0' + hour

if len(minute) == 1:
    minute = '0' + minute

if len(second) == 1:
    second = '0' + second

print(f'{hour}:{minute}:{second}')
