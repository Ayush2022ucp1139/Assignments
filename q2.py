def generate_student_report(name, marks):
    average = sum(marks) / len(marks)

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'
    
    return {
        'name': name,
        'average': round(average, 2),
        'grade': grade
    }

student_name = input("Enter student name: ")
marks = []
for i in range(3):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
    
report = generate_student_report(student_name, marks)
print("\n=== STUDENT REPORT ===")
print(f"Name: {report['name']}")
print(f"Marks: {marks}")
print(f"Average: {report['average']}")
print(f"Grade: {report['grade']}")