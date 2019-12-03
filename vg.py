import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

students = pd.read_csv(io.StringIO('''
major,age,gender,VG
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
major,age,gender,VG
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
