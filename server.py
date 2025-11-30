import logging
import socket
import threading
from request import HTTPRequest
from router import HTTPRouter
from handler import BlogHandler

logger = logging.getLogger(__name__)

class HTTPServer:
    def __init__(self, host="localhost", port=8888):
        self.host = host
        self.port = port
        self.sock = None
        self.router = HTTPRouter()
        self.handler = BlogHandler()

        self.register("__invalid__", self.handler.invalid)
        self.register("/", self.handler.home)

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        logger.info(f"Starting HTTP server on http://{self.host}:{self.port}")
        logger.info(f"Server listening on port {self.port}...")

    def stop(self):
        if self.sock:
            self.sock.close()
            self.sock = None
        logger.info("Server stopped")

    def process(self, sock, host, port):
        req = HTTPRequest(sock)
        req.parse()
        resp = self.router.route(req)
        sock.sendall(resp.to_bytes())
        sock.close()
        logger.info(f"Client {host}:{port} disconnected")

    def wait(self):
        client_socket, client_address = self.sock.accept()
        host, port = client_address[0], client_address[1]

        logger.info(f"Client {host}:{port} connected")
        logger.info(f"Server processing {host}:{port}")

        client_thread = threading.Thread(
            target=self.process,
            args=(client_socket, host, port,)
        )
        client_thread.daemon = True
        client_thread.start()

    def register(self, path, handler):
        self.router.add(path, handler)
