
import socket
import time
import select
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def setup_socket() -> socket.socket | None:
    try:
        server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        HOST,PORT = "127.0.0.1",5055
        server_sock.bind((HOST,PORT))
        server_sock.listen(5)
        return server_sock
    except socket.error as e: #get the appropriate exception for sockets
        logger.error('Failed to create socket')
        logger.error(f'Reason: {e}')


def accept_connection(server_socket:socket.socket,BUFF_SIZE = 4096):
    while True:
        try:
            client_sock,addr = server_socket.accept()
            chat_msg = client_sock.recv(BUFF_SIZE)
            print(chat_msg.decode('utf8'))
        except socket.error as err:
            logger.debug(err)
