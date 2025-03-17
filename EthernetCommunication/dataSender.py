import socket
import time

# 수신(노트북)의 IP 주소와 포트 번호
UDP_IP = "192.168.1.100"        # 윈도우 노트북의 실제 IP 주소 입력
UDP_PORT = 5000                 # 사용할 포트 번호

# UDP 소켓 생성
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

count = 1
try:
    while True:
        message = str(count).encode()
        sock.sendto(message, (UDP_IP, UDP_PORT))
        print(f"Send: {count}")
        count += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("\n송신 종료")
finally:
    sock.close()