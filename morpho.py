from rutermextract import TermExtractor

term_extractor = TermExtractor()

def group_morpho_analysis(groups: dict) -> str:
    preprocess_text_data = ""

    for group in groups:
        try:
            preprocess_text_data += group['description'] + group['name']
        except Exception:
            pass

    analysed_data = {}

    """
    term.normalized - keyword in text
    term.count      - quantity of keyword in text
    """
    for term in term_extractor(preprocess_text_data, limit=10):
        analysed_data[term.normalized] = term.count

    result = []
    for keyword, count in analysed_data.items():
        if count > 1:
            result.append(keyword)

    return result


