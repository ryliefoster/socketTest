import socket

HOST = "127.0.0.1"
PORT = 34671

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            conn.sendall(data)
            conn, addr = s.accept()
