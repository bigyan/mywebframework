# Extract HTTP Verb and Path

import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345

def extract_verb_and_path(request):
    """Extract HTTP verb and URL path from an HTTP request."""
    lines = request.splitlines()
    if lines:
        parts = lines[0].split()
        if len(parts) >= 2:
            verb, path = parts[0], parts[1]
            return verb, path
    return None, None

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
                request = data.decode('utf-8')
                print(f"Received from {addr}: {request}")

                verb, path = extract_verb_and_path(request)
                if verb and path:
                    print(f"HTTP Verb: {verb}, URL Path: {path}")

            conn.sendall(b'Hello, World!')
