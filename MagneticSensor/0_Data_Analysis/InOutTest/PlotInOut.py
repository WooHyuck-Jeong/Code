import os, glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

folderPath = "/Users/jwh/Desktop/Test0730_전달/InOut70/result/"

fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]
# base = 1
# in_70 = 2
# out_70 = 3

useCols = [3, 4, 5]

baseData = pd.read_csv(fileList[0], sep= ",", usecols= useCols)
innerData = pd.read_csv(fileList[1], sep= ",", usecols= useCols)
outerdata = pd.read_csv(fileList[2], sep= ",", usecols= useCols)

meanBaseData = baseData.mean(axis= 0).to_numpy()

def getScaledData(df):
    res = []
    
    for i in range(3):
        scaledData = df.iloc[:, i] - meanBaseData[i]
        res.append(scaledData)

    res = np.array(res).reshape(3, -1).T
    res = pd.DataFrame(res, columns= ['s4', 's5', 's6'])

    return res

scaledInnerData = getScaledData(innerData)
scaledOuterData = getScaledData(outerdata)

scaledData = [scaledInnerData, scaledOuterData]

fig, axs = plt.subplots(1, 2, figsize= (10, 8))
for i, ax in enumerate(axs.flat):
    scaledData[i].plot(kind= "line", ax= ax).legend()

plt.show()