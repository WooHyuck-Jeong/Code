# 수신 코드 - 윈도우
import socket

# 서버 설정
HOST = "192.168.1.101"        # 모든 네트워크 인터페이스에서 연결 허용
PORT = 5000             # 포트 번호

# TCP 소켓 생성
server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server_socket.bind((HOST, PORT))
server_socket.listen(1)             # 하나의 클라이언트만 연결 허용

print(f"[SERVER] {PORT} 포트에서 데이터 수신 대기 중...")

conn, addr = server_socket.accept()
print(f"[SERVER] {addr}에서 연결됨.")

try:
    while True:
        data = conn.recv(1024).decode()     # 데이터 수신
        if not data:
            break
        print(f"[SERVER] 수신: {data}")
except KeyboardInterrupt:
    print("\n[SERVER] 종료")
finally:
    conn.close()
    server_socket.close()