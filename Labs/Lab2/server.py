import socket

s = socket.socket()
host = "127.0.0.1"
port = 12345
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Connection from %s" %(addr,))
    print(c.recv(128).decode("utf-8"))
    c.close()
    