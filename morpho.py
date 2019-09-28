import rutermextract

import keywords


class PyMorpho:
    def __init__(self):
        self.termex = rutermextract.TermExtractor()
        self.true_keywords = keywords.our_keywords

    def get_keywords_list(self, raw_text_data, limit, frequency):
        """ Generate keywords list from string
        term.normalized - keyword in text
        term.count      - quantity of keyword in text
        """
        keyword_count_dict = {}
        result = []

        for term in self.termex(raw_text_data, limit=limit):
            keyword_count_dict[term.normalized] = term.count

        for keyword, count in keyword_count_dict.items():
            if count > frequency:
                result.append(keyword)
        return result

    def get_user_groups_keywords(self, groups, limit=40, frequency=2):

        """ Generate keywords list according to user groups """
        preprocess_text_data = ""
        keyword_count_dict = {}
        user_groups_keywords = []
        for group in groups:
            try:
                preprocess_text_data += group['description'] + group['name']
            except Exception as e:
                print(f"Error: {e}")

        for term in self.termex(preprocess_text_data, limit=limit):
            keyword_count_dict[term.normalized] = term.count

        for keyword, count in keyword_count_dict.items():
            if count > frequency:
                user_groups_keywords.append(keyword)

        return user_groups_keywords
