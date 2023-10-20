# Basic Socket Server

import socket

HOST = '0.0.0.0'  # Listen on all interfaces
# 127.0.0.1
# 0.0.0.0
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            conn.sendall(b'Hello, World!')

# AF_INET, AF_UNIX
# SOCK_STREAM (TCP), SOCK_DGRAM (UDP), SOCK_RAW
