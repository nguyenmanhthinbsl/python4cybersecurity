import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"

port = 9002

server.connect((host,port))

while True:
    msg = server.recv(1024).decode()
    if not msg:
        break
    print(msg)
    data = input("enter a msg: ")
    server.sendall(str.encode(data))
    
server.close()    