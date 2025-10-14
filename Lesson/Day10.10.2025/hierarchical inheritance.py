# sportcar, truck , electriccar kế thừa từ class car
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class SportCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

    def display_info(self):
        base_info = super().display_info()
        print(f"Top Speed: {self.top_speed} km/h")

class Truck(Car):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    def display_info(self):
        base_info = super().display_info()
        print(f"Load Capacity: {self.load_capacity} tons")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_range):
        super().__init__(brand, model)
        self.battery_range = battery_range

    def display_info(self):
        base_info = super().display_info()
        print(f"Battery Range: {self.battery_range} km")
        
sport_car = SportCar("Porsche", "911", 320)
truck = Truck("Volvo", "FH16", 25)
electric_car = ElectricCar("Tesla", "Model S", 600)