import numpy as np

#Q1
marks = np.array([51,45,63,76,82,91,47,38,51,100]) #Out of 10
print(marks)
greater_than_50_marks = marks[marks > 50]
print(greater_than_50_marks)

#Q2
mean_of_the_class = np.mean(marks)
print("The average of the class is: ",mean_of_the_class)

#Q3
median_of_the_class = np.median(marks)
print("The median of the class is: ",median_of_the_class)

#Q4
values, counts = np.unique(marks, return_counts=True)
mode = values[np.argmax(counts)]
print("The average of the class is: ",mode)

#Q5
temperatures = np.array([[1,2,3,4,5,6,7],
                        [8,9,10,11,12,13,14],
                        [15,16,17,18,19,20,21],
                        [22,23,24,25,26,27,28]])

print("The temperatures of the second week are: ",temperatures[1])

#Q6
max_value = np.max(temperatures)
print(max_value)

#Q7
def min_max_normalize(arr):
    arr_min = np.min(arr)
    arr_max = np.max(arr)
    normalized_arr = (arr - arr_min) / (arr_max - arr_min)
    return normalized_arr

normalized_arr = min_max_normalize(temperatures)
print(normalized_arr)

#Q8
standard_deviation = np.std(temperatures)
print(standard_deviation)

#Q9
stock_data = np.random.randint(0, 100, size=(3, 4, 5))
print("3D Stock Data Shape:", stock_data.shape)

product_2_week_3 = stock_data[1, 2, :] 
print("Stock of Product 2 in Week 3 (All Categories):", product_2_week_3)

#Q10
total_stock_per_product = np.sum(stock_data, axis=(1, 2))
print("Total stock per product:", total_stock_per_product)

#Q11
survey_data = np.random.randint(1,10,50)
more_than_7 = survey_data[survey_data > 7]
print(len(more_than_7))

#Q12
count = 0
for i in range(50):
    if(survey_data[i] == 5):
        count += 1
print(count)

#Q13
normalized_rating = min_max_normalize(survey_data)
print(normalized_rating)

#Q14
steps_data = np.random.randint(500,10000,size=(5,7))
average_steps_per_user = np.mean(steps_data, axis=1)

print("Average steps per user:", average_steps_per_user)

#Q15
day_3_steps = []

for i in range(5):
    day_3_steps.append(steps_data[i][2])

print(day_3_steps)

#Q16
more_than_7000_steps = set()

for i in range(5):
    for j in range(7):
        if(steps_data[i][j] > 7000):
            more_than_7000_steps.add(i)

print(more_than_7000_steps)

#Q17
chemical_results = np.array([
    [12.1, 12.3, 11.9, 12.0, 12.2, 12.5, 11.8, 12.1, 12.4, 12.0],
    [8.5, 8.7, 8.4, 8.9, 8.6, 8.3, 8.8, 8.5, 8.7, 8.6],           
    [15.2, 15.0, 15.5, 15.1, 15.3, 14.9, 15.4, 15.2, 15.0, 15.1]  
])

mean_results = np.mean(chemical_results, axis=1)
print("Mean results:", mean_results)

#Q18
deviations = np.abs(chemical_results - mean_results.reshape(-1, 1))
max_dev_trials = np.argmax(deviations, axis=1)
print("Trials with max deviation:", max_dev_trials)

#Q19
patient_vitals = np.array([
    [[98, 72, 120], [97, 71, 118], [99, 73, 122], [96, 70, 119], [98, 72, 121]],
    [[101, 75, 130], [100, 76, 129], [102, 74, 131], [99, 77, 128], [101, 75, 132]]
])

first_patient_day4 = patient_vitals[0, 3]
print("Vitals for Patient 1 on Day 4:", first_patient_day4)

#Q20
from scipy import stats

heart_rates = patient_vitals[0, :, 1]

mode_result = stats.mode(heart_rates)
print(mode_result)
