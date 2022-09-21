# TCPhost.py

import socket

HOST = "192.168.40.45"  # Standard loopback interface address (localhost)
PORT = 42069  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Opening server on IP", HOST, "and port", PORT)
    s.bind((HOST, PORT))
    while (True):
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Got connection from {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                #conn.sendall(data)
                conn.sendall(b"Kiva tietaa nain kolmelta aamuyosta")
