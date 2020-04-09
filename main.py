#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from asterisk.agi import *
from functions import validar, api
from settings import proj_folder


#Criando objetos
agi = AGI()

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
agi.verbose("Resposta: %s" % r.text)

if r.status_code == 200:
    agi.verbose("Tratando resposta")
    
    try: 
        dados = validar.dados(json.loads(r.text))
        agi.verbose(str(dados))
    except:
        dados = {
            'ecliente' : 'N',
            'sinistro' :'N',
            'inadimplente' : 'N'
        }
        agi.verbose("Dados recebidos em um formato invalido")

    agi.verbose("Setando variaveis")
    #Setando variaveis no Asterisk
    agi.set_variable('_ECLIENTE',dados['ecliente'])
    agi.set_variable('_SINISTRO',dados['sinistro'])
    agi.set_variable('_INADIMPLENTE',dados['inadimplente'])
    agi.verbose("Finalizado script")

sys.exit()
