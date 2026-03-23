class Presense:
    def __init__(self) -> None:
        self.contacts = [] 
    def getActiveConnections(self,client_req) -> list:
         #connect to redis/table for active connection
         # add to contacst and return
         return self.contacts