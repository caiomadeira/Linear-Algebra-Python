import time

import requests
import json
from constants import cnpj


def get_data(data):
    count = 0
    url = f"https://receitaws.com.br/v1/cnpj/{data}"
    query = {"token": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
             "cnpj": '06990590000123',
             "plugin": 'RF'}
    response = requests.request("GET", url, params=query)
    time.sleep(1.5)
    print(response.status_code)

    if response.status_code == 200:
        resp = json.loads(response.text)
        return [resp['nome'], resp['situacao'], resp['abertura'], resp['cnpj'], resp['capital_social']]
    else:
        return None


