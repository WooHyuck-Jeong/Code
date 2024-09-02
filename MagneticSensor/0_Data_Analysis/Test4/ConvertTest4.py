import os 
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

movingFilePath = "/Users/jwh/Desktop/0730/Test4/"
file = glob.glob(movingFilePath + "*")

colName = "col"
useCols = [3, 4, 5]
sensorName = [f"s{i}" for i in np.arange(4, 7, 1)]

df = pd.read_table(file[0], names= [colName], skiprows= 100)
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

sensorList = [f"s{i}" for i in np.arange(1, 7, 1)]
res.columns = sensorList

def makeDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

saveFolder = movingFilePath + "result/"
saveFileName = str(file[0].split(f"{movingFilePath}")[1])
makeDirectory(saveFolder)

# res.to_csv(saveFolder + saveFileName + ".csv", index= False)