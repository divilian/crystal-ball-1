import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

gradebook = pd.read_csv(io.StringIO('''
student,Q1,Q2,Q3,Q4,lab1,lab2,lab3,lab4,lab5
Filbert,7,9,10,7,15,19,14,20,20
Jezebel,8,7,0,6,12,12,16,0,20
Betty Lou,10,10,10,10,20,20,20,20,20
Biff,3,2,6,5,10,12,0,0,16
Melvin,0,0,10,10,0,18,20,14,20
''')).set_index('student')

print(gradebook)

def print_harass_list(gradebook):
    for row in gradebook.itertuples():
        if any_zeros(np.array([row.lab1,row.lab2,row.lab3,row.lab4,row.lab5])):
            print("Better check up on {}.".format(row.Index))

def any_zeros_WRONG(labs):
    for lab in labs:
        if lab == 0:
            return True
        else:
            return False

def any_zeros(labs):
    for lab in labs:
        if lab == 0:
            return True
    return False

print_harass_list(gradebook)
