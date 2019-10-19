import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

simpsons = pd.read_csv(io.StringIO('''
name,species,age,gender,fave,IQ,hair,salary
Homer,human,36,M,beer,74,,52000
Marge,human,34,F,helping others,120,stacked tall,
Bart,human,10,M,skateboard,90,buzz,
Lisa,human,8,F,saxophone,200,curly,
Maggie,human,1,F,pacifier,100,curly,
SLH,dog,4,M,,,shaggy,
''')).set_index('name')

print("\norig:")
print(simpsons)
print("\ndropna():")
print(simpsons.dropna())
print("\ndropna(how=\"all\"):")
print(simpsons.dropna(how="all"))
print("\nfillna(\"none\"):")
print(simpsons.fillna("none"))

simpsons['salary'] = simpsons['salary'].fillna(0)
simpsons['IQ'] = simpsons['IQ'].fillna(30)
simpsons['hair'] = simpsons['hair'].fillna("none")
print("\nfillnas:")
print(simpsons)

print("\nbart:")
print(simpsons.loc['Bart'])
print("\n3:")
print(simpsons.iloc[3])
print("\nage:")
print(simpsons['age'])
print("\nkids:")
print(simpsons.loc[['Lisa','Maggie','Bart']])
print("\nweird:")
print(simpsons.iloc[[1,3,4]])
print("\nage, fave, and IQ:")
print(simpsons[['age','fave','IQ']])
