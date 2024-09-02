import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# folderPath = "/Users/jwh/Desktop/0730/Test1/result/"
folderPath = "/Users/jwh/Documents/KOTC/수중도킹/2024년도/6_자기장센서 시험/Test0730/Test1/result/"
# folderPath = "/Users/jwh/Desktop/0720/MagneticTest/Test1_2/result/"
# folderPath = input("Folder Path: ")
# folderPath = "C:\\Users\\hyukk\\Desktop\\0730\\result\\"
# folderPath = "C:\\Users\\hyukk\\Desktop\\0730\\Test1\\result\\"

fileList = [file for file in sorted(glob.glob(folderPath + "*.csv")) if os.path.isfile(file)]

sensor1Data = pd.DataFrame()
sensor2Data = pd.DataFrame()
sensor3Data = pd.DataFrame()
sensor4Data = pd.DataFrame()
sensor5Data = pd.DataFrame()
sensor6Data = pd.DataFrame()

base123Mean = pd.DataFrame()
base456Mean = pd.DataFrame()

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
        base123Mean = pd.concat((base123Mean, baseMean), axis= 1).T.to_numpy().reshape(3,)
        
    elif name.endswith("456"):
        base = pd.read_csv(file, sep= ",", usecols= [3, 4, 5])
        baseMean = base.mean(axis= 0)
        base456Mean = pd.concat((base456Mean, baseMean), axis= 1).T.to_numpy().reshape(3,)

scaledSensor1 = sensor1Data - base123Mean[0]
scaledSensor2 = sensor2Data - base123Mean[1]
scaledSensor3 = sensor3Data - base123Mean[2]
scaledSensor4 = sensor4Data - base456Mean[0]
scaledSensor5 = sensor5Data - base456Mean[1]
scaledSensor6 = sensor6Data - base456Mean[2]

scaledSensor1Mean = pd.DataFrame(scaledSensor1.mean(axis= 0), columns= ["s1"])
scaledSensor2Mean = pd.DataFrame(scaledSensor2.mean(axis= 0), columns= ["s2"])
scaledSensor3Mean = pd.DataFrame(scaledSensor3.mean(axis= 0), columns= ["s3"])
scaledSensor4Mean = pd.DataFrame(scaledSensor4.mean(axis= 0), columns= ["s4"])
scaledSensor5Mean = pd.DataFrame(scaledSensor5.mean(axis= 0), columns= ["s5"])
scaledSensor6Mean = pd.DataFrame(scaledSensor6.mean(axis= 0), columns= ["s6"])

distanceList = [i for i in np.arange(10, 90, 10)]
distanceList = pd.DataFrame(distanceList)

distanceIndex = [f"d{i}" for i in np.arange(10, 90, 10)]
distanceList.index = distanceIndex
distanceList.columns = ["distance"]

def concatScaledData(scaledData):
    res = pd.concat((distanceList, scaledData), axis= 1)
    return res

scaledSensor1Mean = concatScaledData(scaledSensor1Mean)
scaledSensor2Mean = concatScaledData(scaledSensor2Mean)
scaledSensor3Mean = concatScaledData(scaledSensor3Mean)
scaledSensor4Mean = concatScaledData(scaledSensor4Mean)
scaledSensor5Mean = concatScaledData(scaledSensor5Mean)
scaledSensor6Mean = concatScaledData(scaledSensor6Mean)

xTicks = [i for i in np.arange(10, 90, 10)]

fig, axs  = plt.subplots(2, 3, figsize= (12, 8))
yMinLimit = -1400
yMaxLimit = 50
yLimit = [yMinLimit, yMaxLimit]
fig.suptitle("Test1", fontweight= 'bold')
scaledSensor1Mean.plot.line(x= "distance", y= "s1", c= "red", ax= axs[0, 0], marker= "*", grid= True, xlim= [0, 90], ylim= yLimit, xticks= xTicks)
scaledSensor2Mean.plot.line(x= "distance", y= "s2", c= "orange", ax= axs[0, 1], marker= "^", grid= True, xlim= [0, 90], ylim= yLimit, xticks= xTicks)
scaledSensor3Mean.plot.line(x= "distance", y= "s3", c= "gold", ax= axs[0, 2], marker= "d", grid= True, xlim= [0, 90], ylim= yLimit, xticks= xTicks)
scaledSensor4Mean.plot.line(x= "distance", y= "s4", c= "green", ax= axs[1, 0], marker= "o", grid= True, xlim= [0, 90], ylim= yLimit, xticks= xTicks)
scaledSensor5Mean.plot.line(x= "distance", y= "s5", c= "blue", ax= axs[1, 1], marker= "v", grid= True, xlim= [0, 90], ylim= yLimit, xticks= xTicks)
scaledSensor6Mean.plot.line(x= "distance", y= "s6", c= "violet", ax= axs[1, 2], marker= "x", grid= True, xlim= [0, 90], ylim= yLimit, xticks= xTicks)

plt.show()
