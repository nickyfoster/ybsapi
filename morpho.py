from rutermextract import TermExtractor

term_extractor = TermExtractor()


def group_morpho_analysis(groups: dict, limit: int, frequency: int) -> str:
    preprocess_text_data = ""
    for group in groups:
        try:
            preprocess_text_data += group['description'] + group['name']
        except Exception as e:
            print(f"Error: {e}")

    analysed_data = {}

    """
    term.normalized - keyword in text
    term.count      - quantity of keyword in text
    """
    for term in term_extractor(preprocess_text_data, limit=limit):
        analysed_data[term.normalized] = term.count

    result = []
    for keyword, count in analysed_data.items():
        if count > frequency:
            result.append(keyword)

    return result

def generate_dict(raw_text_data, limit, frequency):
    analysed_data = {}
    """
    term.normalized - keyword in text
    term.count      - quantity of keyword in text
    """
    for term in term_extractor(raw_text_data, limit=limit):
        analysed_data[term.normalized] = term.count
    result = []
    for keyword, count in analysed_data.items():
        if count > frequency:
            result.append(keyword)
    return result

