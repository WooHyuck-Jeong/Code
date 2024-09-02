import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def makeDirectory(dirName):
    """
        폴더 생성 함수
    """
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

folderPath = "/Users/jwh/Desktop/Test0730_전달/Test1/result/"
fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]

for i in range(len(fileList)):
    print(fileList[i])

savePath = folderPath.split("Test1/")[0] + "ScaledResult/Test1/"
# makeDirectory(savePath)

colName = "col"
sensorColName = ["s1", "s2", "s3", "s4", "s5", "s6"]

sensor1Data = pd.DataFrame()
sensor2Data = pd.DataFrame()
sensor3Data = pd.DataFrame()
sensor4Data = pd.DataFrame()
sensor5Data = pd.DataFrame()
sensor6Data = pd.DataFrame()
dfBase123Mean = pd.DataFrame()
dfBase456Mean = pd.DataFrame()

for file in fileList:
    name = file.split(f"{folderPath}")[1]
    name = name.split(".")[0]

    if name.startswith("s"):
        distance = name.split("_")[1]
        distance = distance.split(".")[0]

        if name.split("_")[0] == "s1":
            sensorData = pd.read_csv(file, sep= ",", usecols= [0], names = [f"d{distance}"], skiprows= 200)
            sensor1Data = pd.concat((sensor1Data, sensorData), axis = 1)
            
        elif name.split("_")[0] == "s2":
            sensorData = pd.read_csv(file, sep= ",", usecols= [1], names = [f"d{distance}"], skiprows= 200)
            sensor2Data = pd.concat((sensor2Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s3":
            sensorData = pd.read_csv(file, sep= ",", usecols= [2], names = [f"d{distance}"], skiprows= 200)
            sensor3Data = pd.concat((sensor3Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s4":
            sensorData = pd.read_csv(file, sep= ",", usecols= [3], names = [f"d{distance}"], skiprows= 200)
            sensor4Data = pd.concat((sensor4Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s5":
            sensorData = pd.read_csv(file, sep= ",", usecols= [4], names = [f"d{distance}"], skiprows= 200)
            sensor5Data = pd.concat((sensor5Data, sensorData), axis = 1)

        elif name.split("_")[0] == "s6":
            sensorData = pd.read_csv(file, sep= ",", usecols= [5], names = [f"d{distance}"], skiprows= 200)
            sensor6Data = pd.concat((sensor6Data, sensorData), axis = 1)

    elif name.endswith("123"):
        base = pd.read_csv(file, sep= ",", usecols= [0, 1, 2])
        baseMean = base.mean(axis = 0)
        dfBase123Mean = pd.concat((dfBase123Mean, baseMean), axis= 1).T.to_numpy().reshape(3,)
        
    elif name.endswith("456"):
        base = pd.read_csv(file, sep= ",", usecols= [3, 4, 5])
        baseMean = base.mean(axis= 0)
        dfBase456Mean = pd.concat((dfBase456Mean, baseMean), axis= 1).T.to_numpy().reshape(3,)

scaledSensor1 = sensor1Data - dfBase123Mean[0]
scaledSensor2 = sensor2Data - dfBase123Mean[1]
scaledSensor3 = sensor3Data - dfBase123Mean[2]
scaledSensor4 = sensor4Data - dfBase456Mean[0]
scaledSensor5 = sensor5Data - dfBase456Mean[1]
scaledSensor6 = sensor6Data - dfBase456Mean[2]

print(scaledSensor1.head())

scaledSensor = [scaledSensor1, scaledSensor2, scaledSensor3, scaledSensor4, scaledSensor5, scaledSensor6]

for i in range(len(scaledSensor)):
    scaledSensor[i].to_csv(savePath + f"ScaledSenor{i+1}.csv", sep= ",", index= False)