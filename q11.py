from datetime import datetime

class ATMMachine:
    def __init__(self):
        self.__pin = ""          
        self.__balance = 0       
        self.__is_authenticated = False 
        self.__transaction_log = []   
        
    
    def insert_card(self, card_number):
        self.__card_number = card_number
        print(f"Card {card_number} inserted. Please enter your PIN.")
        
    def enter_pin(self, pin):
        self.__verify_pin(pin)
        
    def check_balance(self):
        if not self.__is_authenticated:
            print("Please authenticate first")
            return
        
        self.__log_transaction("Balance check")
        print(f"Your current balance is: ${self.__balance:.2f}")
        
    def deposit(self, amount):
        if not self.__is_authenticated:
            print("Please authenticate first")
            return
            
        if amount <= 0:
            print("Invalid deposit amount")
            return
            
        self.__balance += amount
        self.__log_transaction(f"Deposit: ${amount:.2f}")
        self.__update_server()
        print(f"${amount:.2f} deposited successfully.")
        
    def withdraw(self, amount):
        if not self.__is_authenticated:
            print("Please authenticate first")
            return
            
        if amount <= 0:
            print("Invalid withdrawal amount")
            return
            
        if amount > self.__balance:
            print("Insufficient funds")
            return
            
        self.__balance -= amount
        self.__log_transaction(f"Withdrawal: ${amount:.2f}")
        self.__update_server()
        print(f"Please take your ${amount:.2f}")
        
    def end_session(self):
        self.__is_authenticated = False
        print("Thank you for using our ATM. Please take your card.")
    
    def __verify_pin(self, pin):
        if len(pin) == 4 and pin.isdigit():
            self.__pin = pin
            self.__is_authenticated = True
            print("PIN accepted")
            self.__update_server()
        else:
            print("Invalid PIN")
            
    def __log_transaction(self, transaction_type):
        log_entry = {
            "card": self.__card_number,
            "type": transaction_type,
            "time": datetime.now(),
            "balance": self.__balance
        }
        self.__transaction_log.append(log_entry)
        
    def __update_server(self):
        pass

atm = ATMMachine()
atm.insert_card("1234567890123456")
atm.enter_pin("1234") 
atm.check_balance()
atm.deposit(500)
atm.withdraw(200)
atm.check_balance()
atm.end_session()

