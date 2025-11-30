from response import HTTPResponse

class BlogHandler:
    def __init__(self):
        self.posts = [
            {
                "id": 1,
                "title": "Welcome to My Blog",
                "content": "This is my first blog post!"
            },
            {
                "id": 2,
                "title": "Python HTTP Server",
                "content": "Learning how to build HTTP server with Python."
            }
        ]

    def invalid(self, req):
        return HTTPResponse(404, "invalid path")

    def home(self, req):
        html = """
        <html>
        <head><title>My Blog</title></head>
        <body>
            <h1>My Blog</h1>
            <div>
                <a href="/">Home</a>
                <a href="/posts">Posts</a>
                <a href="/new">New Post</a>
            </div>
            <h2>Recent Posts:</h2>
        """

        for post in self.posts[-2:]:
            html += f"""
            <div style="border:1px solid #ccc; padding:10px; margin:10px;">
                <h3>{post['title']}</h3>
                <p>{post['content'][:50]}...</p>
                <a href="/post/{post['id']}">Read More</a>
            </div>
            """

        html += "</body></html>"

        return HTTPResponse(200, html)

    def all_posts(self, request):
        html = """
        <html>
        <head><title>All Posts</title></head>
        <body>
            <h1>All Posts</h1>
            <div>
                <a href="/">Home</a>
                <a href="/posts">Posts</a>
                <a href="/new">New Post</a>
            </div>
        """

        for post in reversed(self.posts):
            html += f"""
            <div style="border:1px solid #ccc; padding:10px; margin:10px;">
                <h3>{post['title']}</h3>
                <p>{post['content']}</p>
            </div>
            """

        html += "</body></html>"

        return HTTPResponse(200, html)

    def post_detail(self, request):
        post_id = int(request.path.split('/')[-1])

        for post in self.posts:
            if post['id'] == post_id:
                html = f"""
                <html>
                <head><title>{post['title']}</title></head>
                <body>
                    <div>
                        <a href="/">Home</a>
                        <a href="/posts">Posts</a>
                        <a href="/new">New Post</a>
                    </div>
                    <h1>{post['title']}</h1>
                    <p>{post['content']}</p>
                    <a href="/posts">Back to Posts</a>
                </body>
                </html>
                """
                return HTTPResponse(200, html)

        return HTTPResponse(404)

    def new_post_form(self, request):
        html = """
        <html>
        <head><title>New Post</title></head>
        <body>
            <div>
                <a href="/">Home</a>
                <a href="/posts">Posts</a>
                <a href="/new">New Post</a>
            </div>
            <h1>Write New Post</h1>
            <form method="POST" action="/new">
                <div>
                    <label>Title:</label><br>
                    <input type="text" name="title" required>
                </div>
                <div>
                    <label>Content:</label><br>
                    <textarea name="content" rows="5" required></textarea>
                </div>
                <button type="submit">Publish</button>
            </form>
        </body>
        </html>
        """
        return HTTPResponse(200, html)

    def create_post(self, request):
        import urllib.parse
        form_data = urllib.parse.parse_qs(request.body)

        title = form_data.get('title', [''])[0]
        content = form_data.get('content', [''])[0]

        resp = HTTPResponse(req.sock)
        if title and content:
            new_id = max([p['id'] for p in self.posts], default=0) + 1
            new_post = {
                "id": new_id,
                "title": title,
                "content": content
            }
            self.posts.append(new_post)

            html = """
            <html>
            <head>
                <title>Success</title>
                <meta http-equiv="refresh" content="1;url=/posts">
            </head>
            <body>
                <h1>Post Published!</h1>
                <p>Redirecting to posts...</p>
            </body>
            </html>
            """
            return HTTPResponse(200, html)
        else:
            return HTTPResponse(400, "Title and content required")
