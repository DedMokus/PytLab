import socket

HOST = "127.0.0.1"
PORT = 22943

Mail = input("Input mail")
Text = input("Input text\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(f"{Mail}/{Text}")
    while True:
        data = s.recv(1024)
        if not data:
            break
    print(data)


