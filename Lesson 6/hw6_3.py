# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии: {self._income.get("wage") + self._income.get("bonus")}')


p_1 = Position('Иван', 'Иванов', 'админ', 5000, 2000)
p_2 = Position('Петр', 'Петров', 'младший админ', 4500, 1000)
p_3 = Position('Сидр', 'Сидоров', 'старший админ', 15000, 10000)

p_1.get_full_name()
p_2.get_total_income()
p_3.get_full_name()
p_3.get_total_income()
