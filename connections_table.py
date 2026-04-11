class ConnectionTable:

    def __init__(self) -> None:
        self.connections_table = {}

    def __getitem__(self, key):
        return self.connections_table[key]
    
    def deregister_connection(self,client) -> None:
        del self.connections_table[client]

    def register_connection(self,client) -> None:
        self.connections_table[client] = client
    