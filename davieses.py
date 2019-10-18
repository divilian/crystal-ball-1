import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

my_first_data_frame = pd.read_csv(io.StringIO('''
person,age,gender,height,instrument
Dad,50,M,73,piano
Mom,49,F,66,flute
Lizzy,19,F,63,guitar
TJ,18,M,71,trombone
Johnny,15,M,69,euphonium
''')).set_index('person')

print(my_first_data_frame)
