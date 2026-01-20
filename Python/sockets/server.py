import socket

PORT = 8080
LOCALIP = socket.gethostbyname(socket.gethostname())
ADDR = (LOCALIP, PORT)

s = socket.socket()
s.bind(ADDR)
s.listen()
conn, addr = s.accept()

while KeyboardInterrupt: 
    r = conn.recv(100).decode()
    print(r)
    x = input()
    conn.send("Hello from server".encode())

conn.close()