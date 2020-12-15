from json import loads


### reading recieved chat data
chats = open("Snapchat/json/chat_history.json", "r")
s = chats.read()
data = loads(s)
most_freq_rec = {}

for chat in data["Received Chat History"]:
    name = chat["From"]
    if name not in most_freq_rec:
        most_freq_rec[name] = 1
    else:
        most_freq_rec[name] += 1
  
max_user = max(most_freq_rec, key=most_freq_rec.get)
min_user = min(most_freq_rec, key = most_freq_rec.get)
max_chat = max(most_freq_rec.values())
min_chat = min(most_freq_rec.values())

print("Most frequent recieved chat: %s \  %d" % (max_user, max_chat))
print("Least frequent recieved chat: %s \  %d\r\n" % (min_user, min_chat))

res = sorted(most_freq_rec.items(), key=lambda kv: kv[1], reverse=True)
print("top 5 snapchatters that messaged you this month: ")
res = res[:5]
for r in res:
    print(r[0])

print("\n\n")
    



####################################################################


### reading recieved chat data

most_freq_sent = {}
for chat in data["Sent Chat History"]:
    name = chat["To"]
    if name not in most_freq_sent:
        most_freq_sent[name] = 1
    else:
        most_freq_sent[name] += 1
        
max_user = max(most_freq_sent, key=most_freq_sent.get)
min_user = min(most_freq_sent, key = most_freq_sent.get)
max_chat = max(most_freq_sent.values())
min_chat = min(most_freq_sent.values())

print("Most frequent sent chat: %s \  %d" % (max_user, max_chat))
print("Least frequent sent chat: %s \  %d\r\n" % (min_user, min_chat))

res = sorted(most_freq_sent.items(), key=lambda kv: kv[1], reverse=True)
print("top 5 snapchatters that you messaged this month: ")
res = res[:5]
for r in res:
    print(r[0])

print("\n\n")
    

###################

### reading story view data

story_dict = {}
stories = open("Snapchat/json/story_history.json", "r")
data = loads(stories.read())

date_to_view = {}
for story in data["Your Story Views"]:
    date = story['Story Date']
    view = story['Story Views']
    date_to_view[date] = view
    
sorted_views = sorted(date_to_view, key=date_to_view.get,reverse=True)

date_only_dict = {}

print("Top days for views in the past month: ")
for date in sorted_views[:25]:
    date = date.split(" ")
    if date[0] not in date_only_dict:
        date_only_dict[date[0]] = None

for i in date_only_dict.keys():
    print(i)