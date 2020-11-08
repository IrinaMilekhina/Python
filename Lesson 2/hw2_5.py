# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]

while True:
    new_el = input('Для выхода введите q или введите новый элемент рейтинга: ')
    if new_el == 'q':
        break
    elif int(new_el) in my_list:
        my_list.reverse()
        my_list.insert(my_list.index(int(new_el)), int(new_el))
        my_list.reverse()
        print(my_list)
        continue
    else:
        my_list.reverse()
        if min(my_list) >= int(new_el):
            my_list.reverse()
            my_list.append(int(new_el))
            print(my_list)
            continue
        elif max(my_list) <= int(new_el):
            my_list.append(int(new_el))
            my_list.reverse()
            print(my_list)
            continue
        else:
            for ind, el in enumerate(my_list):
                if el >= int(new_el):
                    my_list.insert(ind, int(new_el))
                    my_list.reverse()
                    print(my_list)
                    break
                else:
                    break
