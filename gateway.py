
import socket
import time
import select
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST,PORT = "127.0.0.1",5055
server_sock.bind((HOST,PORT))
server_sock.listen(1)
BUFF_SIZE = 4096

while True:
    try:
        client_sock,addr = server_sock.accept()
        chat_msg = client_sock.recv(BUFF_SIZE)
        print(chat_msg.decode('utf8'))
    except socket.error as err:
        logger.debug(err)
