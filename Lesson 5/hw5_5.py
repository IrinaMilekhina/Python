# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open(r"Files\text_hw5_5.txt", 'w') as f:
    while True:
        user_input = input("Для окончания нажмите enter.\nВведите число для добавления в файл: ")
        if user_input == '':
            break
        else:
            f.write(user_input + ' ')

with open(r"Files\text_hw5_5.txt", 'r') as f:
    content = f.read()
    res_list = [int(item) for item in content.split()]
    print('Сумма добавленных чисел: ', sum(res_list))
