#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
from asterisk.agi import *
from settings import proj_folder
#Criando objetos
agi = AGI()
#funcoes
#Logica CPF

<<<<<<< HEAD

agi.stream_file(proj_folder + '/bem_vindo')	
=======
ANI = agi.env['agi_callerid']
agi.set_variable('ANI',ANI)
agi.verbose("Origem: %s" % ANI)
agi.stream_file(proj_folder + '/audios/bem_vindo')	
>>>>>>> b59c8201bb3eae3d1cf93d8f215a0617d27b2ec4
sys.exit()

