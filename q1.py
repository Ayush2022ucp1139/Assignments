class GroceryBill:
    def __init__(self):
        self.items = []
    
    def add_items(self):
        print("Enter items (name, price, quantity). Type 'done' when finished.")
        while True:
            entry = input("Item (name price quantity): ")
            if entry.lower() == 'done':
                break
            try:
                name, price, quantity = entry.split()
                self.items.append({
                    'name': name,
                    'price': float(price),
                    'quantity': int(quantity)
                })
            except:
                print("Invalid input. Format: name price quantity")
    
    def calc_total_bill(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total


bill = GroceryBill()
bill.add_items()
total = bill.calc_total_bill()
print(f"\nTotal bill amount: ${total:.2f}")