import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def makeDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)


folderPath = "/Users/jwh/Desktop/Test0730/Test2/result/"

fileList = sorted(glob.glob(folderPath + "*.csv"))

base = pd.read_csv(fileList[0], sep= ",")
baseMean = pd.DataFrame(base.mean(axis= 0))

case1 = pd.read_csv(fileList[1], sep= ",")
case2 = pd.read_csv(fileList[8], sep= ",")
case3 = pd.read_csv(fileList[9], sep= ",")
case4 = pd.read_csv(fileList[10], sep= ",")
case5 = pd.read_csv(fileList[11], sep= ",")
case6 = pd.read_csv(fileList[12], sep= ",")
case7 = pd.read_csv(fileList[13], sep= ",")
case8 = pd.read_csv(fileList[14], sep= ",")
case9 = pd.read_csv(fileList[15], sep= ",")
case10 = pd.read_csv(fileList[2], sep= ",")
case11 = pd.read_csv(fileList[3], sep= ",")
case12 = pd.read_csv(fileList[4], sep= ",")
case13 = pd.read_csv(fileList[5], sep= ",")
case14 = pd.read_csv(fileList[6], sep= ",")
case15 = pd.read_csv(fileList[7], sep= ",")


def getScaledData(df):
    res = []
    for i in range(6):
        res.append(df.iloc[:, i] - baseMean.iloc[i, 0])
    
    res = np.array(res).reshape(6, -1).T
    res = pd.DataFrame(res, columns= ["s1", "s2", "s3", "s4", "s5", "s6"])

    return res

scaledCase1 = getScaledData(case1)
scaledCase2 = getScaledData(case2)
scaledCase3 = getScaledData(case3)
scaledCase4 = getScaledData(case4)
scaledCase5 = getScaledData(case5)
scaledCase6 = getScaledData(case6)
scaledCase7 = getScaledData(case7)
scaledCase8 = getScaledData(case8)
scaledCase9 = getScaledData(case9)
scaledCase10 = getScaledData(case10)
scaledCase11 = getScaledData(case11)
scaledCase12 = getScaledData(case12)
scaledCase13 = getScaledData(case13)
scaledCase14 = getScaledData(case14)
scaledCase15 = getScaledData(case15)

yMin = -2400
yMax = 2400

scaledCase = [scaledCase1, scaledCase2, scaledCase3, scaledCase4, scaledCase5, 
              scaledCase6, scaledCase7, scaledCase8, scaledCase9, scaledCase10, 
              scaledCase11, scaledCase12, scaledCase13, scaledCase14, scaledCase15]

savePath = "/Users/jwh/Desktop/Test0730_전달/ScaledResult/Test2/"
makeDirectory(savePath)

for i in range(len(scaledCase)):
    scaledCase[i].to_csv(f"/Users/jwh/Desktop/Test0730_전달/ScaledResult/Test2/ScaledCase{i+1}.csv", sep= ",", index= False)