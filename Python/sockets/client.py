import socket

PORT = 8080
LOCALIP = socket.gethostbyname(socket.gethostname())
ADDR = (LOCALIP, PORT)

s = socket.socket()
s.connect(ADDR)


s.send(b"Hello from client")
while KeyboardInterrupt: 
    r = s.recv(100).decode()
    print(r)
    x = input()
    s.send("Hello from client".encode())
