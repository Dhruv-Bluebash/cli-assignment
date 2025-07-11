from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable, GeocoderTimedOut
import time

geolocator = Nominatim(user_agent="client-validator-cli")

def get_coordinates(address, retries=3):
    for attempt in range(retries):
        try:
            location = geolocator.geocode(address, timeout=10)
            if location:
                time.sleep(1) 
                return (location.latitude, location.longitude)
            else:
                return None
        except (GeocoderUnavailable, GeocoderTimedOut) as e:
            print(f"Geolocation error ({e}), retrying ({attempt+1}/{retries})...")
            time.sleep(2)
    return None

