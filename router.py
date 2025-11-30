import logging

logger = logging.getLogger(__name__)

class HTTPRouter:
    def __init__(self):
        self.routes = {}

    def add(self, path, handler):
        self.routes[path] = handler

    def route(self, req):
        print(req)
        query_path = req.path
        if query_path not in self.routes:
            query_path = "__invalid__"
        handler = self.routes[query_path]
        resp = handler(req)
        return resp
