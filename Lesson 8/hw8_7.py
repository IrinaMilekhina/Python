#  Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
#  методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
#  (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
#  Проверьте корректность полученного результата.

class ComplexNumbers:
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def __str__(self):
        complex_num_format = f'{self.arg_1}+{self.arg_2}*i'
        return complex_num_format

    def __add__(self, other):
        new_arg_x = self.arg_1 + other.arg_1
        new_arg_y = self.arg_2 + other.arg_2
        return ComplexNumbers(new_arg_x, new_arg_y)

    def __mul__(self, other):
        new_arg_x = self.arg_1 * other.arg_1 - self.arg_2 * other.arg_2
        new_arg_y = self.arg_2 * other.arg_1 + self.arg_1 * other.arg_2
        return ComplexNumbers(new_arg_x, new_arg_y)


num_1 = ComplexNumbers(5, 1)
num_2 = ComplexNumbers(5, 1)

print(num_1)
print(num_1 + num_2)
print(num_1 * num_2)
