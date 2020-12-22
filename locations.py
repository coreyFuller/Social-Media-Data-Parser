import json
from geopy.geocoders import Nominatim

    
def getFrequency(locations, geolocator):
    mostFreuqent = max(locations, key=locations.get)
    leastFrequent = min(locations, key = locations.get)
    most = findLocation(mostFreuqent, geolocator)
    least = findLocation(leastFrequent, geolocator)
    return least, most

def findLocation(coordinates, geolocator):
    Lat = str(coordinates[0])
    Long = str(coordinates[1])
    location = geolocator.reverse(Lat + "," + Long) 
    info = str(location).split(",")
    return info
    
def getLocations(location_history):
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
    return loc_dict
    

def getHistory(filepath):
    fp = open("Snapchat/json/location_history.json", "r")
    pure_text = fp.read()
    locations = json.loads(pure_text)
    location_history = locations["Location History"]
    return location_history

def run():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location_history = getHistory("Snapchat/json/location_history.json")
    locations = getLocations(location_history)
    data = getFrequency(locations, geolocator)
    pass

run()