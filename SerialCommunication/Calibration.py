import serial
import numpy as np
import pandas as pd

from CheckSerialPort import getPortList

# Serial Port 연결 및 객체 생성
portList = getPortList()
print(portList)

ser = serial.Serial(port= portList[0],
                    baudrate= 38400,
                    timeout= 1,
                    bytesize= 8)

############### Global Variables ###############
sensorIdx = [4, 9, 14, 20, 25, 30]


############### Data Measurement ###############
result = []
while len(result) < 16:
    data = ser.readline()
    receive = data.decode('utf-8')
    print(receive)

    if len(receive) > 41:
        pass
    else:
        result.append(receive)

############### Split data ###############
sensors = []
for i in sensorIdx:
    sensors.append([r[i : i + 5] for r in result])

sensors = np.array(sensors, dtype= np.float32).T        # (samples, sensor)

############### Calculate Mean ###############
sensors = pd.DataFrame(sensors, columns= [f's{i}' for i in np.arange(1, 7, 1)])
meanSensors = pd.DataFrame(sensors.mean(axis= 0))

############### Save Mean ###############
# meanSensors.to_csv("InitialSensor.csv", sep= ",")