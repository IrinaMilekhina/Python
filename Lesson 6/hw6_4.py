# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.is_police is True:
            print(f'{self.color} полицейская машина {self.name} поехала')
        else:
            print(f'{self.color} машина {self.name} поехала')

    def stop(self):
        if self.is_police is True:
            print(f'{self.color} полицейская машина {self.name} остановилась')
        else:
            print(f'{self.color} машина {self.name} остановилась')

    def turn_direction(self, direction):
        self.direction = direction
        print(f'Машина {self.name} повернула {self.direction} ')

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, town_type, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        self.town_type = town_type

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')
        if self.speed > 60:
            print('ПРЕВЫШЕНИЕ!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')
        if self.speed > 40:
            print('ПРЕВЫШЕНИЕ!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


car_1 = SportCar(60, 'красная', 'mazda')
car_2 = TownCar('горный', 160, 'черная', 'skoda')
car_3 = WorkCar(100, 'белая', 'ford')
car_4 = PoliceCar(100, 'голубая', 'ford')

car_1.go()
car_1.turn_direction('направо')
car_1.show_speed()
car_1.stop()

car_2.go()
car_2.turn_direction('налево')
car_2.show_speed()
car_2.stop()

car_3.go()
car_3.turn_direction('налево')
car_3.show_speed()
car_3.stop()

car_4.go()
car_4.turn_direction('в обратном направлении')
car_4.show_speed()
car_4.stop()
