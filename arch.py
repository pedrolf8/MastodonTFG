import pandas as pd
import csv
t = pd.read_csv('/home/pllorente/dat.csv')
hora = pd.DataFrame()
dia = pd.DataFrame()
semana = pd.DataFrame()
mes = pd.DataFrame()
año = pd.DataFrame()
hd = []
dd = []
sd = []
md = []
ad = []
h = []
d = []
s = []
m = []
a = []
i = 0
print('listo')
for w in t[' window']:
    if('201' in str(t['date'].iloc[i])):
        print('algo')
        if (str(w)=='3600000'):
            h.append(t['date'].iloc[i])
            hd.append(t[' degree '].iloc[i])
        if(str(w)=='86400000'):
            d.append(t['date'].iloc[i])
            dd.append(t[' degree '].iloc[i])
        if(str(w)=='604800000'):
            s.append(t['date'].iloc[i])
            sd.append(t[' degree '].iloc[i])
        if(str(w)=='2592000000'):
            m.append(t['date'].iloc[i])
            md.append(t[' degree '].iloc[i])
        if(str(w)=='31536000000'):
            a.append(t['date'].iloc[i])
            ad.append(t[' degree '].iloc[i])
    i = i + 1
print('listo')
hora['date'] = h
hora[' degree '] = hd
dia['date'] = d
dia[' degree '] = dd
semana['date'] = s
semana[' degree '] = sd
mes['date'] = m
mes[' degree '] = md
año['date'] = a
año[' degree '] = ad
   
hora.to_csv('deghora.csv')
semana.to_csv('degsemana.csv')
mes.to_csv('degmes.csv')
año.to_csv('degaño.csv')