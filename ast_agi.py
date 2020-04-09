#!/usr/bin/env python2.7
import sys
from asterisk.agi import *
from settings import proj_folder
#Criando objetos
agi = AGI()
#funcoes
#Logica CPF

def gravacao_CPF():
	agi.stream_file(proj_folder + '/informe_cpf')
	agi.stream_file('beep')
	agi.appexec('Read','CPF1')
	CPF = agi.get_variable('CPF1')
	result = {}

ANI = agi.env['agi_callerid']
agi.set_variable('ANI',ANI)
agi.verbose("Origem: %s" % ANI)
agi.stream_file(proj_folder + '/bem_vindo')	
sys.exit()

