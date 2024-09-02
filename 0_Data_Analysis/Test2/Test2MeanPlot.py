import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Data path
dataPath = "/Users/jwh/Documents/KOTC/수중도킹/2024년도/6_자기장센서 시험/Test0730_전달/Test2/result/"

# Files
fileNames = [file for file in sorted(glob.glob(dataPath + "*.csv")) if os.path.isfile(file)]

fileIdx = [1, 8, 9, 10, 11, 12, 13, 14, 15, 2, 3, 4, 5, 6, 7]

files = []

for i in fileIdx:
    caseData = pd.read_csv(fileNames[i], sep= ",")
    files.append(caseData)

base = pd.read_csv(fileNames[0], sep= ",")
meanBase = pd.DataFrame(base.mean(axis= 0))

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

meanScaled = [scaledData[i].mean(axis= 0) for i in range(len(scaledData))]

fig, axs = plt.subplots(3, 5, figsize= (20, 18))

cmap = matplotlib.colormaps.get_cmap('tab20')
colors = [cmap(i) for i in range(15)]

yLimit = [-2000, 2000]

for i, ax in enumerate(axs.flat):
    for sensor in sensorNames:
        meanScaled[i].plot(kind="line", ax=ax, title=f'Case {i+1}', grid=True, marker="*", color=colors[i])

plt.subplots_adjust(hspace= 0.4)
plt.show()