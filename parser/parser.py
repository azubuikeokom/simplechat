import re
from chatmodel import Chat, ParseError


class Parser:
    def __init__(self) -> None:
        self._msg_blocks = []
        self._header_values_table = {}
        self._headers = ['Sender','Receiver','Content-Type','Expire','Key']
        self._sender_pattern = re.compile(r'Sender: simplechat:[a-zA-Z0-9_]{4,20}@[a-zA-Z0-9]\.[a-zA-Z]{2,3}', re.I)
        self._receiver_pattern = re.compile(r'Reveiver: simplechat:[a-zA-Z0-9_]{4,20}@[a-zA-Z0-9]\.[a-zA-Z]{2,3}',re.I)
        self._content_type = re.compile(r'Content-Type: application/json|text/html|text/plain',re.I)
        self._encoding = re.compile(r'Encoding: utf8|utf-8', re.I)
        self._expire = re.compile(r'Expire',re.I)
        self._key = re.compile(r'Key',re.I)
        self._chat = Chat()

    def chat_parse(self, msg:str) -> Chat:
        split_msg = self.split_protocol_block(msg)
        header_lines = self.split_protocol_block(split_msg[0])
        for header_line in header_lines:
            if 'Sender' in header_line:
                match = self._sender_pattern.match(header_line)
                if match:
                    self._chat.sender = header_line.split(':',1)
            elif 'Receiver' in header_line:
                match = self._receiver_pattern.match(header_line)
                if match:
                    self._chat.receiver = header_line.split(':',1)
            elif 'Content-Type' in header_line:
                match = self._content_type.match(header_line)
                if match:
                    self._chat.content_type = header_line.split(':',1)
            else:
                raise ParseError           
        return self._chat

    def split_protocol_block(self,msg: str) -> list:
        msg_list = msg.split('/r/n/r/n')
        return msg_list
    
    def split_header_block(self,header_block) -> list:
        header_list = header_block.split('/r/n')
        return header_list
    
    def tokenize_header_line(self,header_block: str) -> dict:
        header_values_table = {}
        header_list = header_block.split('/r/n')
        for header in header_list:
            key,value = header.split(':')
            header_values_table[key] = value
        return header_values_table


    


