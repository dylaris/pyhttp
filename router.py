import logging

logger = logging.getLogger(__name__)

class HTTPRouter:
    def __init__(self):
        self.routes = {}

    def add(self, method, path, handler):
        if method not in self.routes:
            self.routes[method] = {}
        self.routes[method][path] = handler

    def valid(self, method, path):
        if method not in self.routes or path not in self.routes[method]:
            return False
        else:
            return True

    def route(self, ctx):
        if not self.valid(ctx["request"].method, ctx["request"].path):
            ctx["request"].method = "GET"
            ctx["request"].path = "/dead"

        handler = self.routes[ctx["request"].method][ctx["request"].path]
        resp = handler(ctx)
        return resp
