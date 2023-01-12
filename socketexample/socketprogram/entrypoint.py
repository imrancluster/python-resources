#
# Single function will run server and client
#
import socket
from .server import _server
from .client import _client

HOSTNAME = socket.gethostbyname('localhost')
PORT = 5000


def run(run_argument: str):
    if run_argument.lower() == 'server':
        _server(HOSTNAME, PORT)
    elif run_argument.lower() == 'client':
        _client(HOSTNAME, PORT)
