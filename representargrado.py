import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



data2 = pd.read_csv('dat.csv')
data2["date"] = pd.to_datetime(data2["date"], unit='ms')
data2 = data2.sort_values(by='date')
plt.rcParams["figure.figsize"] = (12,8)
plt.plot(data2['date'], data2[' degree '])
plt.xlabel('Fecha')
plt.ylabel('Grado')

plt.savefig('todos.png')
