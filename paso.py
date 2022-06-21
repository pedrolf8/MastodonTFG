import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('CCLhora2.csv')
data1 = pd.read_csv('CCLdia2.csv')
data2 = pd.read_csv('CCLsemana2.csv')
data3 = pd.read_csv('CCLmes2.csv')
data4 = pd.read_csv('CCLaño2.csv')


data["date"] = pd.to_datetime(data["date"], unit='ms')
data1["date"] = pd.to_datetime(data1["date"], unit='ms')
data2["date"] = pd.to_datetime(data2["date"], unit='ms')
data3["date"] = pd.to_datetime(data3["date"], unit='ms')
data4["date"] = pd.to_datetime(data4["date"], unit='ms')

plt.rcParams["figure.figsize"] = (12,12)
plt.plot(data['date'], data['tamaño'])
plt.plot(data1['date'], data1['tamaño'])
plt.plot(data2['date'], data2['tamaño'])
plt.plot(data3['date'], data3['tamaño'])
plt.plot(data4['date'], data4['tamaño'])


plt.ylabel('Weight of the LCC-')
plt.xlabel('Time')
plt.savefig('fgtodosc2.png')
