class HTTPResponse:
    def __init__(self, sock):
        self.sock = sock

    def send(self, status_code, status_text, body, content_type="text/plain"):
        response = f"HTTP/1.1 {status_code} {status_text}\r\n"
        response += f"Content-Type: {content_type}\r\n"
        response += f"Content-Length: {len(body)}\r\n"
        response += "Connection: close\r\n"
        response += "\r\n"
        response += body
        self.sock.sendall(response.encode("utf-8"))

    def report(self, status_code, message):
        body = f"""<html>
        <body>
            <h1>{status_code} Error</h1>
            <p>{message}</p>
        </body>
        </html>
        """
        self.sock.send(status_code, message, body, "text/html")
