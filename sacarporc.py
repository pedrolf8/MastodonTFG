import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

d = pd.read_csv('ConnectedComponents/dat.csv')
g = d.groupby(['date','CCL'], as_index=False).count()
h = d.groupby(['date'], as_index=False).count()
f = []
r = []
t = []
hh = pd.DataFrame()
rr = pd.DataFrame()
i = 0
ii = 0
w = h.iloc[0]
while(ii<len(h)):
    rr = g[g['date'] == h['date'].iloc[ii]]
    f.append(h['date'].iloc[ii])
    r.append(rr['userid'].max()/h['CCL'].iloc[ii])
    t.append(rr['userid'].max())
    ii = ii + 1
hh['date'] = f
hh['porc'] = r
hh['tamaño'] = t
hh.to_csv('CCLtodos2.csv')
        
