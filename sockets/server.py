
import socket

HOST = socket.gethostname()
PORT = 60333
BUFFER_SIZE = 32

try:

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"[INFO]: listening on {HOST}:{PORT}")

    while True:

        connection, addr = server.accept()
        print(f"[INFO]: connection from {addr}")

        while True:
            data = connection.recv(BUFFER_SIZE).decode("utf-8")
            if data:
                print(f"[INFO]: data received : ", data)
                connection.send("server: message received!".encode("utf-8"))
                if data in ('terminate', 'bye', ):
                    print("[INFO]: connection terminated by client!")
                    break
                else:
                    print("[INFO]: waiting for more messages...")

        connection.close()


except KeyboardInterrupt:
    print("[INFO] server shutdown!")