# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
import codecs

lines = 0
words = 0
ind = 1
pos = 'out'

with codecs.open(r"Files\text_hw5_2.txt", 'r', "utf_8_sig") as f:
    for line in f:
        lines += 1

        for letter in line:
            if letter == '-' or letter == '\r' or letter == '\n':
                continue
            elif letter != ' ' and pos == 'out':
                words += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'
        print('Строка', ind, 'слов:', words)
        ind += 1
        words = 0
print("Всего строк:", lines)
