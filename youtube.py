
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

yt = np.clip(np.floor(np.random.normal(250,160,2000)),0,np.inf)
yt = np.concatenate([yt,
    np.clip(np.floor(np.random.normal(950,400,400)),0,np.inf)])
yt = np.concatenate([yt,
    np.clip(np.floor(np.random.normal(2050,900,240)),0,np.inf)])
yt = np.concatenate([yt,
    np.clip(np.floor(np.random.uniform(5050,1000000,90)),0,np.inf)])
yt = np.concatenate([yt,np.zeros(500)])
np.random.shuffle(yt)
yt = pd.Series(yt).astype(int)


qs = [ (q, np.floor(yt.quantile(q))) for q in np.arange(0,1.1,.1) ]
for q in qs:
    print("The {:.1f}-quantile is {:.0f}.".format(q[0],q[1]))
yt[yt < 1000].hist(bins=40)
yt.hist(bins=40)
plt.show()
