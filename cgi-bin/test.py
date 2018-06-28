#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.parse import urlencode
import subprocess
import unittest
import tokens


sentence = {
    'пфр в Московской обл': 'ПФР',
    'ПФР в московской обл': 'ПФР',
    'ПФРвмосковскойобл': 'пфрвмосковскойобл',
    'пфр в московской обл': 'ПФР',
    'ПФР в москве': 'ПФР',
    'pfr moskva': 'pfr',
    'telefon ufms piter': 'telefon ufms piter',
    'cанкт петербург 9221233554': '',
    'cанкт петербург (922)1233554': '',
    'cанкт петербург 922-123-35-54': '',
    'Санкт петербург 9221;233554': '',
    'САНКТ ПЕТЕРБУРГ 892212335': '',
    'пфр. в московской. обл.': 'ПФР.. обл',
    'пфр в московской;': 'ПФР',
    'пфр в московской;пфр в московской': 'ПФР ПФР',
    'пфр в моско;вской': 'ПФР в моско вской',
    'пфр в мо##сковск&ой': 'ПФР в МО сковск ой',
    'пфр! в мос=ковск%ой': 'ПФР в мос ковск ой',
    'екатеринбург лрчсдлрм': 'лрчсдлрм',
    'Екатеринбург адлопа': 'адлопа',
    'упк по ямало-ненецкому': 'УПК',
    'столица карачаево-черкесской': 'столица',
    'санкт_петербург': '',
    '8-912-623-2555': '',
    '8(912)62-32-555': '',
    '8912.623.25.55': '8912.623.25.55',
}


class Test(unittest.TestCase):
    def test(self):
        for key, value in sentence.items():
            args = [
                'curl',
                '{}/cgi-bin/cleanup.py?{}'.format(
                    tokens.local_server,
                    urlencode({'query': key})
                )
            ]
            modified_key = subprocess.check_output(args).decode()
            self.assertIn(value, modified_key)


if __name__ == '__main__':
    unittest.main()
