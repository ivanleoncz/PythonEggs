
import socket

s = socket.socket()
host = socket.gethostname()
port = 60333

s.connect((host, port))
print(s.recv(1024)) # Server Message
s.send(bytes("Client says: hi!", 'utf-8'))
s.close()
