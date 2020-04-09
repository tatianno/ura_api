#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
from asterisk.agi import *
from settings import proj_folder
#Criando objetos
agi = AGI()
#funcoes
#Logica CPF

ANI = agi.env['agi_callerid']
agi.set_variable('ANI',ANI)
agi.verbose("Origem: %s" % ANI)
agi.stream_file(proj_folder + '/audios/bem_vindo')	
sys.exit()

