import os 
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# baseFilePath = "/Users/jwh/Desktop/0730/Test3/result/Base456.csv"
baseFilePath = "/Users/jwh/Documents/KOTC/수중도킹/2024년도/6_자기장센서 시험/Test0730_전달/Test3/result/Base456.csv"

# movingFilePath = "/Users/jwh/Desktop/0730/Test4/result/Moving456.csv"
movingFilePath = "/Users/jwh/Documents/KOTC/수중도킹/2024년도/6_자기장센서 시험/Test0730_전달/Test4/result/Moving456.csv"

colName = "col"
useCols = [3, 4, 5]
sensorName = [f"s{i}" for i in np.arange(4, 7, 1)]

base = pd.read_csv(baseFilePath, sep= ",", usecols= useCols)
meanBase = pd.DataFrame(base.mean(axis= 0).T.to_numpy().reshape(1, 3), columns= sensorName)

moving = pd.read_csv(movingFilePath, sep= ",", usecols= useCols)

s4 = (moving.iloc[:, 0] - meanBase.iloc[0, 0]).to_frame()
s5 = (moving.iloc[:, 1] - meanBase.iloc[0, 1]).to_frame()
s6 = (moving.iloc[:, 2] - meanBase.iloc[0, 2]).to_frame()

res = pd.concat((s4, s5), axis= 1)
res = pd.concat((res, s6), axis= 1)

res.plot(kind= "line")
plt.show()