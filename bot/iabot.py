#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Proyecto: iaboots
Autores: 
Yoandre Saavedra Gonzalez


Funcion: 	App de  la IA.
Requisito: Necesario para que de respuestas

Creación: 21-05-2016
Actualización: 22-05-2016
1. bot normal
2. bot vendedor
"""


import aiml, os
from os.path import join

n = aiml.Kernel()
n.learn("iaboots/bot/aiml/iabots/startup.xml")
n.respond("LOAD IABOTS")

v = aiml.Kernel()
v.learn("iaboots/bot/aiml/vendedor/startup.xml")
v.respond("LOAD VENDEDOR")

a = aiml.Kernel()
a.learn("iaboots/bot/aiml/asistencia/startup.xml")
a.respond("LOAD ASISTENCIA")

sPath = 'MEMORIA'
fichero = 'memory.stxt'
if not os.path.exists(sPath):
	os.mkdir(sPath)

class iabot:
	f = None
	def __init__(self):
		self.f = open(join(sPath, fichero), 'a')

	def responde(self, text, numbot=1):
		self.f.write(text+'\n')
		if numbot is 1:
			return n.respond(text)
		elif numbot is 2:
			return v.respond(text)
		else:
			return a.respond(text)