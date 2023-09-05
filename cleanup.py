import re
from data import cities


def main(query: str) -> str:
    """Apply functions to input query in certain order.  """

    return remove_countries(
        remove_regions(
            remove_cities(
                remove_stop_words(
                    replace_e(
                        remove_symbols(query.lower()))))))


def strip_words_to(number, query):
    result = [word for word in query.split()]
    return ' '.join(result[:number])


def remove_symbols(query):
    """Remove all non-cyrillic symbols including numbers.
       Leave the numbers if the article or law is mentioned.
    """

    stopwords = ['статья', 'ст', 'фз', 'закон']
    if any(word in query.split() for word in stopwords):
        query = re.sub(r'[^а-я0-9^.]', ' ', query)
    else:
        query = re.sub(r'[^а-я]', ' ', query)
    # remove double spaces
    query = re.sub(r"\s\s+", " ", query)
    return query


def replace_e(query):
    return query.replace('ё', 'е')


def remove_latin(query):
    return re.sub(r"([a-zA-Z]+)", '', query)


def remove_numbers(query):
    return re.sub(r"([0-9]+)", ' ', query)


def remove_stop_words(query):
    from data.stopwords import STOP_WORDS

    return " ".join(word for word in query.split() if word not in STOP_WORDS and len(word) < 22)


def remove_phones(query):
    """Remove phone numbers, i.e. sequence of 10 to 18 digits, - and +. """

    match = re.search(r'(^|\s)([\d\+\-\(\)]{10,18})($|\s)', query)
    if match:
        query = query.replace(match.group(), ' ')
    return query


def remove_cities(query):
    """Remove the names of cities in all cases with prepositions. """

    # full search pattern
    pattern = r'(^|\s+)((?:%s)\s+)*((?:%s)\.?\s?)*(?:%s)\b' % (
        "|".join(cities.PREPOSITION),
        "|".join(cities.GOROD),
        "|".join(cities.CITIES)
    )

    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query


def remove_regions(query):
    """Remove the names of regions in cases with prepositions. """
    from data import regions

    # full search pattern
    pattern = r'(^|\s+)((?:%s)\s+)*(?:%s)\b' % (
        "|".join(cities.PREPOSITION), "|".join(regions.REGIONS)
    )
    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query


def remove_countries(query):
    """Remove the names of countries in cases with prepositions. """

    from data import countries

    # full search pattern
    pattern = r"(^|\s+)((?:%s)\s+)*(?:%s)\b" % (
        "|".join(cities.PREPOSITION), "|".join(countries.COUNTRIES)
    )
    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query.strip()


def change_abbr(query):
    """Replace incorrect abbreviations with correct ones. """
    from data import abbrev

    for abbr in abbrev.ABBR:
        pattern = re.compile(r"\b%s\b" % abbr.lower())
        result = re.search(pattern, query)
        if result:
            query = re.sub(pattern, abbr, query)
    return query
