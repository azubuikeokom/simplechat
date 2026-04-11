from enum import Enum

class Header(Enum):
    METHOD = 'Method'
    USERNAME = 'Username'
    RECEIVER = 'Receiver'
    CONTENT_TYPE = 'Content-Type'
    EXPIRE = 'Expire'
    KEY = 'Key'
    ENCODING = 'Encoding'

class Chat:
    method: str
    username: str
    receiver: str 
    content_type: str 
    chat_type: str
    encoding: str
    key: str 
    msg: str
    method: str







