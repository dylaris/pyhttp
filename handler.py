from request import HTTPRequest
from response import HTTPResponse

class HTTPHandler:
    def __init__(self):
        pass

    def process(self, req):
        resp = HTTPResponse(req.sock)

        if req.method.upper() == "GET":
            resp.send(200, "OK", f"Server received:\n\n{req}")
        else:
            resp.report(501, f"Not support method {req.method.upper()} yet.")
