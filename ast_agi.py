#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from asterisk.agi import *
from functions import validar, api
from settings import proj_folder


#Criando objetos
agi = AGI()

def encaminhar_vendas():
    agi.verbose("Encaminhando a chamada para o grupo de vendas")
    agi.appexec('Goto','${VENDAS_DST}')


#Logica CPF
ANI = agi.env['agi_callerid']
agi.set_variable('_ANI',ANI)
agi.verbose("Origem: %s" % ANI)
agi.stream_file(proj_folder + '/audios/cpf_conv')
agi.stream_file('beep')
agi.appexec('Read','_CPF')
CPF = agi.get_variable('CPF')


#Enviando requisicao para obter dados do CPF informado
r = api.get(CPF)
agi.verbose("Resultado GET: %s" % r.status_code)
if r.status_code == 200:
    dados = validar.dados(json.loads(r.text))
    #Setando variaveis no Asterisk
    agi.set_variable('_ECLIENTE',dados['ecliente'])
    agi.set_variable('_SINISTRO',dados['SINISTRO'])
    agi.set_variable('_INADIMPLENTE',dados['INADIMPLENTE'])

    if dados['ecliente']:
        #Caso seja cliente
        agi.verbose("Cliente localizado")


    else:
        #Caso não seja cliente
        agi.verbose("Cliente nao localizado")
        encaminhar_vendas()

else:
    #Caso ocorra erro na comunicacao
    agi.verbose("Falha na comunicacao com a API")
    encaminhar_vendas()

sys.exit()
