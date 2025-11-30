import logging
import sys
from server import HTTPServer

# Initialize log system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stdout
)

if __name__ == "__main__":
    server = HTTPServer()
    server.start()
    while True:
        server.wait()
    server.stop()
