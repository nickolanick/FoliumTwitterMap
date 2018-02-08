from geopy import ArcGIS


def find_location(locate_film):
    """
    (str)-->int,int
    Return the latitude and longitude of the location
    """
    geolocator = ArcGIS(timeout=10)
    place = geolocator.geocode(locate_film)
    return place.latitude, place.longitude
