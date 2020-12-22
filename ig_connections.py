import json

def following_parser(json_fp):
    s = json_fp.read()
    data = json.loads(s)
    not_back = []
    un_acked = []
    for following in data["following"].keys():
        if following not in data["followers"].keys():
            not_back.append(following)
    
    print("\nPeople you follow that don't follow you back: ")
    i = 1
    for user in not_back:
        print("%d - %s" % ( i, user))
        i+=1
    
    for request in data["follow_requests_sent"].keys():
        if request not in data["following"].keys():
            un_acked.append(request)
        
    print("\n\n\n\n")   
    print("Unacknowledged follow requests you sent: ")

    i = 1
    for user in un_acked:
        print("%d - %s" % ( i, user))
        i+=1


def likes_parser(json_fp):
    s = json_fp.read()
    data = json.loads(s)
    media_likes = data['media_likes']
    likes_dict = {}

    for user in media_likes:
        username = user[1]
        if username not in likes_dict:
            likes_dict[username] = 1
        else:
            likes_dict[username] += 1
        
    most_liked = max_user = max(likes_dict, key=likes_dict.get)
    print("Most liked page at %d likes: %s" % (likes_dict[most_liked], most_liked))
    
def run():
    likes = open('instagram/likes.json', 'r')
    followings = open("Instagram/connections.json", "r")
    following_parser(followings)
    likes_parser(likes)
    
    
run()  

