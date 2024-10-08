import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def makeDirectory(dirName):
    
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

folderPath = "/Users/jwh/Desktop/0730/LR/"

fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]

savePath = folderPath + "result/"
makeDirectory(savePath)

colName = "col"
sensorColName = [f"s{i}" for i in np.arange(1, 7, 1)]

for file in fileList:
    
    df = pd.read_table(file, names= [colName], skiprows= 100)
    df = df.iloc[:, 0].str[-39:]
    df = pd.DataFrame(df, columns= [colName])

    s1 = df[colName].str[4:9]
    s2 = df[colName].str[9:14]
    s3 = df[colName].str[14:19]
    s4 = df[colName].str[20:25]
    s5 = df[colName].str[25:30]
    s6 = df[colName].str[30:35]

    res = pd.concat((s1, s2), axis= 1)
    res = pd.concat((res, s3), axis= 1)
    res = pd.concat((res, s4), axis= 1)
    res = pd.concat((res, s5), axis= 1)
    res = pd.concat((res, s6), axis= 1)

    res.columns = sensorColName

    saveFileName = str(file.split(f"{folderPath}")[1])

    res.to_csv(savePath + saveFileName + ".csv", index= False)