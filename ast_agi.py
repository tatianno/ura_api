#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import requests
import json
from asterisk.agi import *
from settings import proj_folder

#Criando objetos
agi = AGI()

#funcoes
def get_api(CPF):
    url = 'http://54.94.135.76:82/autoteste/pabx.asp?cpf=' + str(CPF)
    r = requests.get(url=url)
    agi.verbose("Resultado GET: %s" % r)

#Logica CPF
ANI = agi.env['agi_callerid']
agi.set_variable('_ANI',ANI)
agi.verbose("Origem: %s" % ANI)
agi.stream_file(proj_folder + '/audios/cpf_conv')
agi.stream_file('beep')
agi.appexec('Read','_CPF')
CPF = agi.get_variable('CPF')
get_api(CPF)
sys.exit()
