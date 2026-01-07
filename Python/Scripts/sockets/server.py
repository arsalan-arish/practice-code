import socket

server_socket = socket.socket()
server_socket.bind(('localhost',3000))
server_socket.listen(2)

print("Server is listening on port 3000...")

conn, addr = server_socket.accept()
print(f"Connected with {addr}")

while True:
    data = conn.recv(1024).decode(encoding='utf-8')
    if not data:
        break
    print("Client: ", data)
    conn.send(f"Recieved {data}".encode(encoding='utf-8'))

conn.close()