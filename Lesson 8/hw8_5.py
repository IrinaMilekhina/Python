# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

class OfficeEquipmentWarehouse:
    equipment_count = 0
    all_in_warehouses = {}

    def __init__(self, name, city, square):
        self.name = name
        self.city = city
        self.square = square

    def acceptanse(self, obj):

        OfficeEquipmentWarehouse.equipment_count += 1
        obj.in_warehouse = True
        temp_list = []
        test = OfficeEquipmentWarehouse.all_in_warehouses.get(self.name)
        if test is None:
            OfficeEquipmentWarehouse.all_in_warehouses.update({self.name: obj.name})
        else:
            temp_list.append(test)
            temp_list.append(obj.name)

            OfficeEquipmentWarehouse.all_in_warehouses.update({self.name: temp_list})
            print(OfficeEquipmentWarehouse.all_in_warehouses)


class OfficeEquipment:
    def __init__(self, name, id, in_warehouse, functions='none'):
        self.name = name
        self.id = id
        self.functions = functions
        self.in_warehouse = bool(in_warehouse)


class Printer(OfficeEquipment):
    def __init__(self, name, id, printer_type, functions='printer', in_warehouse=False):
        super().__init__(name, id, in_warehouse)
        self.printer_type = printer_type
        self.type = functions


class Scanner(OfficeEquipment):
    def __init__(self, name, id, quality, in_warehouse=False, functions='scanner'):
        super().__init__(name, id, in_warehouse)
        self.quality = quality
        self.type = functions


class Xerox(OfficeEquipment):
    def __init__(self, name, id, speed, in_warehouse=False, functions='xerox'):
        super().__init__(name, id, in_warehouse)
        self.quality = speed
        self.type = functions


xerox_1 = Xerox(name='ксерокс модный', id=11, speed=500)
print(xerox_1.in_warehouse)
printer_1 = Printer(name='принтер желтый', id=12, printer_type='черно-белый')
wh_1 = OfficeEquipmentWarehouse('склад 1', 'Москва', 100)

OfficeEquipmentWarehouse.acceptanse(wh_1, xerox_1)
print(wh_1.equipment_count)
print(wh_1.all_in_warehouses)
print(xerox_1.in_warehouse)
OfficeEquipmentWarehouse.acceptanse(wh_1, printer_1)

wh_2 = OfficeEquipmentWarehouse('склад 2 маленький', 'Москва', 10)
scanner_1 = Scanner(name='сканер портативный', id=101, quality='high')
OfficeEquipmentWarehouse.acceptanse(wh_2, scanner_1)
print(wh_1.equipment_count)
print(wh_1.all_in_warehouses)
