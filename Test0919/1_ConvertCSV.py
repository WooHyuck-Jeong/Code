import os
import sys
import glob
import numpy as np
import pandas as pd

def makeDirectory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName, exist_ok= True)

if sys.platform == "darwin":
    folderPath = "/Users/jwh/Desktop/0913/Test2/"
elif sys.platform == "win32":
    folderPath = "C:/Users/hyukk/Desktop/0913/Test2/"

files = [file for file in sorted(glob.glob(folderPath + "*"))]

# for i in range(len(files)):
#     print(files[i])
#     print(i)
#     print('-----------')

resultPath = folderPath + "result/"
makeDirectory(resultPath)

# Global Variables
col_name = "col"
sensor_names = [f"s{i}" for i in np.arange(1, 7, 1)]
skip_number = 300
use_number = 4000
class_idx = [0, 11, 20, 21, 22, 23, 24, 25, 26, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19]

class_folder = [files[i] for i in class_idx]

def makeCSV(class_folder, save_path):
    class_data = sorted(glob.glob(class_folder + "/*"))

    for file in class_data:
        df = pd.read_table(file, names= [col_name], skiprows= skip_number, nrows= use_number)
        df = df.iloc[:, 0].str[-39:]
        df = pd.DataFrame(df, columns= [col_name])

        s1 = df[col_name].str[4:9]
        s2 = df[col_name].str[9:14]
        s3 = df[col_name].str[14:19]
        s4 = df[col_name].str[20:25]
        s5 = df[col_name].str[25:30]
        s6 = df[col_name].str[30:35]

        res = [s1, s2, s3, s4, s5, s6]
        res = pd.concat(res, axis= 1)

        res.columns = sensor_names

        save_file_name = file[-9:] + ".csv"

        res.to_csv(save_path + save_file_name, index= False)

for c in class_folder:
    makeCSV(c, save_path= resultPath)

if sys.platform == "darwin":
    base_path = "/Users/jwh/Desktop/0913/base"
elif sys.platform == "win32":
    base_path = ""

base = pd.read_table(base_path, names= [col_name], skiprows= skip_number, nrows= use_number)
base = base.iloc[:, 0].str[-39:]
base = pd.DataFrame(base, columns= [col_name])

b1 = base[col_name].str[4:9]
b2 = base[col_name].str[9:14]
b3 = base[col_name].str[14:19]
b4 = base[col_name].str[20:25]
b5 = base[col_name].str[25:30]
b6 = base[col_name].str[30:35]

res = [b1, b2, b3, b4, b5, b6]
base = pd.concat(res, axis= 1)
base.columns = sensor_names

base.to_csv(resultPath + "base.csv", index= False)