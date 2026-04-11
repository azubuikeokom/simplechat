import asyncio 
from models.client import Client
from parser.parser import Parser, ParseError
from connections_table import ConnectionTable
from finder import Finder
from router import Router
from authentication import Authentication
import logging
import json


logger = logging.getLogger(__name__)
logging.basicConfig(filename=f'{__name__}.log',encoding='utf8')
streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)

class Server:
    def __init__(self,host:str|None="localhost",port:int|None=8888):
        self.host = host 
        self.port = port 
        self.parser = Parser()
        self.active_connections = ConnectionTable()
        self.finder = Finder(self.active_connections)
        self.authentication = Authentication()
        self.router = Router()
    
    async def start_server(self):
        server = await asyncio.start_server(self.handle_connection,self.host,self.port)
        addrs = server.sockets
        for socket in addrs:
            logger.info(f"server listeing {socket.getsockname()}")
        return server

    async def handle_connection(self,reader:asyncio.StreamReader,writer:asyncio.StreamWriter) -> None:
        logger.info(f"Accepted connection from {writer.get_extra_info('socket')}")
        try:
            raw_data = await reader.readuntil(b'\0')
            data = raw_data.decode('utf-8')
            chat = self.parser.parse(data)
            authenticated = await self.authenticate(chat)
            if authenticated:
                if chat.method == "REGISTER":
                    client = Client((reader,writer),chat)
                    await self.register_clients(client)
                    await asyncio.create_task(self.active_connection(client))
        except asyncio.LimitOverrunError as e:
            logger.error(e)
        except asyncio.IncompleteReadError as e:
            logger.error(e)
        except ParseError as e:
            logger.error(e)        

    async def register_clients(self, client: Client) -> None:
        self.active_connections.register_connection(client)
        logger.info(f"just registered client{client} to the active connection table")

    async def route_chat(self) -> None:
        pass

    async def authenticate(self,chat) -> bool:
        return self.authentication.authenticate(chat)
    
    async def active_connection(self,client:Client):
        while True:
            reader,writer = client.get_streams()
            raw_data = await reader.readuntil(b'\n')
            if raw_data == b'':
                break
            data = raw_data.rstrip(b'\0').decode()
            chat = self.parser.parse(data)
            try:
                dst_client = self.finder.find_user(chat.receiver)
                _, writer = dst_client.get_streams()
                writer.write(json.dumps(chat.__dict__).encode("utf8"))
            except KeyError as e:
                logger.error(e)
            


            

            












