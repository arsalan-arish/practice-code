import socket

MSG_BYTES = 20
Local_IPAddress = socket.gethostbyname(socket.gethostname())
PORT = 8080

client = socket.socket()
client.connect((Local_IPAddress, PORT))
while KeyboardInterrupt:
    _ = input()
    client.send(b'Message from client')
    msg = client.recv(MSG_BYTES)
    print(f"Server: {msg}")