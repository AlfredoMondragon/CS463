# geopy_handler.py


from geopy.geocoders import Nominatim # Nominatum geocoder service.

def query_handler(addr):
    """Performs a geo data lookup with given string parameter.
    Uses Nominatum as data source 
    Returns a Location object. See: 

    https://geopy.readthedocs.io/en/stable/index.html?highlight=Location#module-geopy.geocoders
    """
    
    # Create a geocoder
    geolocator = Nominatim(user_agent="geopy_sample")

    # Use geolocator object to retrieve Location object from geocoder (see geopy_sample_script.py)
    
    # Return location object
    return 
