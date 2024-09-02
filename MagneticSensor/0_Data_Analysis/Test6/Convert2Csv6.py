import os
import sys
import glob
import numpy as np
import pandas as pd

def makeDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

if sys.platform == "win32":
    # 윈도우인 경우 폴더 경로
    print("윈도우임")
    folderPath = "C:\\Users\hyukk\\Desktop\\0809\\Test6\\"
else:
    # 맥인 경우 폴더 경로
    print("맥임")
    folderPath = "/Users/jwh/Desktop/0809/Test6/"
    
fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]

savePath = folderPath + "result\\"
makeDirectory(savePath)

colName = "col"
sensorList = [f's{i}' for i in np.arange(1, 7, 1)]

for file in fileList:
    df = pd.read_table(file, names= [colName], skiprows= 200)
    df = df.iloc[:, 0].str[-39:]
    df = pd.DataFrame(df, columns= [colName])
    
    s1 = df[colName].str[4:9]
    s2 = df[colName].str[9:14]
    s3 = df[colName].str[14:19]
    s4 = df[colName].str[20:25]
    s5 = df[colName].str[25:30]
    s6 = df[colName].str[30:35]
    
    res = [s1, s2, s3, s4, s5, s6]
    res = pd.concat(res, axis= 1)
    res.columns = sensorList
    
    saveName = savePath + file.split(f'{folderPath}')[1] + ".csv"
    print(saveName)

    res.to_csv(saveName, index= False)