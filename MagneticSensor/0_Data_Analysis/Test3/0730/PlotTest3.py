import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

folderPath = "/Users/jwh/Desktop/0730/Test3/result/"

fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]

def makeDir(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

def readCsv(file):
    res = pd.read_csv(file, sep= ",")
    return res

base123 = readCsv(fileList[0])
base456 = readCsv(fileList[1])
sensor1 = readCsv(fileList[2])
sensor2 = readCsv(fileList[3])
sensor3 = readCsv(fileList[4])
sensor4 = readCsv(fileList[5])
sensor5 = readCsv(fileList[6])
sensor6 = readCsv(fileList[7])

sensorNames = [f"s{i}" for i in np.arange(1, 7, 1)]

meanBase123 = pd.DataFrame(base123.mean(axis= 0).T.to_numpy().reshape(1, 6), columns= sensorNames)
meanBase456 = pd.DataFrame(base456.mean(axis= 0).T.to_numpy().reshape(1, 6), columns= sensorNames)

s1 = (sensor1.iloc[:, 0] - meanBase123.iloc[0, 0]).to_frame()

# print(s1)
def getScaled(df, idx):

    res = pd.DataFrame()

    if idx == 123:
        for i in range(6):
            tmp = (df.iloc[:, i] - meanBase123.iloc[0, i]).to_frame()
            res = pd.concat((res, tmp), axis= 1)
    
    elif idx == 456:
        for i in range(6):
            tmp = (df.iloc[:, i] - meanBase456.iloc[0, i]).to_frame()
            res = pd.concat((res, tmp), axis= 1)

    return res

sc1 = getScaled(sensor1, 123)
sc2 = getScaled(sensor2, 123)
sc3 = getScaled(sensor3, 123)
sc4 = getScaled(sensor4, 456)
sc5 = getScaled(sensor5, 456)
sc6 = getScaled(sensor6, 456)

sc1 = sc1[['s1', 's2', 's3']]
sc2 = sc2[['s1', 's2', 's3']]
sc3 = sc3[['s1', 's2', 's3']]
sc4 = sc4[['s4', 's5', 's6']]
sc5 = sc5[['s4', 's5', 's6']]
sc6 = sc6[['s4', 's5', 's6']]


scResult = [sc1, sc2, sc3, sc4, sc5, sc6]

# savePath = folderPath.split("result/")[0] + "ScaledData/"
# makeDir(savePath)

# for i in range(len(scResult)):
#     scResult[i].to_csv(savePath + f"sc{i+1}.csv", index= False)

fig, axs = plt.subplots(2, 3, figsize= (12, 10))
fig.suptitle("Test3")
for i, ax in enumerate(axs.flat):
    scResult[i].plot(kind= 'line', ax= ax, title= f"s{i+1}")

plt.show()