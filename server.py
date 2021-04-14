import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

s.bind((socket.gethostname(), 9999))

s.listen(5)
print("Waiting for the connection...")



while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with ", addr, name)

    c.send(bytes('Message from server', 'utf-8'))

    c.close()