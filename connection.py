class Connection:
    def __init__(self) -> None:
        self.active_connections = {}

    def addConnection(self,socket,reg) -> None:
        self.active_connections[reg] = socket
    
    def check_connection(self,username) -> str | None:
        if username in self.active_connections:
            return self.active_connections[username]
