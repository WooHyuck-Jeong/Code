import socket

# 수신할 포트 번호
UDP_IP = "0.0.0.0"      # 모든 네트워크 인터페이스에서 수신 허용
UDP_PORT = 5000       # 라즈베리파이 설정 포트와 동일하게 설정

# UDP 소켓 생성
sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sock.bind((UDP_IP, UDP_PORT))

print(f"포트 {UDP_PORT}에서 데이터 수신 대기 중...")

try:
    while True:
        data, addr = sock.recvfrom(1024)    # 최대 1024 바이트 수신
        print(f"수신 [{addr}]: {data.decode()}")
except KeyboardInterrupt:
    print("\n수신 종료")
finally:
    sock.close()