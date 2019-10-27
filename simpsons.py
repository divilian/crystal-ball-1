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

print("\nLisa's IQ:")
lisas_row = simpsons.loc['Lisa']
lisas_iq = lisas_row['IQ'] 
print("Lisa's IQ is {}".format(lisas_iq))
print("Lisa's IQ is {}".format(simpsons.loc['Lisa']['IQ']))

print("\nindex:")
print(simpsons.index)
print("\ncolumns:")
print(simpsons.columns)
print("\nlen:")
print(len(simpsons))
print("\nshape:")
print(simpsons.shape)

print("\nsort by index:")
print(simpsons.sort_index())
print("\nsort by IQ:")
print(simpsons.sort_values('IQ'))
print("\nsort by two:")
print(simpsons.sort_values(['gender','hair','IQ'],
    ascending=[False,True,False]))
print("\nmedian IQ:")
print(simpsons['IQ'].median())
print("\ntotal salary:")
print(simpsons['salary'].sum())
print("\nwhole mean:")
print(simpsons.mean())

print("\nquery:")
print(simpsons[simpsons.age > 18])
print("\ncompound query:")
print(simpsons[(simpsons.age <= 18) & (simpsons.species == "human")])
print("\ncompound query #2:")
print(simpsons[(simpsons.IQ > 100) | (simpsons.age > 30)])
print("\nquery with cols #1:")
print(simpsons[simpsons.age > 18]['fave'])
print("\nquery with cols #2:")
print(simpsons[simpsons.age > 18][['fave','gender','IQ']])
