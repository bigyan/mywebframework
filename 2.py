# Print all incoming requests

import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print(f"Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            # Receive data from the client
            data = conn.recv(1024)
            if data:
                print(f"Received from {addr}: {data.decode('utf-8')}")

            conn.sendall(b'Hello, World!')
