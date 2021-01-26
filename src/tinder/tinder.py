import json

fp = open("Tinder/data.json", "r")

data = json.loads(fp.read())

print(data)