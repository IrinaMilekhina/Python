# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class ContainsNumOnly(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipmentWarehouse:
    warehouses_equipment_count = 0
    all_in_warehouses = {}

    def __init__(self, name, city, square):
        self.name = name
        self.city = city
        self.square = square
        self.warehouse_equipment_count = 0
        self.amount = 0

    @staticmethod
    def warehouses_status():
        print(f'Всего на складах {OfficeEquipmentWarehouse.warehouses_equipment_count} шт')
        print(f'Полный состав на складах: {OfficeEquipmentWarehouse.all_in_warehouses}')

    def warehouse_status(self):
        print(f'Всего на складe "{self.name}" {self.warehouse_equipment_count} шт')
        print(f'Полный состав на складе "{self.name}": {OfficeEquipmentWarehouse.all_in_warehouses.get(self.name)}')

    def acceptanse(self, obj, amount):
        try:
            self.amount = int(amount)
            if amount <= 0:
                raise ContainsNumOnly(f'Количество "{obj.name}" должно быть целым положительным числом (и не ноль)')
        except ValueError:
            print(f'Вы ввели не число для количества объекта "{obj.name}"')
        except ContainsNumOnly as err:
            print(err)
        else:
            OfficeEquipmentWarehouse.warehouses_equipment_count += amount
            self.warehouse_equipment_count += amount
            obj.in_warehouse = True
            temp_list = []
            test = OfficeEquipmentWarehouse.all_in_warehouses.get(self.name)
            if test is None:
                OfficeEquipmentWarehouse.all_in_warehouses.update({self.name: obj.name})
            else:
                temp_list.append(test)
                temp_list.append(obj.name)

                OfficeEquipmentWarehouse.all_in_warehouses.update({self.name: temp_list})


class OfficeEquipment:
    def __init__(self, name, in_warehouse, functions='none'):
        self.name = name
        self.functions = functions
        self.in_warehouse = bool(in_warehouse)

    def acceptanse_status(self):
        print(f'Статус оприходования на складе объекта "{self.name}": {self.in_warehouse}')


class Printer(OfficeEquipment):
    def __init__(self, name, printer_type, functions='printer', in_warehouse=False):
        super().__init__(name, in_warehouse)
        self.printer_type = printer_type
        self.type = functions


class Scanner(OfficeEquipment):
    def __init__(self, name, quality, in_warehouse=False, functions='scanner'):
        super().__init__(name, in_warehouse)
        self.quality = quality
        self.type = functions


class Xerox(OfficeEquipment):
    def __init__(self, name, speed, in_warehouse=False, functions='xerox'):
        super().__init__(name, in_warehouse)
        self.quality = speed
        self.type = functions


# создаем тестовые объекты
xerox_1 = Xerox(name='ксерокс модный', speed=500)
printer_1 = Printer(name='принтер желтый', printer_type='черно-белый')
wh_1 = OfficeEquipmentWarehouse('склад 1', 'Москва', 100)
wh_2 = OfficeEquipmentWarehouse('склад 2 маленький', 'Москва', 10)
scanner_1 = Scanner(name='сканер портативный', quality='high')
# проверяем статус оприходования
OfficeEquipment.acceptanse_status(xerox_1)
# выполняем оприходование
OfficeEquipmentWarehouse.acceptanse(wh_1, xerox_1, 2)
# повторно проверяем статус
OfficeEquipment.acceptanse_status(xerox_1)
# пробуем оприходовать с количеством 0
OfficeEquipmentWarehouse.acceptanse(wh_1, printer_1, 0)
# пробуем оприходовать со строкой вместо количества
OfficeEquipmentWarehouse.acceptanse(wh_2, scanner_1, '4v')
# проверяем что добавилось на склад
OfficeEquipmentWarehouse.warehouse_status(wh_1)
# добавляем второй объект и проверяем статус
OfficeEquipmentWarehouse.acceptanse(wh_1, printer_1, 10)
OfficeEquipmentWarehouse.warehouse_status(wh_1)
# добавляем объект на другой склад и проверяем все статусы
OfficeEquipmentWarehouse.acceptanse(wh_2, scanner_1, 4)
OfficeEquipmentWarehouse.warehouses_status()
OfficeEquipmentWarehouse.warehouse_status(wh_2)
OfficeEquipmentWarehouse.warehouse_status(wh_1)
