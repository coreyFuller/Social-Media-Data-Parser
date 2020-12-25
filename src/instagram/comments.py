from json import loads

def readFile(filepath):
    fp = open(filepath, encoding="utf8")
    s = fp.read()
    metadata = loads(s)
    return metadata

def getMostCommented(metadata, my_username='cjfuller_official'):
    user_dict = {}
    for comment in metadata['media_comments']:
        if comment[2] not in user_dict:
            user_dict[comment[2]] = 1
        else:
            user_dict[comment[2]] += 1
    if my_username in user_dict.keys():
        del user_dict[my_username]
    max_user = max(user_dict, key = user_dict.get) 
    return user_dict[max_user], max_user
     

def run():
    metadata = readFile("Instagram/comments.json")
    info = getMostCommented(metadata)
    print(info)
    
run()