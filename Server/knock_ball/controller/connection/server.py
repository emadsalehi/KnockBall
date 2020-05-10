import socket
from controller.game_controller import GameController

HOST = '127.0.0.1'
PORT = 6543

class Server(object):
    """This class is used for connecting clients to server"""

    def __init__(self):
        """Create server socket"""

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((HOST, PORT))

    def listen(self):
        """Listen for clients and create user"""

        self.socket.listen(1)
        while True:
            client, address = self.socket.accept()
            
