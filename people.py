import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

people = pd.read_csv('people.csv')

gender_color = pd.crosstab(people.gender, people.color)
print(gender_color)
print(scipy.stats.chi2_contingency(gender_color))

print(scipy.stats.chi2_contingency(gender_color))

people.boxplot('salary',by='gender')

print(people.groupby('gender')['salary'].mean())

print(people.groupby('gender')['followers'].mean())

print(scipy.stats.ttest_ind(
    people[people.gender=="female"]['followers'],
    people[people.gender=="male"]['followers']))

print(scipy.stats.ttest_ind(
    people[people.gender=="female"]['salary'],
    people[people.gender=="male"]['salary']))
