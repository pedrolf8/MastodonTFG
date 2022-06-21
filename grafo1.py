import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('degdia.csv')
data2 = pd.read_csv('deghora.csv')
data3 = pd.read_csv('degsemana.csv')
data4 = pd.read_csv('degmes.csv')
data5 = pd.read_csv('degaño.csv')

data["date"] = pd.to_datetime(data["date"], unit='ms')
data2["date"] = pd.to_datetime(data2["date"], unit='ms')
data3["date"] = pd.to_datetime(data3["date"], unit='ms')
data4["date"] = pd.to_datetime(data4["date"], unit='ms')
data5["date"] = pd.to_datetime(data5["date"], unit='ms')

data = data.sort_values(by='date')
data2 = data2.sort_values(by='date')
data3 = data3.sort_values(by='date')
data4 = data4.sort_values(by='date')
data5 = data5.sort_values(by='date')

plt.rcParams["figure.figsize"] = (12,8)

plt.plot(data5['date'], data5['degree'])
plt.plot(data4['date'], data4['degree'] )
plt.plot(data3['date'], data3['degree'])
plt.plot(data['date'], data['degree'])
plt.plot(data2['date'], data2['degree'])



plt.xlabel('Fecha')
plt.ylabel('Grado')
plt.savefig('total.png')