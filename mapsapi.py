import googlemaps

import auth

gmaps = googlemaps.Client(key=auth.google_maps_API)

SPB = (59.935552, 30.321777)


class PyMapsAPI:
    """Custom Google Maps API class for searching new place."""
    """Nick: remember to set_coordinates first!"""

    def __init__(self, language='ru', radius=5000):
        self.gmaps = googlemaps.Client(key=auth.google_maps_API)  # Google Maps API initialization
        self.coordinates = (59.935552, 30.321777)  # The lat/lon center point values. Default: Saint-Petersburg center
        self.language = language  # The language in which to return results.
        self.radius = radius  # Distance in meters within which to bias results.

    def set_coordinates(self, custom_coordinates):
        self.coordinates = custom_coordinates

    def get_places_by_query(self, search_text):
        return self.gmaps.places_autocomplete_query(input_text=search_text, location=self.coordinates,
                                                    radius=self.radius, language=self.language)

    def get_place_info_by_id(self, place_id):
        place_info = self.gmaps.place(place_id=place_id, language='ru')
        return place_info

    def get_formatted_places(self, search_text):
        formatted_places = []
        unformatted_places = self.gmaps.places_autocomplete_query(input_text=search_text, location=self.coordinates,
                                                                  radius=self.radius, language=self.language)
        for place in unformatted_places:
            try:
                formatted_places.append({'place_description': place['description'], 'place_id': place['place_id']})
            except Exception as e:
                print(f"Error: {e}")
        return formatted_places

    def get_recommended_places(self, true_user_keywords):
        recommended_places = []
        for keyword in true_user_keywords:
            recommended_places.append(self.get_formatted_places(keyword))
        return recommended_places

