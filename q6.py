 
import pandas as pd
'''def calculate_results(sub1, sub2, sub3):
    total_marks = sub1 + sub2 + sub3
    percentage = (total_marks / 300) * 100
    return total_marks, percentage
num_students = int(input("Enter the number of students: "))
SID = []
SNAME = []
SUB1 = []
SUB2 = []
SUB3 = []
Total = []
Percentage = []
for i in range(num_students):
    print(f"\nEnter details for student {i+1}:")
    sid = input("Enter Student ID: ")
    sname = input("Enter Student Name: ")
    sub1 = float(input("Enter marks for Subject 1: "))
    sub2 = float(input("Enter marks for Subject 2: "))
    sub3 = float(input("Enter marks for Subject 3: "))
    total, percentage = calculate_results(sub1, sub2, sub3)
    SID.append(sid)
    SNAME.append(sname)
    SUB1.append(sub1)
    SUB2.append(sub2)
    SUB3.append(sub3)
    Total.append(total)
    Percentage.append(percentage)
data = {
    'SID': SID,
    'SNAME': SNAME,
    'SUB1': SUB1,
    'SUB2': SUB2,
    'SUB3': SUB3,
    'Total': Total,
    'Percentage': Percentage
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
'''
