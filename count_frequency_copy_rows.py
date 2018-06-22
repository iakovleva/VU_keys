#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import openpyxl
from collections import Counter

def count_frequency(fl):
    wb = openpyxl.load_workbook(fl)
    sh = wb.active
    cnt = Counter()

    # Create new sheet with headers row
    sh2 = wb.create_sheet(title='Sheet2')
    sh2.cell(row=1, column=1).value = sh.cell(row=1, column=1).value
    sh2.cell(row=1, column=2).value = 'Word'
    for col in range(3, 18):
        sh2.cell(row=1, column=col).value = sh.cell(row=1, column=col-1).value

    # Create Counter for all words in column
    for i in range(1, sh.max_row):
            cell = sh.cell(row=i, column=6).value
            if cell is not None:
                for word in str(cell).split():
                    cnt[word.lower()] += 1

    # Check if each common word is in each keyword phrase, create new row with all
    # data about kw plus a column with commom word in this phrase
    new_row_start = 2
    for k, v in cnt.most_common(100):
#        print(k, v)
        for i in range(1, sh.max_row):
            cell = sh.cell(row=i, column=6).value
            if cell is not None:
                if k in str(cell).lower().split():
                    sh2.cell(row=new_row_start, column=1).value = sh.cell(row=i, column=1).value
                    sh2.cell(row=new_row_start, column=2).value = k
                    sh2.cell(row=new_row_start, column=3).value = sh.cell(row=i, column=2).value
                    sh2.cell(row=new_row_start, column=4).value = sh.cell(row=i, column=3).value
                    sh2.cell(row=new_row_start, column=5).value = sh.cell(row=i, column=4).value
                    sh2.cell(row=new_row_start, column=6).value = sh.cell(row=i, column=5).value
                    sh2.cell(row=new_row_start, column=7).value = sh.cell(row=i, column=6).value
                    sh2.cell(row=new_row_start, column=8).value = sh.cell(row=i, column=7).value
                    sh2.cell(row=new_row_start, column=9).value = sh.cell(row=i, column=8).value
                    sh2.cell(row=new_row_start, column=10).value = sh.cell(row=i, column=9).value
                    sh2.cell(row=new_row_start, column=11).value = sh.cell(row=i, column=10).value
                    sh2.cell(row=new_row_start, column=12).value = sh.cell(row=i, column=11).value
                    sh2.cell(row=new_row_start, column=13).value = sh.cell(row=i, column=12).value
                    sh2.cell(row=new_row_start, column=14).value = sh.cell(row=i, column=13).value
                    sh2.cell(row=new_row_start, column=15).value = sh.cell(row=i, column=14).value
                    sh2.cell(row=new_row_start, column=16).value = sh.cell(row=i, column=15).value
                    sh2.cell(row=new_row_start, column=17).value = sh.cell(row=i, column=16).value
                    new_row_start += 1
    wb.save(fl)

if __name__ == '__main__':
    count_frequency(sys.argv[1])
