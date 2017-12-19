#! /usr/bin/python

import sys
import re


def main():
    try:
        if len(sys.argv) > 2:
            print ("Please enter only 1 text string query")
        else:
            query = sys.argv[1]
            match = re.search(r'(^|\s)([\d\+\-\(\)]{10,18})($|\s)', query)
            if match:
                new_query = query.replace(match.group(), ' ')
                print (new_query.strip())
            else:
                print (query)
    except IndexError:
        print ("Enter a query")

if __name__ == '__main__':
    main()
