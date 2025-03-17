import socket
import time

# 수신(노트북)의 IP 주소와 포트 번호
UDP_IP = "192.168.0.132"        # 윈도우 노트북의 실제 IP 주소 입력
UDP_PORT = 5000                 # 사용할 포트 번호

# UDP 소켓 생성
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

data = 101
try:
    while True:
        message = str(data).encode()
        sock.sendto(message, (UDP_IP, UDP_PORT))
        print(f"Send: $000-0740-0664+0027,+0989+0571+{data},1,0")
        data += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\n송신 종료")
finally:
    sock.close()