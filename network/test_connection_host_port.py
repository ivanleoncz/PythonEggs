
import socket

def check_connection(address, port):
    """ Test connection for specific host and port. """

    assert type(address) == str, "address -> must be a string"
    assert type(port) == int, "port -> must be an integer"

    s = socket.socket()
    try:
        s.connect((address, port))
        return True
    except Exception:
        return False
    finally:
        s.close()


host = "127.0.0.1"
port = 27017

if check_connection(host, port):
    print("Connection OK")
else:
    print("Connection: NOK")
