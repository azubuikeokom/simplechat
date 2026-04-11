import re
from models.chatmodel import Chat
from parser.exception import ParseError
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename=f'{__name__}.log',encoding='utf8')
streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)
logger.setLevel(logging.DEBUG)

class Parser:
    """Parsing of chat messages to return a request object"""
    def __init__(self) -> None:
        self._msg_blocks = []
        self._header_values_table = {}
        self._username_pattern = re.compile(r'Username: simplechat:[a-zA-Z0-9_]{2,20}@[a-zA-Z0-9]{2,20}\.[a-zA-Z]{2,4}', re.I)
        self._receiver_pattern = re.compile(r'Receiver: simplechat:[a-zA-Z0-9_]{2,20}@[a-zA-Z0-9]{2,20}\.[a-zA-Z]{2,4}',re.I)
        self._content_type = re.compile(r'Content-Type: (application/json|text/html|text/plain)',re.I)
        self._encoding = re.compile(r'Encoding: (utf8|utf-8)', re.I)
        self._expire = re.compile(r'Expire',re.I)
        self._key = re.compile(r'Key',re.I)
        self._method = re.compile(r'Method: (REGISTER|CHAT)',re.I)
        self._chat = Chat()

    def parse(self, msg:str) -> Chat:
        headers, msg = self.split_request_block(msg)
        header_lines = self.split_header_block(headers)
        self._chat.msg = msg
        for header_line in header_lines:
            if 'Username' in header_line:
                match = self._username_pattern.match(header_line)
                if match:
                    self._chat.username = header_line.split(':',2)[-1].strip()
            elif 'Receiver' in header_line:
                match = self._receiver_pattern.match(header_line)
                if match:
                    self._chat.receiver = header_line.split(':',2)[-1].strip()
            elif 'Content-Type' in header_line:
                match = self._content_type.match(header_line)
                if match:
                    self._chat.content_type = header_line.split(':',1)[-1].strip()
            elif 'Method' in header_line:
                match = self._method.match(header_line)
                if match:
                    self._chat.method = header_line.split(':',1)[-1].strip()
            elif 'Encoding' in header_line:
                match = self._encoding.match(header_line)
                if match:
                    self._chat.encoding = header_line.split(':',1)[-1].strip()
            else:
                raise ParseError           
        return self._chat

    def split_request_block(self,msg: str) -> list:
        "Split request block into headers and payload"
        request_list = msg.split('\n\n')
        logger.info(f"Request block split {request_list}")
        return request_list
    
    def split_header_block(self,header_block) -> list:
        "Split headers into a list of headers and their values"
        header_list = header_block.split('\n')
        logger.info(f"Header block split {header_list}")
        return header_list
    
    def tokenize_header_line(self,header_block: str) -> dict:
        "Split header line"
        header_values_table = {}
        header_list = header_block.split('\n')
        for header in header_list:
            key,value = header.split(':')
            header_values_table[key] = value
        logger.info(f"tokenized header lines {header_values_table}")
        return header_values_table


if __name__ == "__main__":
    parser = Parser()
    try:
        with open('protocol_test.txt','r') as f:
            sample_msg = f.read()
            chat = parser.parse(sample_msg)
            print(chat.__dict__)
    except ParseError as e:
        logger.error(e)

    


