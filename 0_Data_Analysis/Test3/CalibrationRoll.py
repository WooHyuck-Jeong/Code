import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

basePath = "/Users/jwh/Desktop/0720/MagneticTest/Test2/result/Base.csv"
rollPath = "/Users/jwh/Desktop/0720/MagneticTest/Test3/result/Roll1.csv"

base = pd.read_csv(basePath, sep= ",")
baseMean = pd.DataFrame(base.mean(axis= 0), columns= ["base"])

roll = pd.read_csv(rollPath, sep= ",")

sensorList = [f"s{i+1}" for i in range(6)]

def getScaled(df):
    res = []
    for i in range(6):
        res.append(df.iloc[:, i] - baseMean.iloc[i, 0])

    res = np.array(res).reshape(6, -1).T
    res = pd.DataFrame(res, columns= sensorList)

    return res

scaledRoll = getScaled(roll)
# scaledRoll.to_csv("/Users/jwh/Desktop/0720/MagneticTest/Test3/result/ScaledRoll.csv", sep= ",")

data = scaledRoll.copy()

plt.ion()
fig, axs = plt.subplots(3, 2, figsize= (15, 10))
colorList = ["red", "orange", "gold", "green", "blue", "violet"]
lines = []

for i, ax in enumerate(axs.flat):
    line, = ax.plot([], [], label= f"Sensor {i + 1}", color= colorList[i])
    lines.append(line)
    ax.legend()
    ax.grid()
    ax.set_ylabel("Value")
    ax.set_title(f"Sensor {i + 1} Data")

idx = []
sensorData = [[] for _ in range(data.shape[1])]

def updatePlot():
    for i, ax in enumerate(axs.flat):
        lines[i].set_xdata(idx)
        lines[i].set_ydata(sensorData[i])
        ax.relim()
        ax.autoscale_view()

for i in range(data.shape[0]):
    idx.append(i)
    
    for j in range(data.shape[1]):
        sensorData[j].append(data.iloc[i, j])
    updatePlot()
    plt.pause(0.01)

plt.ioff()
plt.tight_layout()
plt.show()