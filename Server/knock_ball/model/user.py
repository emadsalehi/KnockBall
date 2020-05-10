import enum
import threading
import socket
from controller.game_controller import GameController

class UserState(enum.Enum):
    """Enum that defines user state in app"""

    not_logged_in = 1
    logged_in = 2
    in_game = 3


class User:
    """Keeps user's client socket and states"""

    def __init__(self, client, address):
        """Initialize user state and run reader thread of user"""

        self.user_state = UserState.not_logged_in
        threading.Thread(target = self.read_user_data, args = (,)).start()


    def read_user_data():
        """Method to read data from user client"""

        size = 4096
        while True:
            try:
                data = self.client.recv(size)
                self.process_data(data)
            except:
                self.client.close()
                self.remove_user()
                return False


    def process_data(self, data):
        """Proccess data that come from client"""

        raise("Not implemented error.")


    def remove_user(self):
        """Remove user from active users list"""

        raise("Not implemented error.")
