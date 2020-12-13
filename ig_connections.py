import json

ig = open("Instagram/connections.json", "r")
s = ig.read()
data = json.loads(s)
not_back = []
for following in data["following"].keys():
    if following not in data["followers"].keys():
        not_back.append(following)
        pass
print("People you follow that don't follow you back: ")
i = 1
for user in not_back:
    print("%d - %s" % ( i, user))
    i+=1
    
