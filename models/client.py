from models.chatmodel import Chat
import asyncio

class Client:

    def __init__(self,streams:tuple,chat:Chat) -> None:
        self._streams = streams
        self._chat = chat

    def __str__(self) -> str:
        return f"{self._username}"
    
    def __repr__(self) -> str:
        return f"{self._username}"

    def set_username(self, chat:Chat) -> None:
        self._username = chat.username
    
    def get_streams(self) -> tuple[asyncio.StreamReader,asyncio.StreamWriter]:
        return self._streams


