import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

fans = pd.read_csv(io.StringIO('''
age,hometown,current_residence,years_in_residence,team
29,Warrenton,Warrenton,29,Redskins
39,Lubbock,Arlington,2,Cowboys
47,Allegheny,Chevy Chase,13,Redskins
31,Littleton,Littleton,3,Broncos
51,Orange County,Dumfries,23,Redskins
32,Warrenton,Winchester,11,Redskins
39,Dumfries,Miami,5,Redskins
31,Warrenton,Charlottesville,6,Jets
52,Arlington,Fredericksburg,17,Redskins
60,Tyson's Corner,Falls Church,4,Cowboys
17,Fredericksburg,Fredericksburg,17,Redskins
29,Fredericksburg,Seattle,21,Seahawks
37,Richmond,Richmond,37,Redskins
35,Mechanicsville,Orlando,8,Redskins
19,New York,New York,19,Giants
63,New York,Orlando,17,Giants
42,Alexandria,Manassas,10,Redskins
22,Allegheny,Harrisburg,1,Steelers
38,Mechanicsville,Fredericksburg,6,Redskins
32,Warrenton,Orlando,1,Redskins
'''))

print(fans)

training = fans.sample(frac=.7)
print(training)
test = fans[~fans.index.isin(training.index)]
print(test)