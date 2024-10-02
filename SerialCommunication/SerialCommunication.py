import time
import serial
import threading
import numpy as np

from pyts.image import GramianAngularField
from CheckSerialPort import getPortList
from keras.models import load_model

# Serial Port 연결 및 객체 생성
portList = getPortList()
print(portList)

ser = serial.Serial(port= portList[0],
                    baudrate= 38400,
                    timeout= 1,
                    bytesize= 8)


############### Global Variables ###############
sensorIdx = [4, 9, 14, 20, 25, 30]                      # 센서별 slicing index
gaf = GramianAngularField(method= 'difference')         # 이미지 인코딩 객체
trainedModel = load_model("")                           # 학습 모델 --> 모델 경로 입력

run = True                                              # 실행 제어 플래그 --> 추후 수정 필요


############### Method ###############
def execute_command():
    """
        데이터 계측 실행 명령어
    """
    global run
    run = True

def stop_command():
    """
        데이터 계측 종료 명령어
    """
    global run
    run = False

def userInputListener():
    """
        사용자 입력 비동기 처리 함수
    """
    global run
    while run:
        userInput = input("Enter 'q' to stop: ")
        if userInput == 'q':
            stop_command()


############### 입력 Thread 시작 ###############
inputThread = threading.Thread(target= userInputListener)
inputThread.start()


############### 데이터 계측 및 예측 ###############
predictResult = []

while run:
    result = []                                                 # 수신 데이터 저장 배열 초기화

    while len(result) < 16:                                     # 수신 데이터 개수 16개 될때까지 실행
        data = ser.readline()                                   # ser 객체를 통해 데이터 읽기
        receive = data.decode('utf-8')                          # 수신한 데이터 utf-8로 변환
        print(receive)

        # 중간에 데이터 겹쳐 수신하는 경우 제외
        if len(receive) > 41:                                   # 수신 데이터의 길이 > 41인 경우
            pass
        else:                                                   # 수신 데이터의 길이 =< 41인 경우
            result.append(receive)                              # result 배열에 수신 데이터 저장

    sensors = []                                                # 수신받은 데이터 센서별로 분리하여 저장
    for i in sensorIdx:
        sensors.append([r[i : i + 5] for r in result])          # sensorIdx에 저장된 idx에 따라 센서별 수신 데이터 저장

    sensors = np.array(sensors, dtype= np.float32).T            # 수신받은 데이터 (samples, sensor) 형태로 저장 ==> (sample, 6) 형태

    encodeSensor = []                                           # 인코딩 결과 저장 리스트

    for i in range(6):                                          # 센서 데이터 이미지 인코딩센서의 개수: 6
        s = sensors[:, i].reshape(-1, 1)
        e = gaf.fit_transform(s.T).reshape(16, 16, 1)
        encodeSensor.append(e)                                  # 인코딩된 데이터 저장
    
    ############### 인코딩된 이미지 병합(concatenate) ###############
    concated = np.concatenate(encodeSensor, axis= 2).reshape(1, 16, 16, 6)
    print(concated.shape)

    ############### 학습된 모델을 통해 드로그 위치 예측 ###############
    predictClass = np.argmax(trainedModel.predict(concated), axis= 1)
    predictResult.append(predictClass)
    print(predictClass)

############### 입력 Thread 종료될 때까지 대기 ###############
inputThread.join()