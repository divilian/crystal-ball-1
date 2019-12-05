import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

students = pd.read_csv(io.StringIO('''
Major,Age,Gender,VG
PSYC,22,F,No
MATH,20,F,No
PSYC,19,F,No
CPSC,20,M,Yes
MATH,18,M,Yes
CPSC,20,F,No
CPSC,19,O,No
CPSC,17,M,Yes
PSYC,18,F,No
CPSC,20,F,No
MATH,18,F,No
CPSC,22,F,Yes
MATH,21,M,No
CPSC,23,M,Yes
PSYC,17,M,Yes
CPSC,18,F,No
PSYC,19,F,Yes
'''
))

students = pd.read_csv(io.StringIO('''
Major,Age,Gender,VG
PSYC,old,F,No
MATH,middle,F,No
PSYC,middle,F,No
CPSC,middle,M,Yes
MATH,young,M,Yes
CPSC,middle,F,No
CPSC,middle,O,No
CPSC,young,M,Yes
PSYC,young,F,No
CPSC,middle,F,No
MATH,young,F,No
CPSC,old,F,Yes
MATH,middle,M,No
CPSC,old,M,Yes
PSYC,young,M,Yes
CPSC,young,F,No
PSYC,middle,F,Yes
'''
))

print(students)

students_test = pd.read_csv(io.StringIO('''
Major,Age,Gender,VG
CPSC,young,F,No
CPSC,old,O,No
MATH,old,F,No
CPSC,middle,M,No
PSYC,middle,F,Yes
PSYC,young,F,No
MATH,old,M,Yes
CPSC,middle,M,Yes
'''
))

print(students_test)

def predict(major, age, gender):
    if gender == 'M':
        if age == 'young':
            return 'Yes'
        elif age == 'middle':
            if major == 'PSYC' or major == 'CPSC':
                return 'Yes'
            elif major == 'MATH':
                return 'No'
        elif age == 'old':
            return 'Yes'
    elif gender == 'F':
        if major == 'MATH':
            return 'No'
        elif major == 'CPSC':
            if age == 'young' or age == 'middle':
                return 'No'
            elif age == 'old':
                return 'Yes'
        elif major == 'PSYC':
            if age == 'young' or age == 'old':
                return 'No'
            elif age == 'middle':
                return 'Yes'  # Here's our "contradiction"
    elif gender == 'O':
        return 'No'

count = 0
for row in students_test.itertuples():
    if predict(row.Major, row.Age, row.Gender) == row.VG:
        print("  Predicted {}/{}/{} right!".format(row.Major,row.Age,row.Gender))
        count += 1
    else:
        print("X Predicted {}/{}/{} wrong. :(".format(row.Major,row.Age,row.Gender))

accuracy = count / len(students_test) * 100
print("Our accuracy on the test set was {}% ({}/{}).".format(accuracy,
    count, len(students_test)))

