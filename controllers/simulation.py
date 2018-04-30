#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

dbSimulation = mongoOP.OpMongoDB('worldcup2018','simulacao')

def getSimulations(id, dados):
	return dbSimulation.findSimulationByIdUser(id)

def createSimulation(dados):
	pass
	# return dbSimulation.saveIW(dados)

def createSimulationGroup(dados, iduser, idgrupo):
	response = {}

	try:
		dados['gols_a'] = 0
		dados['gols_b'] = 0
		response = dbSimulation.collection.insert(dados)
		# self.collection.insert_one({"dados":1})
	except:
		response = {
			"Error": True,
			"Message": "FAIL"
		}
	return response
