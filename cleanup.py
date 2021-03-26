import re
import values
import psycopg2


def main(query):
    """Apply functions to input query in certain order.
    Input: string query.
    Output: changed query.
    """
    q1 = remove_symbols(query.lower())
    return change_abbr(remove_countries(remove_regions(remove_cities(remove_phones(q1)))))


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

# TODO Cache sorted lists
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

# TODO Cache sorted lists
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

# TODO Cache sorted lists
    # sort list by length starting from longest
    country_list_sorted = sorted(values.COUNTRY, key=len, reverse=True)

    # full search pattern
    pattern = r"(^|\s+)((?:%s)\s+)*(?:%s)\b" % (
        "|".join(values.PREPOSITION), "|".join(country_list_sorted)
    )
    match = re.search(pattern, query)
    if match:
        query = query.replace(match.group(), '')
    return query.strip()


def change_abbr(query):
    """Replace incorrect abbreviations with correct ones. """

    for abbr in values.ABBR:
        pattern = re.compile(r"\b%s\b" % abbr.lower())
        result = re.search(pattern, query)
        if result:
            query = re.sub(pattern, abbr, query)
    return query


if __name__ == '__main__':
    sql = "UPDATE keys SET newkey=%s where key=%s"
    try:
        conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
        cur = conn.cursor()
        cur.execute("SELECT * from keys where newkey is NULL")
        for row in cur.fetchall():
            new_key = main(row[0])
            cur.execute(sql, (new_key, row[0]))
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cur.close()
        conn.close()
