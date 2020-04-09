import requests

url_api = 'http://54.94.135.76:82/autoteste/pabx.asp?cpf='

def get(CPF):
    url = url_api + str(CPF)
    r = requests.get(url=url)
    return r 