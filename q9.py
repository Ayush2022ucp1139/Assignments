class Course:
    def __init__(self, course_name, total_modules):
        self.course_name = course_name
        self.total_modules = total_modules
        self.completed_modules = 0
    
    def complete_module(self, count=1):
        if self.completed_modules + count <= self.total_modules:
            self.completed_modules += count
            return True
        return False
    
    def get_progress(self):
        if self.total_modules == 0:
            return 0
        return (self.completed_modules / self.total_modules) * 100
    
    def show_progress(self):
        progress = self.get_progress()
        print(f"Course: {self.course_name}")
        print(f"Progress: {self.completed_modules}/{self.total_modules} modules")
        print(f"Completion: {progress:.1f}%")
    
    def __str__(self):
        progress = self.get_progress()
        return f"{self.course_name} - {progress:.1f}% complete"

python_course = Course("Python Programming", 10)
    
print("Starting course:")
python_course.show_progress()
    
print("\nCompleting 3 modules:")
python_course.complete_module(3)
python_course.show_progress()
    
print("\nCompleting 5 more modules:")
python_course.complete_module(5)
python_course.show_progress()
    
print("\nTrying to complete 3 more (should cap at total):")
if not python_course.complete_module(3):
    print("Cannot complete more modules than total!")
python_course.show_progress()