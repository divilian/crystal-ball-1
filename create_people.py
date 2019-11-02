import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

NUM_PEEPS = 5000

genders = np.random.choice(['male','female','other'],p=[.489,.509,.002],
    size=NUM_PEEPS)
followers = np.round(np.where(genders == "male", 
    np.random.exponential(9, size=NUM_PEEPS),
    np.random.exponential(12, size=NUM_PEEPS)))
followers = followers + 13
colors = np.where(genders == "male", 
    np.random.choice(['red','blue','yellow','purple','pink'],
        p=[.2,.6,.1,.1,0], size=NUM_PEEPS),
    np.random.choice(['red','blue','yellow','purple','pink','green'],
        p=[.1,.1,.15,.25,.25,.15], size=NUM_PEEPS))
salaries = np.clip(np.round(followers * .5 + np.random.normal(40,25,size=NUM_PEEPS),2),0,np.inf)

peeps = pd.DataFrame({ 'gender': genders, 'followers': followers,
    'color': colors, 'salary': salaries })[['gender','salary','color','followers']]
peeps['followers'] = peeps['followers'].astype(int)
peeps.to_csv('madeup.csv',index=False)

print(scipy.stats.ttest_ind(peeps[peeps.gender=="male"]["salary"],peeps[peeps.gender=="female"]["salary"]))
print(peeps.groupby('gender')['salary'].median())


