#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cgi, cgitb
import os
import csv
import tokens


cgitb.enable()

HTML = """
<html>
<head>
<title></title>
</head>
<body>
  <h1>Upload File</h1>
  <form action="upload_csv_file.py" method="POST" enctype="multipart/form-data">
    File: <input name="file" type="file">
    <input name="submit" type="submit">
</form>

</body>
</html>
"""

def upload_csv_file():
    print("Content-type: text/html\r\n\r\n")
    print(HTML)
    form = cgi.FieldStorage()
    try:
        uploaded_file = form['file']
        fl = os.path.join(tokens.UPLOAD_DIR, os.path.basename(uploaded_file.filename))

        if uploaded_file.file:
            # Convert file from bytes to strings
            str_file = uploaded_file.value.decode('utf-8').splitlines()
            # Read the file data
            filedata = csv.DictReader(str_file)
            # Retrieve the header row
            header = filedata.fieldnames
            # Save file
            with open(fl, 'w', newline='') as fl:
                writer = csv.DictWriter(fl, header)
                writer.writeheader()
                for row in filedata:
                    writer.writerow(row)
            print('File was saved')
        else:
            print('File was not uploaded')
    except KeyError:
        pass

if __name__ == '__main__':
    upload_csv_file()
