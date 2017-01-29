import socket

s = socket.socket()

s.connect((socket.gethostname(), 12345))

print s.recv(1)

s.close()
