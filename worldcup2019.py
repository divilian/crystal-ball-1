import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
import io

wc = pd.read_csv(io.StringIO('''
last,first,date,in_mins,in_secs,out_mins,out_secs,goals,asst,tackles,fouls
Morgan,Alex,28-Jun,0,0,90,0,0,0,2,1
Rapinoe,Megan,28-Jun,0,0,74,27,2,0,2,2
Press,Christen,28-Jun,74,27,90,0,0,0,1,0
Lavelle,Rose,28-Jun,0,0,90,0,0,1,3,0
Lavelle,Rose,7-Jul,0,0,90,0,1,0,4,1
Rapinoe,Megan,7-Jul,0,0,83,16,1,1,3,2
Lloyd,Carli,7-Jul,83,16,90,0,0,0,1,0
Dunn,Crystal,23-Jun,42,37,81,5,0,1,1,2
'''))

wc['in_time'] = np.round(wc['in_mins'] + wc['in_secs'] / 60,2)
wc['out_time'] = np.round(wc['out_mins'] + wc['out_secs'] / 60,2)
del wc['in_mins']
del wc['in_secs']
del wc['out_mins']
del wc['out_secs']

wc['mins_played'] = wc['out_time'] - wc['in_time']

grouped_wc = wc.groupby(['last','first'])
by_player = grouped_wc[['goals','asst','fouls','tackles','mins_played']].sum()

print(by_player)

by_player['tkl_per_90'] = np.round(by_player['tackles'] / by_player['mins_played'] * 90,2)
del by_player['tackles']
print(by_player)

#wc['starter'] = np.where(wc['in_time'] == 0, True, False)
#del wc['in_time']
#del wc['out_time']
print(wc)
