class HTTPResponse:
    def __init__(self, status_code, body="", content_type="text/html"):
        self.status_code = status_code
        self.body = body
        self.headers = {
            "Content-Type": content_type,
            "Content-Length": str(len(body.encode("utf-8")))
        }

    def to_bytes(self):
        status_text = {
            200: "OK",
            404: "Not Found",
            500: "Internal Server Error"
        }

        response_line = f"HTTP/1.1 {self.status_code} {status_text.get(self.status_code, 'Unknown')}\r\n"

        headers = ""
        for key, value in self.headers.items():
            headers += f"{key}: {value}\r\n"

        return (response_line + headers + "\r\n" + self.body).encode("utf-8")
