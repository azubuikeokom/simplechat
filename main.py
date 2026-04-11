from connections_table import ConnectionTable
from server import Server
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
if PORT is not None:
    PORT = int(PORT)

async def main(host,port):
    server = Server(host=host,port=port)
    main_server = await server.start_server()
    async with main_server:
        await main_server.serve_forever()
          

if __name__ == "__main__":
    asyncio.run(main(HOST,PORT))