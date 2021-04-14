import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((socket.gethostname(), 9999))

name = input("Enter your name: ")
c.send(bytes(name,"utf-8"))

print(c.recv(1024).decode())



