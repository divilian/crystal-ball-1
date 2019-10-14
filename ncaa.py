import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats

raw = np.random.normal(22,12,300)
raw = np.concatenate([raw,np.random.normal(32,6,100)])
pts = pd.Series(np.clip(raw,0,np.inf)).astype(int)

plt.clf()
pts.plot(kind="hist")
plt.savefig("ncaa1.png")
plt.clf()
pts.plot(kind="hist",bins=30)
plt.savefig("ncaa2.png")
plt.clf()
pts.plot(kind="box")
plt.savefig("ncaabox.png")

print("min: {}".format(pts.quantile(0)))
print(".25-quantile: {}".format(pts.quantile(.25)))
print(".5-quantile: {}".format(pts.quantile(.5)))
print(".75-quantile: {}".format(pts.quantile(.75)))
print("max: {}".format(pts.quantile(1)))
print("mean: {}".format(pts.mean()))

