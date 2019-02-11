import json, requests


city_list = [
'кыргызстан', 'таджикистан', 'казахстан', 'узбекистан', 'украина', 'беларусь',
'беларусия', 'армения', 'грузия', 'азербайджан', 'киргизия', 'молдавия', 'туркмения',
]

new_city_list = []
url = "https://ws3.morpher.ru/russian/declension"

for i in range(len(city_list)):
    s = city_list[i]

    params = dict (
        s=str(s),
        format="json",
        #token= #Не обязателен. Подробнее: http://morpher.ru/ws3/#authentication
        )

    response = requests.get(url=url, params=params)
    data = json.loads(response.text)
    new_city_list.extend([
        data.get('Р'),
        data.get('Д'),
        data.get('В'),
        data.get('Т'),
        data.get('П'),
    ])

print(new_city_list)
