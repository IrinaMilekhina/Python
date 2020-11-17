# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import codecs

with codecs.open(r"Files\text_hw5_4.txt", 'r', "utf_8_sig") as f_eng:
    for line in f_eng:
        temp_list = [line.split()]

rus_dict = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре',
    5: 'Пять',
    6: 'Шесть',
    7: 'Семь',
    8: 'Восемь',
    9: 'Девять',
    10: 'Десять',
}

for line in temp_list:
    with open("Files\\text_hw5_4_2.txt", 'a') as f_ru:
        print(rus_dict.get(int(line[2])), '—', line[2], file=f_ru)
