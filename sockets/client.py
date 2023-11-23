
import socket

HOST = socket.gethostname()
PORT = 60333

with socket.socket() as client:

    client.connect((HOST, PORT))

    while True:
        message = input("\n[INFO]: type message > ")
        client.send(message.encode("utf-8"))
        print("[INFO]: server reply => ", client.recv(1024).decode("utf-8"))
        if message in ('terminate', 'bye', ):
            break

    print("[INFO]: connection terminated by client!")
    client.close()
