from geopy.geocoders import Nominatim
from time import sleep

geolocator = Nominatim(user_agent="disease_app")

def get_coordinates(place):
    try:
        location = geolocator.geocode(place)
        if location:
            return (location.latitude, location.longitude)
    except:
        return None
