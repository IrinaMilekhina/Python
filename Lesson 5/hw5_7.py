# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
import codecs

firm_profit_dict = {}
average_profit_dict = {}
average_profit = 0

with codecs.open(r"Files\text_hw5_7.txt", 'r', "utf_8_sig") as f:
    content = f.read().splitlines()
    firms_quantity = len(content)
for firm in content:
    profit = int(firm.split()[2]) - int(firm.split()[3])
    firm_profit_dict.update({firm.split()[0]: profit})
    if profit > 0:
        average_profit += profit

    average_profit_dict.update({'average_profit': average_profit / firms_quantity})
res_list = [firm_profit_dict, average_profit_dict]
print(res_list)

with open(r"Files\json_hw5_7.json", "w") as write_f:
    json.dump(res_list, write_f)
