# pyhttp

A simple HTTP server built with Python, providing a simple blog system.

## Quick Start

```console
$ python main.py
```

The login:
```console
Username: aris
Password: aris
```
You can set it through `setup_account()` in `server.py`.


## Project Structure

- `main.py` - Server entry point
- `server.py` - Accepts HTTP request and spawns new threads for processing
- `request.py` - Parses HTTP request
- `router.py` - Routes request to appropriate handler based on URL path
- `handler.py` - Handles request and generates response
- `response.py` - Builds HTTP response

## Workflow

The complete request processing flow:

1. **Request Reception** - User accesses `localhost:8888/`, server accepts the request
2. **Request Parsing** - Extracts request method (GET/POST) and path ('/')
3. **Thread Handling** - Creates a new thread to process the request
4. **Routing** - Routes the request to the corresponding handler function
5. **Response Generation** - Handler processes the request and returns an HTTP response
6. **Content Delivery** - Browser receives and renders the response (e.g., `login.html`)

## Reference

- [HTTP](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Guides/Overview)
