class RestaurantOrder:
    def __init__(self):
        self.items = []
    
    def add_item(self, food_item, price):
        self.items.append({"item": food_item, "price": price})
    
    def calculate_bill(self):
        total = sum(item["price"] for item in self.items)
        return {
            "total_items": len(self.items),
            "total_amount": total,
            "items": self.items
        }
    
    def print_receipt(self):
        bill = self.calculate_bill()
        print("\n=== RESTAURANT RECEIPT ===")
        for item in self.items:
            print(f"{item['item']:20} ${item['price']:.2f}")
        print("-" * 30)
        print(f"TOTAL ITEMS: {bill['total_items']}")
        print(f"TOTAL AMOUNT: ${bill['total_amount']:.2f}")
        print("=========================")


order = RestaurantOrder()
order.add_item("Burger", 8.99)
order.add_item("Fries", 3.50)
order.add_item("Soda", 2.50)
order.add_item("Ice Cream", 4.75)
    
bill = order.calculate_bill()
print(f"Total items ordered: {bill['total_items']}")
print(f"Total bill amount: ${bill['total_amount']:.2f}")
    
order.print_receipt()