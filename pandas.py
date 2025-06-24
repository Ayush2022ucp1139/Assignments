import pandas as pd

#Q1
fruits = pd.Series(['Apple', 'Banana', 'Mango', 'Orange', 'strawberry'])
print(fruits[2])

#Q2
students = {'Rahul': 85, 'Ayush': 92, 'Ashwani': 78, 'Ronak': 88}
student_series = pd.Series(students)
print(student_series['Ayush'])

#Q3
data = {'Name': ['A', 'B', 'C'], 'Age': [20, 21, 19], 'Marks': [85, 90, 78]}
df1 = pd.DataFrame(data)
print(df1['Marks'])

#Q4
employees = pd.DataFrame({
    'Name': ['Raj', 'Ayush', 'Ashwani'],
    'Salary': [50000, 60000, 55000],
    'Department': ['IT', 'HR', 'Finance']
})
print(employees.loc[employees['Name'] == 'Raj', 'Salary'])

#Q5
students = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [20, 21, 19, 22],
    'Marks': [85, 90, 78, 92]
})
print(students.iloc[:3])

#Q6
customers = pd.DataFrame({
    'Name': ['X', 'Y', 'Z'],
    'Age': [25, 30, 35],
    'City': ['Mumbai', 'Delhi', 'Bangalore']
})
customers.at[2, 'Name'] = 'New Name'
print(customers)

#Q7
import numpy as np
df2 = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Marks': [85, np.nan, 78]
})
mean_marks = df2['Marks'].mean()
df2['Marks'] = df2['Marks'].fillna(mean_marks)
print(df2)

#Q8
# df = pd.read_excel('students.xlsx')
# print(df.head())

#Q9
# df = pd.read_excel('students.xlsx')
# null_age_rows = df.loc[df['Age'].isnull()]
# print(null_age_rows)

#Q10
employees_details = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Salary': [50000, 60000, 55000]
})
mean_salary = employees_details['Salary'].mean()
print(mean_salary)

#Q11
df3 = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Score': [85, np.nan, 78]
})
df3.loc[df3['Score'].isnull(), 'Score'] = 75
print(df3)

#Q12
df4 = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Age': [20, 21, 19, 22, 20],
    'Marks': [85, 90, 78, 92, 88],
    'Grade': ['A', 'A', 'B', 'A', 'B']
})
print(df4.iloc[1:5, 0:3])

#Q13
df5 = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Age': [20, 21, 19]
})
print(df5.loc[df5['Age'] > 20])

#Q14
items = pd.DataFrame({
    'Item': ['Pen', 'Notebook', 'Pencil'],
    'Quantity': [10, 5, 20],
    'Price': [10, 50, 5]
})
items['Total'] = items['Quantity'] * items['Price']
print(items)

#Q15
cities = pd.DataFrame({
    'City': ['Delhi', 'Mumbai', 'Chennai', 'Kolkata'],
    'Temperature': [28, np.nan, 32, np.nan]
})
mean_temp = cities['Temperature'].mean()
cities['Temperature'] = cities['Temperature'].fillna(mean_temp)
print(cities)