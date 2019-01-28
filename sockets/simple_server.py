
import socket

s = socket.socket()
host = socket.gethostname()
port = 60333
s.bind((host, port))
s.listen(30)

while True:
    c, addr = s.accept()
    print("Connection Status: ", addr)
    c.send(bytes("Server says: hello!", 'utf-8'))
    c.close()
