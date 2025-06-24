class Car:
    def __init__(self, brand, model, daily_rent):
        self.brand = brand
        self.model = model
        self.daily_rent = daily_rent

    def calculate_rent(self, days):
        if days > 0:
            return days * self.daily_rent
        return 0
    

car1 = Car("Toyota", "Camry", 50)
car2 = Car("Honda", "Civic", 40)
    
print("Available Cars:")
print(car1)
print(car2)
    
print("\nRenting car1 for 5 days:")
total_rent_1 = car1.calculate_rent(5)
print(f"Total rent: ${total_rent_1}")

print("\nRenting car2 for 10 days:")
total_rent_2 = car1.calculate_rent(10)
print(f"Total rent: ${total_rent_2}")



