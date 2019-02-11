#! /usr/bin/env python3.7
# -*- coding: utf-8 -*-

import re
import cgi
import values

form = cgi.FieldStorage()
query = form.getvalue('query')


def main(query):
    print("Content-type:text/html; charset:utf-8;\r\n\r\n")
    import sys
    print(query)
    print(sys.version)
    print(sys.stdout.encoding)
    query = query.lower()
    q1 = remove_symbols(query)
    q2 = remove_phones(q1)
    q3 = remove_cities(q2)
    q4 = remove_regions(q3)
    q5 = remove_countries(q4)
    print(change_abbr(q5))

def remove_symbols(query):
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
    query = re.sub("\s\s+", " ", query)
    return query

def remove_phones(query):
    match = re.search(r'(^|\s)([\d\+\-\(\)]{10,18})($|\s)', query)
    if match:
        query = query.replace(match.group(), ' ')
    return query

def remove_cities(query):
    # Add cities with 'ё' replaced on 'e'
    for city in values.CITY:
        if 'ё' in city:
            new_city = city.replace('ё', 'е')
            values.CITY.append(new_city)

    # sort city list alphabetically and by length starting from longest
    city_list_sorted = sorted(sorted(values.CITY, key=len, reverse=True))

    # full search pattern
    pattern = r"(^|\s+)((?:%s)\s+)*((?:%s)\.?\s?)*(?:%s)\b" % (
        "|".join(values.PREPOSITION), "|".join(values.GOROD), "|".join(city_list_sorted))

    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query

def remove_regions(query):
    # sort list by length starting from longest
    region_list_sorted = sorted(values.REGION, key=len, reverse=True)

    # full search pattern
    pattern = r"(^|\s+)((?:%s)\s+)*(?:%s)\b" % (
        "|".join(values.PREPOSITION), "|".join(region_list_sorted)
        )
    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query

def remove_countries(query):
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
    for abbr in values.ABBR:
        pattern = re.compile(r"\b%s\b" % abbr.lower())
        result = re.search(pattern, query)
        if result:
            query = re.sub(pattern, abbr, query)
    return query


if __name__ == '__main__':
    main(query)
