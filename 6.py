import socket

HOST = '0.0.0.0'
PORT = 12345
ROUTES = {
    '/': 'Welcome to our raw HTTP server!',
    '/info': 'This is the info page.',
    '/login': 'Please provide login credentials.'
}

def extract_request_path(request):
    """Extract the request path from the HTTP request."""
    lines = request.split('\n')
    if lines:
        parts = lines[0].split(' ')
        if len(parts) > 1:
            return parts[1]
    return None


class SimpleServer:
    def __init__(self):
        pass

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            print(f"Listening on {HOST}:{PORT}")
            while True:
                conn, addr = s.accept()
                with conn:
                    ip_address = addr[0]

                    data = conn.recv(1024)
                    if data:
                        request = data.decode('utf-8')

                        # Add the server logic here...
                        path = extract_request_path(request)
                        if path in ROUTES:
                            response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(ROUTES[path])}\r\n\r\n{ROUTES[path]}"
                            conn.sendall(response.encode('utf-8'))
                        else:
                            response = "HTTP/1.1 404 Not Found\r\nContent-Length: 9\r\n\r\nNot Found"
                            conn.sendall(response.encode('utf-8'))

if __name__ == "__main__":
    server = SimpleServer()
    server.run()
