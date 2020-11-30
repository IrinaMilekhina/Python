# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class OfficeEquipmentWarehouse:
    def __init__(self, name, city, square):
        self.name = name
        self.city = city
        self.square = square


class OfficeEquipment:
    def __init__(self, name, id, functions='none'):
        self.name = name
        self.id = id
        self.type = functions


class Printer(OfficeEquipment):
    def __init__(self, name, id, printer_type, functions='printer'):
        super().__init__(name, id)
        self.printer_type = printer_type
        self.type = functions


class Scanner(OfficeEquipment):
    def __init__(self, name, id, quality, functions='scanner'):
        super().__init__(name, id)
        self.quality = quality
        self.type = functions


class Xerox(OfficeEquipment):
    def __init__(self, name, id, speed, functions='xerox'):
        super().__init__(name, id)
        self.quality = speed
        self.type = functions


xerox_1 = Xerox('name', 11, 'high')
o = OfficeEquipment('f', 1)
