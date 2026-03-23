from connection import Connection

class finder:
    def __init__(self):
        self.connection = Connection()

    def user_active(self,chat_msg):
        socket = self.connection.check_connection(chat_msg)
        if socket:
            # send message to client
            pass