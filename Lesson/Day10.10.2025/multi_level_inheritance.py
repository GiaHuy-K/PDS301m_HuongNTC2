class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def display_info(self):
        print(f"Max Speed: {self.max_speed}, Mileage: {self.mileage}")
        
class Car(Vehicle):
    def __init__(self, max_speed, mileage, brand):
        super().__init__(max_speed, mileage)
        self.brand = brand

    def display_info(self):
        base_info = super().display_info()
        print(f"Brand: {self.brand}")
        
class SportsCar(Car):
    def __init__(self, max_speed, mileage, brand, turbo):
        super().__init__(max_speed, mileage, brand)
        self.turbo = turbo

    def display_info(self):
        super().display_info()
        print(f"Turbo: {self.turbo}")
        
sports_car = SportsCar(300, 15, "Ferrari", True)
sports_car.display_info()
