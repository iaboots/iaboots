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


import aiml

n = aiml.Kernel()
n.learn("bot/aiml/iabots/startup.xml")
n.respond("LOAD IABOTS")

v = aiml.Kernel()
v.learn("bot/aiml/vendedor/startup.xml")
v.respond("LOAD VENDEDOR")

a = aiml.Kernel()
a.learn("bot/aiml/asistencia/startup.xml")
a.respond("LOAD ASISTENCIA")

class iabot:
	def responde(self, text, numbot=1):
		if numbot is 1:
			return n.respond(text)
		elif numbot is 2:
			return v.respond(text)
		else:
			return a.respond(text)