import googlemaps

import auth


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

    def get_places_test_method(self, search_text):
        return self.gmaps.places(query=search_text, location=self.coordinates, radius=self.radius,
                                 language=self.language)

    def get_place_info_by_id(self, place_id):
        place_info = self.gmaps.place(place_id=place_id, language='ru')
        return place_info

    def get_parsed_places(self, search_text):
        parsed_places = []
        unparsed_places = self.gmaps.places_autocomplete_query(input_text=search_text, location=self.coordinates,
                                                               radius=self.radius, language=self.language)
        for place in unparsed_places:
            try:
                parsed_places.append({'place_description': place['description'], 'place_id': place['place_id']})
            except Exception:
                pass
        return parsed_places

    def get_recommended_places(self, true_user_keywords):
        recommended_places = []
        for keyword in true_user_keywords:
            recommended_places.append(self.get_parsed_places(keyword))
        return recommended_places

    def format_place(self, place_id, place_description):
        formatted_data = {}
        place_data = self.get_place_info_by_id(place_id)
        try:
            formatted_data['name'] = place_data['result']['name']
            formatted_data['description'] = place_description
            formatted_data['address'] = place_data['result']['formatted_address']
            formatted_data['phone'] = place_data['result']['international_phone_number']
            formatted_data['website'] = place_data['result']['website']
            formatted_data['icon'] = place_data['result']['icon']
            formatted_data['url'] = place_id['result']['url']
        except Exception:
            pass
        return formatted_data

    def format_recommended_places(self, recommended_places):
        formatted_recommended_places = []
        for places in recommended_places:
            for place in places:
                formatted_recommended_places.append(self.format_place(place['place_id'], place['place_description']))

        return formatted_recommended_places
