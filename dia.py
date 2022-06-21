import pandas as pd
import csv
t = pd.read_csv('/home/pllorente/ConnectedComponents/dat.csv')
hora = pd.DataFrame()
dia =pd.DataFrame()
semana = pd.DataFrame()
mes = pd.DataFrame()
año = pd.DataFrame()
h = []
hd = []
hc = []
d = []
dd = []
dc = []
s = []
sd = []
sc = []
m = []
md = []
mc = []
a = []
ad = []
ac = []
i = 0
print('listo')
for w in t['window']:
    if(str(w)=='3600000'):
        h.append(t['date'].iloc[i])
        hd.append(t['userid'].iloc[i])
        hc.append(t['CCL'].iloc[i])
    if(str(w)=='86400000'):
        d.append(t['date'].iloc[i])
        dd.append(t['userid'].iloc[i])
        dc.append(t['CCL'].iloc[i])    
    if(str(w)=='604800000'):
        s.append(t['date'].iloc[i])
        sd.append(t['userid'].iloc[i])
        sc.append(t['CCL'].iloc[i])
    if(str(w)=='2592000000'):
        m.append(t['date'].iloc[i])
        md.append(t['userid'].iloc[i])
        mc.append(t['CCL'].iloc[i])
    if(str(w)=='31536000000'):
        a.append(t['date'].iloc[i])
        ad.append(t['userid'].iloc[i])
        ac.append(t['CCL'].iloc[i])
    i = i + 1
print('listo')
hora['date'] = h
hora['userid'] = hd
hora['CCL'] = hc
dia['date'] = d
dia['userid'] = dd
dia['CCL'] = dc
semana['date'] = s
semana['userid'] = sd
semana['CCL'] = sc
mes['date'] = m
mes['userid'] = md
mes['CCL'] = mc
año['date'] = a
año['userid'] = ad
año['CCL'] = ac
hora.to_csv('deghorac.csv')
dia.to_csv('degdiac.csv')
semana.to_csv('degsemanac.csv')
mes.to_csv('degmesc.csv')
año.to_csv('degañoc.csv')