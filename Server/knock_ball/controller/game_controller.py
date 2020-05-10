class GameController:
    """Using singleton design pattern from big manager of game!"""

    __instance = None


    @staticmethod
    def get_instance():
        '''Static access method'''

        if GameController.__instance == None:
            GameController()
        return GameController.__instance

    def __init__(self):
        '''Private constructor'''

        if GameController.__instance == None:
            GameController.__instance = self
            self.user_dict = {}


    def sign_up(self, userame, password):
        """Signup user to database"""

        raise("Not implemented error!")


    def login(self, username, password):
        """Login user by using database"""

        raise("not implemented error!")
