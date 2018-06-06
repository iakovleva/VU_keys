#! /usr/bin/python

import sys
import openpyxl
from collections import Counter

def count_frequency(fl):
    wb = openpyxl.load_workbook(fl)
    sh = wb.active
    sh2 = wb.create_sheet(title='Sheet2')
    cnt = Counter()

    # Create Counter for all words in column
    for i in range(1, sh.max_row):
            key = sh.cell(row=i, column=1).value
            for word in key.split():
                cnt[word] += 1

    new_row_start = 1
    for k, v in cnt.most_common(40):
        print(k)
        for i in range(1, sh.max_row):
            if k in sh.cell(row=i, column=1).value.split():
                sh2.cell(row=new_row_start, column=1).value = sh.cell(row=i,column=1).value
                sh2.cell(row=new_row_start, column=2).value = k
                new_row_start += 1
    wb.save(fl)

if __name__ == '__main__':
    count_frequency(sys.argv[1])
