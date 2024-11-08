# Exercise 2



class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_driven = 0

    def set_speed(self, speed):
        # Sets the car's current speed to a specified value within limits
        self.current_speed = min(self.max_speed, speed)

    def drive(self):
        # Drive the car for one hour at the current speed
        self.distance_driven += self.current_speed

class ElectricCar(Car):
    def __init__(self, name, max_speed, battery_capacity):
        super().__init__(name, max_speed)
        self.battery_capacity = battery_capacity  # Battery capacity in kWh

class GasolineCar(Car):
    def __init__(self, name, max_speed, tank_volume):
        super().__init__(name, max_speed)
        self.tank_volume = tank_volume  # Tank volume in liters

# Main program
def main():
    # Create one electric car and one gasoline car
    electric_car = ElectricCar("ABC-15", 180, 52.5)
    gasoline_car = GasolineCar("ACD-123", 165, 32.3)

    # Set speeds for both cars
    electric_car.set_speed(150)  # Set speed to 150 km/h for electric car
    gasoline_car.set_speed(140)  # Set speed to 140 km/h for gasoline car

    # Drive both cars for 3 hours
    for _ in range(3):
        electric_car.drive()
        gasoline_car.drive()

    # Print out the distance driven by each car
    print(f"{electric_car.name}: Distance driven after 3 hours is {electric_car.distance_driven} km")
    print(f"{gasoline_car.name}: Distance driven after 3 hours is {gasoline_car.distance_driven} km")

# Run the main program
main()
