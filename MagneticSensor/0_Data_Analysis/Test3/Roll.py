import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로 설정 (실제 경로로 변경하세요)
folderPath = "/Users/jwh/Desktop/0720/MagneticTest/Test3/"
fileList = sorted(glob.glob(folderPath + "*"))

colName = "col"

roll = pd.read_table(fileList[1], names=[colName])
roll = roll.iloc[:, 0].str[-39:]
roll = pd.DataFrame(roll, columns=[colName])

s1 = roll[colName].str[4:9]
s2 = roll[colName].str[9:14]
s3 = roll[colName].str[14:19]
s4 = roll[colName].str[20:25]
s5 = roll[colName].str[25:30]
s6 = roll[colName].str[30:35]

res = pd.concat((s1, s2), axis=1)
res = pd.concat((res, s3), axis=1)
res = pd.concat((res, s4), axis=1)
res = pd.concat((res, s5), axis=1)
res = pd.concat((res, s6), axis=1)

colList = [f"s{i+1}" for i in range(6)]

res.columns = colList

roll = res.copy()
roll = roll.astype(dtype='int64')

# 데이터 불러오기
data = roll.copy()

# 데이터 확인
print(data.shape)  # (3571, 6) 확인

# 초기 설정
plt.ion()  # 인터랙티브 모드 켜기
fig, axs = plt.subplots(3, 2, figsize=(15, 10))
colors = ["red", "orange", "gold", "green", "blue", "violet"]
lines = []

# 초기 플롯 설정
for i, ax in enumerate(axs.flat):
    line, = ax.plot([], [], label=f'Sensor {i + 1}', color=colors[i])
    lines.append(line)
    ax.legend()
    ax.grid()
    ax.set_xlabel("time")
    ax.set_ylabel("Value")
    ax.set_title(f"Sensor {i + 1} Data")

# 데이터를 저장할 리스트 초기화
idx = []
sensor_data = [[] for _ in range(data.shape[1])]

# 그래프 업데이트 함수
def update_plot():
    for i, ax in enumerate(axs.flat):
        lines[i].set_xdata(idx)
        lines[i].set_ydata(sensor_data[i])
        ax.relim()
        ax.autoscale_view()

# 데이터 플로팅
for i in range(data.shape[0]):
    idx.append(i)
    for j in range(data.shape[1]):
        sensor_data[j].append(data.iloc[i, j])
    update_plot()
    plt.pause(0.01)  # 잠시 멈추어 업데이트 시간을 줍니다

plt.ioff()  # 인터랙티브 모드 끄기
plt.tight_layout()
plt.show()