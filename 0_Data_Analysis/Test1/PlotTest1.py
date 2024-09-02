import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# folderPath = input("Folder: ")
folderPath = "/Users/jwh/Desktop/0730/Test1/result/"
# folderPath = "C:\\Users\\hyukk\\Desktop\\0726\\result\\"
# folderPath = "C:\\Users\\hyukk\\Desktop\\0730\\Test1\\result\\"

fileList = [file for file in sorted(glob.glob(folderPath + "*")) if os.path.isfile(file)]

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

yMin = -1500
yMax = 50
yLim = [yMin, yMax]

fig, ax = plt.subplots(2, 3, figsize= (12, 8))
scaledSensor1.plot(kind= "line", ax= ax[0, 0], title= "Sensor1", ylim= yLim).legend(loc= "center right", bbox_to_anchor= (1.2, 0.5))
scaledSensor2.plot(kind= "line", ax= ax[0, 1], title= "Sensor2", ylim= yLim).legend(loc= "center right", bbox_to_anchor= (1.2, 0.5))
scaledSensor3.plot(kind= "line", ax= ax[0, 2], title= "Sensor3", ylim= yLim).legend(loc= "center right", bbox_to_anchor= (1.2, 0.5))
scaledSensor4.plot(kind= "line", ax= ax[1, 0], title= "Sensor4", ylim= yLim).legend(loc= "center right", bbox_to_anchor= (1.2, 0.5))
scaledSensor5.plot(kind= "line", ax= ax[1, 1], title= "Sensor5", ylim= yLim).legend(loc= "center right", bbox_to_anchor= (1.2, 0.5))
scaledSensor6.plot(kind= "line", ax= ax[1, 2], title= "Sensor6", ylim= yLim).legend(loc= "center right", bbox_to_anchor= (1.2, 0.5))
plt.subplots_adjust(wspace= 0.4, hspace= 0.6)
plt.show()

# C:\Users\hyukk\Desktop\MagneticTest\Test1_2\result\