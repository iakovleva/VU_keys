#! /usr/bin/python3
# -*- coding: utf-8 -*-

import re
import cgi

form = cgi.FieldStorage()
query = form.getvalue('query')


def main(query):
    print("Content-type:text/html\r\n\r\n")
    match = re.search(r'(^|\s)([\d\+\-\(\)]{10,18})($|\s)', query)
    if match:
        new_query = query.replace(match.group(), ' ')
        print(new_query.strip())
    else:
        print(query)

if __name__ == '__main__':
    main(query)
