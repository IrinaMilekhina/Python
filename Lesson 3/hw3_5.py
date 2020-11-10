# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.
users_numbers = ''
finish = False
while True:
    users_numbers = users_numbers + ' ' + input('Для выхода введите q в любой момент.\nВведите числа через пробел: ')
    temp_sum = 0
    numbers_list = users_numbers.split()
    if 'q' in numbers_list:
        numbers_list.remove('q')
        finish = True

    for i in numbers_list:
        temp_sum = temp_sum + int(i)
    print('Сумма введенных чисел:', temp_sum)

    if finish:
        print('Окей, выходим')
        break