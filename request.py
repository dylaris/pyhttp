import urllib.parse

class HTTPRequest:
    def __init__(self, sock):
        self.sock = sock
        # request line
        self.method = None
        self.path = None
        self.query_params = {}
        self.version = None
        # request headers
        self.headers = {}
        # request body
        self.body = None

    def parse(self):
        self.data = self.sock.recv(1024).decode("utf-8") # may overflow
        self._parse_request_line()
        self._parse_request_headers()
        self._parse_request_body()

    def get_header(self, name):
        return self.headers.get(name.lower())

    def get_query_param(self, name):
        return self.query_params.get(name)

    def _parse_request_line(self):
        lines = self.data.split("\r\n", 1)
        request_line = lines[0]
        method, path, version = request_line.split(" ")
        url_parts = path.split("?", 1)
        self.method = method
        self.version = version
        self.path = url_parts[0]
        query_string = url_parts[1] if len(url_parts) > 1 else ""
        if query_string:
            pairs = query_string.split("&")
            for pair in pairs:
                if "=" in pair:
                    # k1=v1&k2=v2
                    key, val = pair.split("=", 1)
                    key = urllib.parse.unquote(key)
                    val = urllib.parse.unquote(val)
                    self.query_params[key] = val
                else:
                    # k1&k2=v2
                    key = urllib.parse.unquote(key)
                    self.query_params[key] = ""

    def _parse_request_headers(self):
        lines = self.data.split("\r\n")
        for i in range(1, len(lines)):
            line = lines[i]
            if line == "":
                break
            if ": " in line:
                key, val = line.split(": ")
                self.headers[key.lower()] = val

    def _parse_request_body(self ):
        parts = self.data.split("\r\n\r\n", 1)
        if len(parts) > 1:
            self.body = parts[1]
            content_length = self.get_header("content-length")
            if content_length:
                self.body = self.body[:int(content_length)]

    def __str__(self):
        result = f"{self.method} {self.path} {self.version}\n"
        result += "Headers:\n"
        for key, val in self.headers.items():
            result += f"  {key}: {val}\n"
        if self.query_params:
            result += "Query Parameters:\n"
            for key, val in self.query_params.items():
                result += f"  {key}: {val}\n"
        if self.body:
            result += f"Body: {self.body}\n"
        return result
