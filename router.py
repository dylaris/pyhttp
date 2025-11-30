from handler import HTTPHandler

class HTTPRouter:
    def __init(self):
        self.routes = {}

    def add(self, path, handler):
        pass

    def route(self, req):
        handler = HTTPHandler()
        handler.process(req)
