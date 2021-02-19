from time import sleep


class TrafficLight:
    __color: str

    def running(self):
        while True:
            self.__color = 'красный'
            print(self.__color)
            sleep(7)
            self.__color = 'желтый'
            print(self.__color)
            sleep(2)
            self.__color = 'зеленый'
            print(self.__color)
            sleep(5)


trafficLight = TrafficLight()
# trafficLight.running()


class Road:
    __length: int
    __width: int

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_masses(self, mass_for_1_sm, height):
        return str(self.__length * self.__width * mass_for_1_sm * height / 1000) + ' тонн'


road = Road(20, 5000)
print(road.calculate_masses(25, 5))


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


position = Position('Kate', 'Evdochenko', 'разработчик', 1000, 10)
print(position.get_full_name())
print(position.get_total_income())


class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(self.speed)

    def go(self):
        print(self.name + ' поехала')

    def stop(self):
        print(self.name + ' остановилась')

    def turn(self, direction: str):
        print(self.name +' повернула на ' + direction)


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        if self.speed > 40: print('Скорость превышена')
        print(self.speed)


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, False)

    def show_speed(self):
        if self.speed > 60: print('Скорость превышена')
        print(self.speed)


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, True)


workCar = WorkCar(70, 'red', 'work car')
policeCar = PoliceCar(100, 'red', 'police car')
sportCar = SportCar(220, 'red', 'sport car')
townCar = TownCar(61, 'red', 'town car')

policeCar.go()
policeCar.stop()
policeCar.turn('право')
workCar.show_speed()
townCar.show_speed()


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'ручка')

    def draw(selfs):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'карандаш')

    def draw(selfs):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def __init__(self):
        Stationery.__init__(self, 'маркер')

    def draw(selfs):
        print('Отрисовка маркером')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
