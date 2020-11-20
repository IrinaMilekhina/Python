# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, lenght, width):
        self._width = width
        self._lenght = lenght

    def calculation(self):
        res = self._lenght * self._width * 25 * 5
        if res >= 1000:
            print(f'{res / 1000} т')
        if res < 1000:
            print(f'{res} кг')


r_1 = Road(20, 5000)
r_1.calculation()
