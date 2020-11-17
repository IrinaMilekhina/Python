# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re
import codecs

with codecs.open(r"Files\text_hw5_6.txt", 'r', "utf_8_sig") as f:
    count_lines = len(f.readlines())
    f.seek(0)
    i = 0
    res_dict = {}
    while i < count_lines:
        content = f.readline()
        key = ''
        for letter in content:
            if letter == ':':
                break
            else:
                key += letter

        value = sum([int(item) for item in re.findall('(\d+)', content)])

        res_dict.update({key: value})
        i += 1
print(res_dict)
