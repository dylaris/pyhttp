import logging
import socket
import threading
from request import HTTPRequest
from router import HTTPRouter
from handler import HTTPHandler

logger = logging.getLogger(__name__)

class HTTPServer:
    def __init__(self, host="localhost", port=8888):
        self.host = host
        self.port = port
        self.sock = None
        self.router = HTTPRouter()
        self.handler = HTTPHandler()
        self.login = False

        self.setup_account("aris", "aris")
        self.setup_routes()

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

        ctx = {
            "username": self.username,
            "password": self.password,
            "login": self.login,
            "request": req
        }

        resp = self.router.route(ctx)
        sock.sendall(resp.to_bytes())

        self.login = ctx["login"]

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

    def setup_routes(self):
        self.router.add("GET", "/", self.handler.home)
        self.router.add("GET", "/login", self.handler.login)
        self.router.add("POST", "/login", self.handler.login)
        self.router.add("GET", "/dead", self.handler.dead)

    def setup_account(self, name, passwd):
        self.username = name
        self.password = passwd

