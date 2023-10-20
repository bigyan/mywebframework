# Send a valid HTTP/1.1 response

import socket

HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 12345

DB = {
    'name':'Ram'
}

ROUTES = {
    '/': f'Welcome to our raw HTTP server, {DB["name"]}!\n',
    '/info': 'This is the info page.\n',
    '/login': 'Please provide login credentials.\n'
}

def extract_verb_and_path(request):
    """Extract HTTP verb and URL path from an HTTP request."""
    lines = request.splitlines()
    if lines:
        parts = lines[0].split()
        if len(parts) >= 2:
            verb, path = parts[0], parts[1]
            return verb, path
    return None, None

def create_http_response(body):
    """Create a valid HTTP/1.1 response."""
    headers = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {}\r\n\r\n".format(len(body))
    return headers + body

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
                
                body = ROUTES.get(path, "404 Not Found")
                response = create_http_response(body)
                conn.sendall(response.encode('utf-8'))

