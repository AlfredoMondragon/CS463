# geopy_sample_script.py

# Sample script that uses a human readable address
# to retrieve geographic information from geodata store.

# Nominatum is the geodata store.
from geopy.geocoders import Nominatim

# Create connection object with data store
geolocator = Nominatim(user_agent="geopy_sample")

q = '1701 bryant st, denver, co'

# Retrieve geolocation object from data store (if exists).
a = geolocator.geocode(q)

# Dump some available attributes from location object
print('Location A: ', a.latitude, a.longitude)

