class Car:
    className = 'Car'
    objectsCount = 0

    def __init__(self, tank_capacity, fuel_consumption, average_speed):
        self._tank_capacity = tank_capacity
        self._fuel_consumption = fuel_consumption
        self._average_speed = average_speed
        Car.objectsCount = Car.objectsCount + 1

    def get_tank_capacity(self):
        return self._tank_capacity

    def set_tank_capacity(self, capacity):
        if capacity > 0:
            self._tank_capacity = capacity
        else:
            self._tank_capacity = 0.1

    def get_fuel_consumption(self):
        return self._fuel_consumption

    def set_fuel_consumption(self, consumption):
        if consumption > 0:
            self._fuel_consumption = consumption
        else:
            self._fuel_consumption = 0.1

    def get_average_speed(self):
        return self._average_speed

    def set_average_speed(self, speed):
        if speed > 0:
            self._average_speed = speed
        else:
            self._average_speed = 1

    def info(self):
        print(f"Ёмкость бака: {self._tank_capacity} л")
        print(f"Расход топлива: {self._fuel_consumption} л/100км")
        print(f'Средняя скорость: {self._average_speed} км/ч')

    def distance_to_empty(self):
        distance = (self._tank_capacity / self._fuel_consumption) * 100
        print(f'Пройденное расстояние до полного опустошения бака: {distance:.2f} км')
        return distance


class Truck(Car):
    className = 'Truck'

    def __init__(self, tank_capacity, fuel_consumption, average_speed, cargo_weight):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.cargo_weight = cargo_weight

    def set_cargo_weight(self, weight):
        if weight > 0:
            self.cargo_weight = weight
        else:
            self.cargo_weight = 1

    def info(self):
        super().info()
        print(f'Тип: {Truck.className}')
        print(f"Вес груза: {self.cargo_weight} кг")

    def fuel_ratio(self):
        fuel_for_250km = (self._fuel_consumption / 100) * 250
        ratio = self.cargo_weight / fuel_for_250km
        print(f'Соотношение веса груза к количеству топлива на 250 км: {ratio:.2f} кг/л')
        return ratio


class Bus(Car):
    className = 'Bus'

    def __init__(self, tank_capacity, fuel_consumption, average_speed, passenger_count):
        super().__init__(tank_capacity, fuel_consumption, average_speed)
        self.passenger_count = passenger_count

    def set_passenger_count(self, count):
        if count > 0:
            self.passenger_count = count
        else:
            self.passenger_count = 1

    def info(self):
        super().info()
        print(f'Тип: {Bus.className}')
        print(f"Количество пассажиров: {self.passenger_count}")

    def fuel_ratio(self):
        fuel_for_250km = (self._fuel_consumption / 100) * 250
        ratio = self.passenger_count / fuel_for_250km
        print(f'Соотношение числа пассажиров к количеству топлива на 250 км: {ratio:.2f} пасс/л')
        return ratio


car = Car("Объект класса " + Car.className, 60, 8, 90)
car.info()
car.distance_to_empty()

print('\n')

truck = Truck(200, 25, 80, 5000)
bus = Bus(120, 18, 70, 40)

truck.info()
truck.fuel_ratio()

print('\n')

bus.info()
bus.fuel_ratio()

print(f'Objects count: {Car.objectsCount}')
