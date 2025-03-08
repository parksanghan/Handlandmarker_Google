import socket

# 서버 설정
HOST = "0.0.0.0"  # 모든 인터페이스에서 연결 수락
PORT = 12345       # 사용할 포트 번호

# 소켓 생성 및 바인딩
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # 최대 대기 클라이언트 수

print(f"🚀 Python 서버 실행 중... (IP: {HOST}, PORT: {PORT})")

while True:
    client_socket, addr = server_socket.accept()
    print(f"✅ 클라이언트 {addr} 연결됨!")

    # 클라이언트로부터 메시지 수신
    data = client_socket.recv(1024).decode("utf-8")
    print(f"📩 받은 메시지: {data}")

    # 클라이언트에 응답 전송
    response = "서버에서 수신 완료!"
    client_socket.send(response.encode("utf-8"))

    # 연결 종료
    client_socket.close()
