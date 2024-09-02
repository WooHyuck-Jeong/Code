import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

folderPath = "/Users/jwh/Desktop/0720/MagneticTest/Test3/"
fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]

def makeDirectory(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath, exist_ok= True)

saveDirectoryPath = folderPath + "result/"
makeDirectory(saveDirectoryPath)

colName = "col"
sensorColName = [f"s{i+1}" for i in range(6)]

for file in fileList:
    df = pd.read_table(file, names= [colName])
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
    
    res.to_csv(saveDirectoryPath + saveFileName + ".csv", index= False)