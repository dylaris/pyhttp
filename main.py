import socket
import threading

class HTTPServer:
    def __init__(self, host="localhost", port=8888):
        self.host = host
        self.port = port
        self.sock = None

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"Server: running on {self.host}:{self.port}")

    def stop(self):
        if self.sock:
            self.sock.close()
            self.sock = None
        print("Server: stopped")

    def accept_request(self):
        client_socket, client_address = self.sock.accept()
        print(f"Client: {client_address[0]}:{client_address[1]} connected")
        client_thread = threading.Thread(
            target=self.handle_request,
            args=(client_socket, client_address)
        )
        client_thread.daemon = False
        client_thread.start()

    def handle_request(self, sock, addr):
        print(f"Server: processing {addr[0]}:{addr[1]}")
        while True:
            data = sock.recv(1024)
            if not data:
                break
            print(f"Server: receive: {data}")
        sock.close()
        print(f"Client: {addr[0]}:{addr[1]} disconnected")

if __name__ == "__main__":
    server = HTTPServer()
    server.start()
    while True:
        server.accept_request()
    server.stop()
