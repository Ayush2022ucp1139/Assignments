class Student:
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__marks = {}
        
    def get_name(self):
        return self.__name
        
    def get_student_id(self):
        return self.__student_id
        
    def get_marks(self, subject=None):
        if subject:
            return self.__marks.get(subject, "Subject not found")
        return self.__marks.copy()
        
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) > 0:
            self.__name = new_name
        else:
            print("Invalid name format")
            
    def add_mark(self, subject, mark):
        if not isinstance(subject, str) or len(subject) == 0:
            print("Invalid subject name")
            return
        if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
            print("Mark must be a number between 0 and 100")
            return
        self.__marks[subject] = mark
        print(f"Mark {mark} added for {subject}")
            
student1 = Student("Alice Johnson", "S12345")

student1.add_mark("Math", 85)
student1.add_mark("Science", 92)
student1.add_mark("History", 78)


student1.add_mark("English", 105) 

print(student1.get_name())
print(student1.get_marks("Math"))
print(student1.get_marks()) 
            