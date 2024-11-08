# Exercise 2

class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_driven = 0

    def set_speed(self, speed):
        self.current_speed = min(self.max_speed, speed)

    def drive(self):
        self.distance_driven += self.current_speed

class ElectricCar(Car):
    def __init__(self, name, max_speed, battery_capacity):
        super().__init__(name, max_speed)
        self.battery_capacity = battery_capacity

class GasolineCar(Car):
    def __init__(self, name, max_speed, tank_volume):
        super().__init__(name, max_speed)
        self.tank_volume = tank_volume

def main():
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    electric_car.set_speed(150)
    gasoline_car.set_speed(140)

    for _ in range(3):
        electric_car.drive()
        gasoline_car.drive()

    print(f"{electric_car.name}: Distance driven after 3 hours is {electric_car.distance_driven} km")
    print(f"{gasoline_car.name}: Distance driven after 3 hours is {gasoline_car.distance_driven} km")

main()
