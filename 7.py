import socket

class WebServer:
    def __init__(self):
        self.routes = {}  # URL to view function mapping
    
    def route(self, path):
        def decorator(f):
            self.routes[path] = f
            return f
        return decorator

    def serve(self, host='127.0.0.1', port=4000):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            print(f"Serving on http://{host}:{port}")
            while True:
                conn, addr = s.accept()
                with conn:
                    request = conn.recv(1024).decode('utf-8')
                    # Get the request path (very naive way for simplicity)
                    path = request.split(' ')[1]

                    # If path in routes, call the associated function
                    if path in self.routes:
                        response = f"HTTP/1.1 200 OK\n\n{self.routes[path]()}".encode('utf-8')
                    else:
                        response = "HTTP/1.1 404 Not Found\n\nNot Found".encode('utf-8')

                    conn.sendall(response)

app = WebServer()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/hello')
def hello():
    return "Hello from another path!"

if __name__ == '__main__':
    app.serve()
