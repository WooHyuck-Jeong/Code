import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

folderPath = "C:\\Users\\hyukk\\Desktop\\0809\\Test5\\result\\"

fileList = [file for file in sorted(glob.glob(folderPath + "*.csv")) if os.path.isfile(file)]

innerData = []
outerData = []
topData = []
botData = []

for file in fileList:
    name = file.split(f'{folderPath}')[1]
    name = name.split(".")[0]
    
    if not name.startswith("Ba"):
        distance = name.split("_")[1]
        position = name.split("_")[0]
        
        if position == "I":
            data = pd.read_csv(file, sep= ",", usecols= [2], names= [f"d{distance}"], skiprows= 200, nrows= 2000)
            data = pd.DataFrame(data, columns= [f"d{distance}"])
            innerData.append(data)
            
        elif position == "O":
            data = pd.read_csv(file, sep= ",", usecols= [2], names= [f"d{distance}"], skiprows= 200, nrows= 2000)
            data = pd.DataFrame(data, columns= [f"d{distance}"])
            outerData.append(data)
            
        elif position == "T":
            data = pd.read_csv(file, sep= ",", usecols= [2], names= [f"d{distance}"], skiprows= 200, nrows= 2000)
            data = pd.DataFrame(data, columns= [f"d{distance}"])
            topData.append(data)
        
        elif position == "B":
            data = pd.read_csv(file, sep= ",", usecols= [2], names= [f"d{distance}"], skiprows= 200, nrows= 2000)
            data = pd.DataFrame(data, columns= [f"d{distance}"])
            botData.append(data)

innerData = pd.concat(innerData, axis= 1)
outerData = pd.concat(outerData, axis= 1)
topData = pd.concat(topData, axis= 1)
botData = pd.concat(botData, axis= 1)

baseData = pd.read_csv(fileList[5], sep= ",", usecols= [2], names= ["base"], skiprows= 200, nrows= 2000)
baseMean = baseData.mean(axis= 0)

def getScaledData(df):
    res = df - baseMean.iloc[0]
    return res

scaledInnerData = getScaledData(innerData)
scaledOuterData = getScaledData(outerData)
scaledTopData = getScaledData(topData)
scaledBotData = getScaledData(botData)

scaledData = [scaledInnerData, scaledOuterData, scaledTopData, scaledBotData]
meanScaledData = [scaledData[i].mean(axis= 0) for i in range(len(scaledData))]

imgTitleList = ["Inner", "Outer", "Top", "Bot"]

fig, axs = plt.subplots(2, 2, figsize= (20, 18))

for i, ax in enumerate(axs.flat):
    meanScaledData[i].plot(kind= "line", ax= ax, title= imgTitleList[i], ylim= [-2400, 2400], marker= "v").legend()
    
plt.subplots_adjust(hspace= 0.4, wspace= 0.4)
plt.show()