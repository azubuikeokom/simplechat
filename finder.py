from connection import Connection
from models.chatmodel import Chat 
from models.client import Client
from connections_table import ConnectionTable
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
class Finder:
    """This search for active connection and send message to the client's queue"""
    def __init__(self,active_connections:ConnectionTable):
        self.active_connection = ConnectionTable()

    def find_user(self,username: str) -> Client:
        client:Client = self.active_connection[username]
        return client

