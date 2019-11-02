import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

people = pd.read_csv('people.csv')

print(pd.crosstab(people.gender, people.color))
