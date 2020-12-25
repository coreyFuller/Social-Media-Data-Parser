from instagram import connections
from json import loads

class Instagram:    
    connections_info = {}
    likes_info = {}
    comments_info = {}
    
    def __init__(self):
        self.connections_info = connections.getConnectionsInfo("Instagram/connections.json")
        

    def run(self):
        print(connections.getNotFollowedBack(self.connections_info))
        print(connections.getUnacknowledgedRequests(self.connections_info))   
