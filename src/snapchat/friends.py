from json import loads

def readFile(filepath):
    fp = open(filepath, "r")
    s = fp.read()
    metadata = loads(s)
    return metadata

def getUnacknowledgedRequests(metadata):
    unacked_requests = []
    for user in metadata['Friend Requests Sent']:
        if user['Username'] not in  metadata['Friends']:
            unacked_requests.append(user['Username'])
    return unacked_requests
    

def run():
    metadata = readFile("Snapchat/json/friends.json")
    print(getUnacknowledgedRequests(metadata))
    pass
