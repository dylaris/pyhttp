from response import HTTPResponse

class HTTPHandler:
    def __init__(self):
        pass

    def dead(self, ctx):
        return HTTPResponse(404, "SOMETHING WRONG OCCURS!")

    def css(self, ctx):
        with open("webroot/style.css", "r", encoding="utf-8") as f:
            return HTTPResponse(200, f.read(), "text/css")

    def home(self, ctx):
        with open("webroot/home.html", "r", encoding="utf-8") as f:
            return HTTPResponse(200, f.read())

    def blog(self, ctx):
        with open("webroot/blog.html", "r", encoding="utf-8") as f:
            return HTTPResponse(200, f.read())

    def login(self, ctx):
        if ctx["request"].method == "GET":
            with open("webroot/login.html", "r", encoding="utf-8") as f:
                html = f.read()
                return HTTPResponse(200, html)
        elif ctx["request"].method == "POST":
            username = ctx["request"].get_form_data("username")
            password = ctx["request"].get_form_data("password")
            if username == ctx["username"] and password == ctx["password"]:
                ctx["login"] = True
                with open("webroot/home.html", "r", encoding="utf-8") as f:
                    return HTTPResponse(200, f.read())
            else:
                ctx["login"] = False
                with open("webroot/failure.html", "r", encoding="utf-8") as f:
                    return HTTPResponse(200, f.read())
