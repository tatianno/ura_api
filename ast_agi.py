#!/usr/bin/env python2.7
import sys
from asterisk.agi import *
from settings import proj_folder
#Criando objetos
agi = AGI()
#funcoes
#Logica CPF


agi.stream_file(proj_folder + '/bem_vindo')	
sys.exit()

