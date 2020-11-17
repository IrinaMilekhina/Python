# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
import codecs

temp_list = []
processing_dict = {}
with codecs.open(r"Files\text_hw5_3.txt", 'r', "utf_8_sig") as f:

    for line in f:
        temp_list.append(line.split())
processing_dict = dict(temp_list)

for pare in processing_dict.items():
    if float(pare[1]) < 20000:
        print(f'У сотрудника {pare[0]} оклад менее 20 тыс: {pare[1]}')

salary_sum = 0
for salary in processing_dict.values():
    salary_sum += float(salary)
average = salary_sum / len(processing_dict)
print(f'Средний оклад сотрудников: {average}')
