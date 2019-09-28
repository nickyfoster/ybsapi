import googlemaps
import auth

gmaps = googlemaps.Client(key=google_api_key)
SPB = (59.935552, 30.321777)


class PyMapsAPI():
    """Custom Google Maps API class for searching new place."""

    def __init__(self):
        self.gmaps = googlemaps.Client(key=auth.google_maps_API)
        self.coordinates = None

    def set_custom_coordinates(self, custom_coordinates):
        self.coordinates = custom_coordinates

    def get_places_by_query(self, search_text):
        return self.gmaps.places_autocomplete_query(input_text=search_text, location=SPB, radius=5000, language='ru')

    def get_formatted_places(self, search_text):




def get_places_info(search_text):
    user_places = gmaps.places_autocomplete_query(input_text=search_text, location=SPB, radius=5000, language='ru')
    return user_places


def find_places(search_text):
    places_to_return = []
    user_places = gmaps.places_autocomplete_query(input_text=search_text, location=SPB, radius=5000, language='ru')
    for place in user_places:
        places_to_return.append({'place_description': place['description'], 'place_id': place['place_id']})
    return places_to_return


def get_place_info(place_id):
    place_info = gmaps.place(place_id=place_id, language='ru')
    return place_info
