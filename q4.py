class Employee:
    name = ""
    emp_id = 0
    salary = 0

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def display_details(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Salary: ${self.salary:,.2f}")
    
emp1 = Employee("John Doe", "E1001", 75000)
emp2 = Employee("Jane Smith", "E1002", 85000)
    
emp1.display_details()
emp2.display_details()
    