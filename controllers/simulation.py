#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

from routes import routers

dbSimulation = mongoOP.OpMongoDB('worldcup2018','simulacao')

def getSimulations(id, dados):
	return dbSimulation.findSimulationByIdUser(id)

def createSimulation(dados):
	pass
	# return dbSimulation.saveIW(dados)

def createSimulationGroup(dados, iduser, idgrupo):
	response = {}
	print (idgrupo)
	t = routers.getIdPartida2(11)
	print (t)
	print (t['rodada'])
	# matchAtual = routers.getIdPartida2(int(idgrupo))
	# matchAtual['data'] = routers.getIdPartida2(idgrupo)

	# print (dumps(matchAtual))
	# print (matchAtual['data'])

	try:
		# dados['gols_b'] = matchAtual['data']
		# dados['gols_a'] = matchAtual['rodada']
		response = dbSimulation.collection.insert(dados)
		# self.collection.insert_one({"dados":1})
	except:
		response = {
			"Error": True,
			"Message": "FAIL"
		}
	return response
