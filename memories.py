import json
import os
import datetime

memories = open("json/memories_history.json")
data = json.loads(memories.read())

for info in data['Saved Media']:
    date = info['Date']
    url = info['Download Link']
    filetype = info['Media Type']
    
    req = requests.post(url, allow_redirects=True)
    response = req.text
    file = requests.get(response)
    
    
    day = date.split(" ")[0]
    time = date.split(" ")[1].replace(':', '-')
    filename = f'Memories/{day}_{time}.mp4' if type == 'VIDEO' else f'memories/{day}_{time}.jpg'
    
    with open(filename, 'wb') as f:
        f.write(file.content)