
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats


taylor = np.repeat("Taylor Swift", 388)
katy = np.repeat("Katy Perry", 265)
drake = np.repeat("Drake", 261)
adele = np.repeat("Adele", 212)
rihanna = np.repeat("Rihanna", 136)
bieb = np.repeat("Justin Bieber", 134)

celebs = np.concatenate([taylor, katy, drake, adele, rihanna, bieb])
np.random.shuffle(celebs)
celebs = pd.Series(celebs)

counts = celebs.value_counts()
print(counts)

plt.figure()
counts.sort_index().plot(kind='bar',color="purple")
plt.savefig('celebs2.png', bbox_inches='tight')
