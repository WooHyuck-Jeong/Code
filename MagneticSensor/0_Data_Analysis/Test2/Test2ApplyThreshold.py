import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

dataPath = "/Users/jwh/Documents/KOTC/수중도킹/2024년도/6_자기장센서 시험/Test0730_전달/Test2/result/"

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

positiveThreshold = 10
negativeThreshold = -10

meanCase = meanScaled.copy()

filteredCase = []
for i in range(len(meanCase)):
    temp = []
    for j in range(meanCase[i].shape[0]):
        if negativeThreshold <= meanCase[i][j] <= positiveThreshold:
            meanCase[i][j] = 0
            temp.append(meanCase[i][j])
        else:
            temp.append(meanCase[i][j])
    filteredCase.append(temp)

filteredCase = [pd.DataFrame(filteredCase[i]) for i in range(len(filteredCase))]
filteredCase = pd.concat(filteredCase, axis= 1)

caseNum = [f'case{i}' for i in np.arange(1, 16, 1)]

filteredCase.columns = caseNum
filteredCase.index = sensorNames

fig, axs = plt.subplots(3, 5, figsize= (20, 18))

cmap = cm.get_cmap('tab20', 15)
# colors = [cmap(i) for i in range(15)]
colors = ['red', 'orange', 'darkkhaki', 'green', 'cyan', 'blue', 'violet', 'black', 'magenta', 'darkorange', 'navy', 'r', 'purple', 'c', 'gray']

for i, ax in enumerate(axs.flat):
    filteredCase.iloc[:, i].plot(kind= "line",
                                 ax= ax,
                                 title= f'Case {i + 1}',
                                 grid= True,
                                 marker= "v",
                                 markersize= 4,
                                 color= colors[i],
                                 ylim= [-1500, 1500],
                                 yticks= np.arange(-1500, 2000, 500)
                                 )

plt.subplots_adjust(hspace= 0.4)
plt.show()