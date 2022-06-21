import csv
import json
import sys
from subprocess import call
import ast
import os
import pandas as pd


os.system('mkdir resultado')
os.chdir('analizar')
os.system('ls > lista.txt')
l = open('lista.txt', 'r')
a = []
for row in l:
    if ("lista" in row):
        print("")
    else:
        a.append(row.replace("\n", ""))
        
l.close()
res = pd.DataFrame()
bf = []
uf = []
dff = []
sf = []
vf = []
for x in a:
    print(x)
    df = pd.read_csv(str(x))
    i = 0
    y = 0
    while(y < len(df['ServerUser'])):
        dff.append(df['Date'].iloc[y])
        sf.append(df['ServerUser'].iloc[y])
        vf.append(df['UserId'].iloc[y])
        bf.append(df['ServerMentioned'].iloc[y])
        uf.append(df['UserMentioned'].iloc[y])
        y = y + 1

res['Date'] = dff
res['UserId'] = vf
res['ServerUser'] = sf    
res['UserMentioned'] = uf
res['ServerMentioned'] = bf
res.to_csv('../resultado/resultadoanalizar.csv')    


os.chdir('/home/pllorente/grafo')
os.system('ls > lista.txt')
l = open('lista.txt', 'r')
a = []
b = []
for row in l:
    if ("enlace" in row):
        b.append(row.replace("\n", ""))
    else:
        a.append(row.replace("\n", ""))
l.close()
nodo = pd.DataFrame()
i = 0
ni = []
nl = []
for d in a:
    f = pd.read_csv(str(d))
    while(i < len(f)):
        ni.append(f['Id'].iloc[i])
        nl.append(f['Label'].iloc[i])
        i = i + 1
nodo['Id'] = ni
nodo['Label'] = nl
nodo.to_csv('/home/pllorente/resultado/resultadonodo.csv')

enlace = pd.DataFrame()
i = 0
es = []
et = []
for d in b:
    f = pd.read_csv('/grafo/'+str(d))
    while(i < len(f)):
        ni.append(f['source'].iloc[i])
        nl.append(f['target'].iloc[i])
        i = i + 1
enlace['source'] = ni
enlace['target'] = nl
enlace.to_csv('resultado/resultadoenlace.csv')





