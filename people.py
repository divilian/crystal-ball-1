import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

people = pd.read_csv('people.csv')

gender_color = pd.crosstab(people.gender, people.color)
print(gender_color)
print(scipy.stats.chi2_contingency(gender_color))
