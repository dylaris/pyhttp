from response import HTTPResponse

class HTTPHandler:
    def __init__(self):
        pass

    def dead(self, ctx):
        return HTTPResponse(404, "SOMETHING WRONG OCCURS!")

    def home(self, ctx):
        with open("webroot/index.html", "r") as f:
            html = f.read()
            return HTTPResponse(200, html)

    def login(self, ctx):
        if ctx["request"].method == "GET":
            with open("webroot/login.html", "r") as f:
                html = f.read()
                return HTTPResponse(200, html)
        elif ctx["request"].method == "POST":
            username = ctx["request"].get_form_data("username")
            password = ctx["request"].get_form_data("password")
            print(f"Login attempt: {username}, {password}")
            if username == ctx["username"] and password == ctx["password"]:
                ctx["login"] = True
                return HTTPResponse(200, "<h1>Login Success!</h1>")
            else:
                ctx["login"] = False
                return HTTPResponse(401, "<h1>Login Failed!</h1>")
