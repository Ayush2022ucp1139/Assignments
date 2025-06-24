class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.brand} {self.model} ({self.year})"
    
class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        return f"Car: {super().display_info()}, Doors: {self.num_doors}"


class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type  # e.g., "Mountain", "Road", "Electric"

    def display_info(self):
        return f"Bike: {super().display_info()}, Type: {self.bike_type}"


class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load):
        super().__init__(brand, model, year)
        self.max_load = max_load  # in kg

    def display_info(self):
        return f"Truck: {super().display_info()}, Max Load: {self.max_load}kg"    
    
car = Car("Toyota", "Camry", 2022, 4)
bike = Bike("Trek", "FX 3", 2023, "Hybrid")
truck = Truck("Ford", "F-150", 2021, 2000)

print(car.display_info())    
print(bike.display_info())   
print(truck.display_info())    