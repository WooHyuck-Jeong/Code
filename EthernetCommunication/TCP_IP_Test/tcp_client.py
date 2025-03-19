# 데이터 송신 코드 - 라즈베리파이 4
import socket, time

# 윈도우와 IP, 포트 설정
SERVER_IP = "192.168.0.157"     # 윈도우 노트북의 실제 IP 주소
PORT = 5000                     # 서버에서 설정한 포트

# TCP 소켓 생성 및 연결
client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client_socket.connect((SERVER_IP, PORT))

print(f"[CLIENT] {SERVER_IP}: {PORT} 서버에 연결됨.")

count = 1
try:
    while True:
        msg = str(f"$000-938-0290+0500,+0192-0258+{count},1,0").encode()        # 숫자를 문자열로 변환 후 바이트로 인코딩
        client_socket.sendall(msg)                                              # 데이터 전송
        print(f"[CLIENT] 전송: {str(msg)}")
        count += 1
        time.sleep(1)       # 1초 대기
        time.sleep(1)
except KeyboardInterrupt:
    print("\n[CLIENT] 종료")
finally:
    client_socket.close()
