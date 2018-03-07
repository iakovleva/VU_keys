#! /usr/bin/python

import sys
import re

symbol_list = [
    '\?', '!', '@', '·', '#', '\$', '\%', '\^', '\&', '\*', '\(', '\)', '\[', '\]',
    '\{', '\}', '\/', '\|', r'\\', '№', '\+', '<', '>', ':', ';', '“', '“', '`', '~', '=',
]


def main():
    try:
        if len(sys.argv) > 2:
            print ("Please enter only 1 text string query")
        else:
            query = sys.argv[1].lower()
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
            print (query)
    except IndexError:
        print ("Enter a query")

if __name__ == '__main__':
    main()
