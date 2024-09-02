import os
import sys
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

if sys.platform == "win32":
    print("윈도우임")
    folderPath = "C:\\Users\\hyukk\\Desktop\\0809\\Test6\\result\\"
else:
    print("맥임")
    folderPath = "/Users/jwh/Desktop/0809/Test6/result/"

fileList = [file for file in sorted(glob.glob(folderPath + "*.csv")) if os.path.isfile(file)]

negativeSensor1 = []
positiveSensor1 = []
negativeSensor2 = []
positiveSensor2 = []
negativeSensor3 = []
positiveSensor3 = []
negativeSensor4 = []
positiveSensor4 = []
negativeSensor5 = []
positiveSensor5 = []
negativeSensor6 = []
positiveSensor6 = []

for file in fileList:
    name = file.split(f"{folderPath}")[1]
    name = name.split(".")[0]
    
    if name.startswith("s"):
        sensorNumber = name.split("_")[0]
        position = name.split("_")[1]
        distance = name.split("_")[2]
        
        if sensorNumber == "s1":
            if position == "n":
                data = pd.read_csv(file, sep= ",", usecols= [0], names= [f"n{distance}"], skiprows= 100, nrows= 2000)
                negativeSensor1.append(data)
            elif position == "p":
                data = pd.read_csv(file, sep= ",", usecols= [0], names= [f"p{distance}"], skiprows= 100, nrows= 2000)
                positiveSensor1.append(data)
        
        elif sensorNumber == "s2":
            if position == "n":
                data = pd.read_csv(file, sep= ",", usecols= [1], names= [f"n{distance}"], skiprows= 100, nrows= 2000)
                negativeSensor2.append(data)
            elif position == "p":
                data = pd.read_csv(file, sep= ",", usecols= [1], names= [f"p{distance}"], skiprows= 100, nrows= 2000)
                positiveSensor2.append(data)
                
        elif sensorNumber == "s3":
            if position == "n":
                data = pd.read_csv(file, sep= ",", usecols= [2], names= [f"n{distance}"], skiprows= 100, nrows= 2000)
                negativeSensor3.append(data)
            elif position == "p":
                data = pd.read_csv(file, sep= ",", usecols= [2], names= [f"p{distance}"], skiprows= 100, nrows= 2000)
                positiveSensor3.append(data)
                
        elif sensorNumber == "s4":
            if position == "n":
                data = pd.read_csv(file, sep= ",", usecols= [3], names= [f"n{distance}"], skiprows= 100, nrows= 2000)
                negativeSensor4.append(data)
            elif position == "p":
                data = pd.read_csv(file, sep= ",", usecols= [3], names= [f"p{distance}"], skiprows= 100, nrows= 2000)
                positiveSensor4.append(data)
                
        elif sensorNumber == "s5":
            if position == "n":
                data = pd.read_csv(file, sep= ",", usecols= [4], names= [f"n{distance}"], skiprows= 100, nrows= 2000)
                negativeSensor5.append(data)
            elif position == "p":
                data = pd.read_csv(file, sep= ",", usecols= [4], names= [f"p{distance}"], skiprows= 100, nrows= 2000)
                positiveSensor5.append(data)
                
        elif sensorNumber == "s6":
            if position == "n":
                data = pd.read_csv(file, sep= ",", usecols= [5], names= [f"n{distance}"], skiprows= 100, nrows= 2000)
                negativeSensor6.append(data)
            elif position == "p":
                data = pd.read_csv(file, sep= ",", usecols= [5], names= [f"p{distance}"], skiprows= 100, nrows= 2000)
                positiveSensor6.append(data)


negativeSensor1 = pd.concat(negativeSensor1, axis= 1)
positiveSensor1 = pd.concat(positiveSensor1, axis= 1)
negativeSensor2 = pd.concat(negativeSensor2, axis= 1)
positiveSensor2 = pd.concat(positiveSensor2, axis= 1)
negativeSensor3 = pd.concat(negativeSensor3, axis= 1)
positiveSensor3 = pd.concat(positiveSensor3, axis= 1)
negativeSensor4 = pd.concat(negativeSensor4, axis= 1)
positiveSensor4 = pd.concat(positiveSensor4, axis= 1)
negativeSensor5 = pd.concat(negativeSensor5, axis= 1)
positiveSensor5 = pd.concat(positiveSensor5, axis= 1)
negativeSensor6 = pd.concat(negativeSensor6, axis= 1)
positiveSensor6 = pd.concat(positiveSensor6, axis= 1)

sensor1 = pd.concat((negativeSensor1, positiveSensor1), axis= 1)
sensor2 = pd.concat((negativeSensor2, positiveSensor2), axis= 1)
sensor3 = pd.concat((negativeSensor3, positiveSensor3), axis= 1)
sensor4 = pd.concat((negativeSensor4, positiveSensor4), axis= 1)
sensor5 = pd.concat((negativeSensor5, positiveSensor5), axis= 1)
sensor6 = pd.concat((negativeSensor6, positiveSensor6), axis= 1)

sensors = [sensor1, sensor2, sensor3, sensor4, sensor5, sensor6]

base123 = pd.read_csv(fileList[0], sep= ",", usecols= [0, 1, 2], nrows= 2000)
base123Mean = base123.mean(axis= 0)

base456 = pd.read_csv(fileList[1], sep= ",", usecols= [3, 4, 5], nrows= 2000)
base456Mean = base456.mean(axis= 0)

baseMean = pd.concat((base123Mean, base456Mean), axis= 0)

scaledSensors = [sensors[i] - baseMean.iloc[i] for i in range(len(sensors))]

fig, axs = plt.subplots(2, 3, figsize= (20, 18))
for i, ax in enumerate(axs.flat):
    scaledSensors[i].plot(kind= "line", 
                          ax= ax, 
                          title= f"Sensor {i+1}", 
                          grid= True,
                          ylim= [-2400, 2400]
                          )
plt.subplots_adjust(hspace= 0.4, wspace= 0.4)
plt.show()