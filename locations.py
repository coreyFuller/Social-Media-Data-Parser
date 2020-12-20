import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

fp = open("Snapchat/json/location_history.json", "r")

pure_text = fp.read()
locations = json.loads(pure_text)
location_history = locations["Location History"]

loc_dict = {}
for location in location_history:
    latAndLong = location['Latitude, Longitude']
    latAndLong = latAndLong.split(",")
    latitude = latAndLong[0].split(" ")[0]
    longitude = latAndLong[1].split(" ")[1]
    latAndLong = (latitude, longitude)
    if latAndLong not in loc_dict:
        loc_dict[latAndLong] = 1
    else:
        loc_dict[latAndLong] += 1
        
most_loc = max(loc_dict, key=loc_dict.get)
least_loc = min(loc_dict, key=loc_dict.get)

Lat = str(most_loc[0])
Long = str(most_loc[1])
location = geolocator.reverse(Lat + "," + Long) 
info = str(location).split(",")

print("%s, %s" % (info[3], info[4]))