class Payment:
    def make_payment(self, amount):
        pass 


class CreditCardPayment(Payment):
    def make_payment(self, amount):
        return f"Processing Credit Card Payment of ₹{amount}"


class DebitCardPayment(Payment):
    def make_payment(self, amount):
        return f"Processing Debit Card Payment of ₹{amount}"


class UPIPayment(Payment):
    def make_payment(self, amount):
        return f"Processing UPI Payment of ₹{amount}"


def process_payment(payment_method, amount):
    print(payment_method.make_payment(amount))


credit_card = CreditCardPayment()
debit_card = DebitCardPayment()
upi = UPIPayment()

process_payment(credit_card, 1000)  
process_payment(debit_card, 500)    
process_payment(upi, 200)           