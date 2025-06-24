class MovieTicket:
    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price
    
    def calculate_total(self, quantity):
        return self.price * quantity
    
    def display_ticket(self):
        print(f"\nMovie: {self.movie_name}")
        print(f"Seat: {self.seat_number}")
        print(f"Price per ticket: ${self.price:.2f}")
    
    def display_group_ticket(self, quantity):
        total = self.calculate_total(quantity)
        self.display_ticket()
        print(f"Quantity: {quantity}")
        print(f"Total cost: ${total:.2f}")


ticket1 = MovieTicket("Avengers: Endgame", "A12", 12.50)
ticket1.display_ticket()
ticket1.display_group_ticket(4)