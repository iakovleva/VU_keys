#!/usr/bin/env python3

import re
import cgi
import values


form = cgi.FieldStorage()
query = form.getvalue('query')


def main(query):
    """Apply functions to input query in certain order.

    Input: string query.
    Output: changed query.
    """

    print("Content-type:text/html; charset:utf-8;\r\n\r\n")
    query = query.lower()
    q1 = remove_symbols(query)
    q2 = remove_phones(q1)
    q3 = remove_cities(q2)
    q4 = remove_regions(q3)
    q5 = remove_countries(q4)
    print(change_abbr(q5))


def remove_symbols(query):
    """Remove symbols according to the rules."""

    # remove '_' in any case except spu_orb
    if 'spu_orb' not in query:
        query = re.sub(r'_', ' ', query)
    # replace comma with space
    if ',' in query:
        query = re.sub(r',', ' ', query)
    # remove other punctuation
    for symbol in values.SYMBOL:
        result = re.search(symbol, query)
        if result:
            query = re.sub(symbol, ' ', query)
    # remove spaces, dots and dashes in the end and at the beginning
    query = query.strip(' -.')
    # remove double spaces
    query = re.sub(r"\s\s+", " ", query)
    return query


def remove_phones(query):
    """Remove phone numbers, i.e. sequence of 10 to 18 digits, - and +. """

    match = re.search(r'(^|\s)([\d\+\-\(\)]{10,18})($|\s)', query)
    if match:
        query = query.replace(match.group(), ' ')
    return query


def remove_cities(query):
    """Remove the names of cities in all cases with prepositions. """

    # Add cities with 'ё' replaced on 'e'
    for city in values.CITY:
        if 'ё' in city:
            new_city = city.replace('ё', 'е')
            values.CITY.append(new_city)

    # sort city list alphabetically and by length starting from longest
    city_list_sorted = sorted(sorted(values.CITY, key=len, reverse=True))

    # full search pattern
    pattern = r'(^|\s+)((?:%s)\s+)*((?:%s)\.?\s?)*(?:%s)\b' % (
        "|".join(values.PREPOSITION),
        "|".join(values.GOROD),
        "|".join(city_list_sorted)
        )

    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query


def remove_regions(query):
    """Remove the names of regions in cases with prepositions. """

    # sort list by length starting from longest
    region_list_sorted = sorted(values.REGION, key=len, reverse=True)

    # full search pattern
    pattern = r'(^|\s+)((?:%s)\s+)*(?:%s)\b' % (
        "|".join(values.PREPOSITION), "|".join(region_list_sorted)
        )
    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query


def remove_countries(query):
    """Remove the names of countries in cases with prepositions. """

    # sort list by length starting from longest
    country_list_sorted = sorted(values.COUNTRY, key=len, reverse=True)

    # full search pattern
    pattern = r"(^|\s+)((?:%s)\s+)*(?:%s)\b" % (
        "|".join(values.PREPOSITION), "|".join(country_list_sorted)
        )
    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query


def change_abbr(query):
    """Replace incorrect abbreviations with correct ones. """

    for abbr in values.ABBR:
        pattern = re.compile(r"\b%s\b" % abbr.lower())
        result = re.search(pattern, query)
        if result:
            query = re.sub(pattern, abbr, query)
    return query


if __name__ == '__main__':
    main(query)
