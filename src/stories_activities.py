from json import loads

def readFile(filepath):
    fp = open(filepath, "r")
    s = fp.read()
    metadata = loads(s)
    return metadata

def getMostInteractedPolls(metadata):
    user_dict = {}
    for data in metadata['polls']:
        if data[1] not in user_dict:
            user_dict[data[1]] = 1
        else:
            user_dict[data[1]] += 1
    return max(user_dict, key=user_dict.get), user_dict[max(user_dict, key=user_dict.get)]

def run():
    metadata = readFile("Instagram/stories_activities.json")
    most = getMostInteractedPolls(metadata)    