from urllib.parse import urlencode
import subprocess
import unittest
import tokens, cleanup


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
    'как добраться в евпаторию': 'как добраться',
    'получить внж гражданину казахстана': 'получить ВНЖ гражданину',
    'получить дмс': 'получить ДМС',
    'внж россии': 'ВНЖ России',
}


remote = '{}/cgi-bin/cleanup.py?'.format(tokens.remote_server)
local = '{}/VU_keys/cleanup.py?'.format(tokens.local_server)


class Test(unittest.TestCase):
    def test_main(self):
        for key, value in sentence.items():
            with self.subTest():
                args = [
                    'curl',
                    '{}{}'.format(remote, urlencode({'query': key}))
                ]
                modified_key = subprocess.check_output(args).decode()
                self.assertIn(value, modified_key)

#    def test_remove_symbols(self):
#        for key, value in sentence.items():
#            with self.subTest():
#                keyword =
#                cleanup.remove_symbols(key)%20%D0%BF%D0%BE%20%D1%8F%D0%BC%D0%B0%D0%BB%D0%BE-%D0%BD%D0%B5%D0%BD%D0%B5%D1%86%D0%BA%D0%BE%D0%BC%D1%83
#                self.assertEqual(value,

if __name__ == '__main__':
    unittest.main()


'''
url encoded phrases for manual test

%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%B3%D1%80%D0%B0%D0%B6%D0%B4%D0%B0%D0%BD%D0%B8%D0%BD%D1%83%20%D0%BA%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD%D0%B0

%D0%BF%D1%84%D1%80%20%D0%B2%20%D0%9C%D0%BE%D1%81%D0%BA%D0%BE%D0%B2%D1%81%D0%BA%D0%BE%D0%B9%20%D0%BE%D0%B1%D0%BB%0D%0A

c%D0%B0%D0%BD%D0%BA%D1%82%20%D0%BF%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%209221233554%0D%0A

%D1%83%D0%BF%D0%BA%20%D0%BF%D0%BE%20%D1%8F%D0%BC%D0%B0%D0%BB%D0%BE-%D0%BD%D0%B5%D0%BD%D0%B5%D1%86%D0%BA%D0%BE%D0%BC%D1%83

%D1%81%D1%82%D0%BE%D0%BB%D0%B8%D1%86%D0%B0%20%D0%BA%D0%B0%D1%80%D0%B0%D1%87%D0%B0%D0%B5%D0%B2%D0%BE-%D1%87%D0%B5%D1%80%D0%BA%D0%B5%D1%81%D1%81%D0%BA%D0%BE%D0%B9

%D0%B2%D0%BD%D0%B6%20%D1%80%D0%BE%D1%81%D1%81%D0%B8%D0%B8%27

'''
