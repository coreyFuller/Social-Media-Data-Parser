import json


def getNotFollowedBack(connections):
    not_back = []
    print(connections["following"])
    for user in connections["following"].keys():
        if user not in connections["followers"].keys():
            not_back.append(user)
    return not_back

def getUnacknowledgedRequests(connections): 
    unacked_requests = []      
    for request in connections["follow_requests_sent"].keys():
        if request not in connections["following"].keys():
            unacked_requests.append(request)
    return unacked_requests
    
    
def getConnectionsInfo(filename):
    fp = open(filename, "r")
    s = fp.read()
    data = json.loads(s)
    
    not_following_back = getNotFollowedBack(data)
    unacked_requests = getUnacknowledgedRequests(data)
    
    return not_following_back, unacked_requests

def buildLikesDictionary(media_likes):
    likes_dict = {}
    for user in media_likes:
        username = user[1]
        if username not in likes_dict:
            likes_dict[username] = 1
        else:
            likes_dict[username] += 1
    return likes_dict

def getFrequency(likes):
    most = max(likes, key = likes.get)
    least = min(likes, key = likes.get)
    return least, most
    
def getLikesInfo(filename):
    fp = open(filename, "r")
    s = fp.read()
    data = json.loads(s)
    media_likes = data['media_likes']
    likes = buildLikesDictionary(media_likes)
    return likes
    
def run():
    connection_data = getConnectionsInfo("Instagram/connections.json")
    likes = getLikesInfo("Instagram/likes.json")
    frequency = getFrequency(likes)
    print("Most liked page at %d likes: %s" % (likes[frequency[1]], frequency[1]))
    print(connection_data[0])
    print("\n\n\n\n\n")
    print(connection_data[1])

run()  

