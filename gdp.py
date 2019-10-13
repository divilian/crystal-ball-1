
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

gdp = pd.read_csv(io.StringIO('''
Nation,Trillion
Italy,2.26
Germany,4.42
Brazil,2.26
United States,21.41
France,3.06
Canada,1.91
Japan,5.36
China,15.54
India,3.16
United Kingdom,3.02
'''), squeeze=True, index_col=0)

print(gdp)
plt.figure()
gdp.sort_values(ascending=False).plot(kind='bar',color="green")
plt.savefig('gdp2.png', bbox_inches='tight')
