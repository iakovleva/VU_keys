#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re
import cgi

form = cgi.FieldStorage()
query = form.getvalue('query')

symbol_list = [
    '\?', '!', '@', '·', '#', '\$', '\%', '\^', '\&', '\*', '\(', '\)', '\[', '\]',
    '\{', '\}', '\/', '\|', r'\\', '№', '\+', '<', '>', ':', ';', '“', '“', '`', '~', '=',
]


def main(query):
    print("Content-type:text/html\r\n\r\n")
    # remove '_' in any case except spu_orb 
    if 'spu_orb' not in query:
        query = re.sub(r'_', ' ', query)
    # replace comma with space
    if ',' in query:
        query = re.sub(r',', ' ', query)
    # remove other punctuation
    for symbol in symbol_list:
        result = re.search(symbol, query)
        if result:
            query = re.sub(symbol, ' ', query)
    # remove spaces, dots and dashes in the end and at the beginning
    query = query.strip(' -.')
    # remove double spaces
    query = re.sub("\s\s+", " ", query)
    print(query)

if __name__ == '__main__':
    main(query)
