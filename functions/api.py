import requests
from settings import url_api

def get(CPF):
    url = url_api + str(CPF)
    r = requests.get(url=url)
    return r 