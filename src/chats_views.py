from json import loads

def getRecievedFrom(chats_dict):
    most_freq_rec = {}
    for chat in chats_dict["Received Chat History"]:
        name = chat["From"]
        if name not in most_freq_rec:
            most_freq_rec[name] = 1
        else:
            most_freq_rec[name] += 1
    return most_freq_rec

def getMetadata(filepath):
    chats = open(filepath, "r")
    s = chats.read()
    data = loads(s)
    return data

def getMax(chats_dict):
    max_user = max(chats_dict, key=chats_dict.get)
    max_chat = max(chats_dict.values())
    return max_user, max_chat

def getMin(chats_dict):
    min_user = min(chats_dict, key = chats_dict.get)
    min_chat = min(chats_dict.values())
    return min_user, min_chat
    
def getFrequency(chats_dict):
    max = getMax(chats_dict)
    min = getMin(chats_dict)
    return max, min

def MostFrequentNames(max_chats):
    top_snapchatters = []
    res = sorted(max_chats.items(), key=lambda kv: kv[1], reverse=True)
    res = res[:5]
    for r in res:
        top_snapchatters.append(r)
    return top_snapchatters

def getSentTo(chats_dict):
    most_freq_sent = {}
    for chat in chats_dict["Sent Chat History"]:
        name = chat["To"]
        if name not in most_freq_sent:
            most_freq_sent[name] = 1
        else:
            most_freq_sent[name] += 1
    return most_freq_sent

def parseStoryData(story_dict):
    story_dict = {}
    stories = open("Snapchat/json/story_history.json", "r")
    data = loads(stories.read())

    date_to_view = {}
    for story in data["Your Story Views"]:
        date = story['Story Date']
        view = story['Story Views']
        date_to_view[date] = view
        
    sorted_views = sorted(date_to_view, key=date_to_view.get,reverse=True)
    
    return sorted_views

def getTopStoryDates(sorted_views):
    date_only_dict = {}
    for date in sorted_views[:25]:
        date = date.split(" ")
        if date[0] not in date_only_dict:
            date_only_dict[date[0]] = None
    return date_only_dict

    
def run():
    chats_dict = getMetadata("Snapchat/json/chat_history.json")  
    story_dict = getMetadata("Snapchat/json/story_history.json")
    sent = getSentTo(chats_dict)
    received = getRecievedFrom(chats_dict)  
    sent_frequency = getFrequency(sent)
    received_frequency = getFrequency(received)
    views = parseStoryData(story_dict)
    top_views_dict = getTopStoryDates(views)
    
    pass
    
run()