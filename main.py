import logging
import sys
from server import HTTPServer
from request import HTTPRequest

# Initialize log system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

if __name__ == "__main__":
    server = HTTPServer()
    server.start()
    # while True:
    server.wait_request()
    server.stop()
