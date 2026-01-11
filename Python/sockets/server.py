import socket 
from threading import Thread, active_count

Local_IPAddress = socket.gethostbyname(socket.gethostname())
PORT = 8080
ADDR = (Local_IPAddress, PORT)
MSG_BYTES = 20

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while KeyboardInterrupt:
        msg = conn.recv(MSG_BYTES)
        print(f"Client: {msg}")
        _ = input()
        conn.send(b"Message from server")

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONECTIONS] {active_count() - 1}")

print(f"[STARTING] server at {ADDR}")
start()