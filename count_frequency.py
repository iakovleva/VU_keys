#! /usr/bin/python

import sys
import openpyxl
from collections import Counter


def count_frequency(fl):
    wb = openpyxl.load_workbook(fl)
    sh = wb.active
    cnt = Counter()

    # Create Counter for all words in column
    for i in range(1, sh.max_row):
            cell =  sh.cell(row=i, column=1).value
            if cell is not None:
                for word in cell.split():
                    cnt[word] += 1

    for k, v in cnt.most_common(40):
        print(k, v)

if __name__ == '__main__':
    count_frequency(sys.argv[1])
