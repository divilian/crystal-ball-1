
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

num_plays = np.clip(np.floor(np.random.normal(250,160,2000)),0,np.inf)
num_plays = np.concatenate([num_plays,
    np.clip(np.floor(np.random.normal(950,400,400)),0,np.inf)])
num_plays = np.concatenate([num_plays,
    np.clip(np.floor(np.random.normal(2050,900,240)),0,np.inf)])
num_plays = np.concatenate([num_plays,
    np.clip(np.floor(np.random.uniform(5050,1000000,90)),0,np.inf)])
num_plays = np.concatenate([num_plays,np.zeros(500)])
np.random.shuffle(num_plays)
num_plays = pd.Series(num_plays).astype(int)


qs = [ (q, np.floor(num_plays.quantile(q))) for q in np.arange(0,1.1,.1) ]
for q in qs:
    print("The {:.1f}-quantile is {:.0f}.".format(q[0],q[1]))
print("The IQR is {:.2f}.".format(num_plays.quantile(.75) -
    num_plays.quantile(.25)))
plt.clf()
num_plays.plot(kind="hist", color="red")
plt.savefig("youtube1.png")
plt.clf()
num_plays.plot(kind="hist", bins=100, color="red")
plt.savefig("youtube2.png")
plt.clf()
num_plays[num_plays < 1000].plot(kind="hist", bins=40, color="green")
plt.savefig("youtube3.png")
plt.clf()
num_plays.plot(kind="box")
plt.savefig("youtubebox.png")
