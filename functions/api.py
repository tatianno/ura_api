import requests

url_api = 'http://servidor/autoteste/pabx.asp?cpf='

def get(CPF):
    url = url_api + str(CPF)
    r = requests.get(url=url)
    return r 