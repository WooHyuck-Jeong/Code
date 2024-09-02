import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Datapath
dataPath = "/Users/jwh/Documents/KOTC/수중도킹/2024년도/6_자기장센서 시험/Test0730_전달/Test2/result/"

# Files
fileNames = [file for file in sorted(glob.glob(dataPath + "*.csv")) if os.path.isfile(file)]

base = pd.read_csv(fileNames[0], sep= ",")
meanBase = pd.DataFrame(base.mean(axis= 0))

fileIdx = [1, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7]

files = []

for idx in fileIdx:
    caseData = pd.read_csv(fileNames[idx], sep= ",")
    files.append(caseData)

sensorNames = [f's{i}' for i in np.arange(1, 7, 1)]

def getScaledData(df):
    res = []
    for i in range(6):
        res.append(df.iloc[:, i] - meanBase.iloc[i, 0])
    res = np.array(res).reshape(6, -1).T
    res = pd.DataFrame(res, columns= sensorNames)
    return res

scaledData = []
for i in range(len(files)):
    scaled = getScaledData(files[i])
    scaledData.append(scaled)

yMin = -2200
yMax = 2200
yLim = [yMin, yMax]

fig, axs = plt.subplots(3, 5, figsize= (20, 18))
for i, ax in enumerate(axs.flat):
    scaledData[i].plot(kind= "line",
                       ax= ax,
                       ylim= yLim,
                       title= f"Case {i+1}",
                       ).legend()
plt.subplots_adjust(hspace= 0.4)
plt.show()