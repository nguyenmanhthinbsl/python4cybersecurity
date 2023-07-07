import socket

server =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host =  "127.0.0.1" #or localhost
port = 9002 

server.bind((host,port))

server.listen()

client, addr =  server.accept()

print(f"connection receive from address {addr}")

while True:
    data = input("enter a msg:")
    client.sendall(str.encode(data))
    msg = client.recv(1024).decode()
    if not msg:
        break
    print(msg)
client.close()   