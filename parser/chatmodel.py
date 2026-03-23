from enum import Enum


class Header(Enum):
    METHOD = 'Method'
    SENDER = 'Sender'
    RECEIVER = 'Receiver'
    CONTENT_TYPE = 'Content-Type'
    EXPIRE = 'Expire'
    KEY = 'Key'
    ENCODING = 'Encoding'

class Chat:
    method: str
    sender: str
    receiver: str 
    content_type: str 
    expire: str
    key: str 
    msg: str
    

class ParseError(Exception):
    def __repr__(self) -> str:
        return f'ParseError: Parsing failed. Check Headers and their values'




