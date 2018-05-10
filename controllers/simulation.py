#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP
from operator import itemgetter

from routes import routers

dbSimulation = mongoOP.OpMongoDB('worldcup2018','simulacao')

def getSimulations(id, dados):
	return dbSimulation.findSimulationByIdUser(id)

def simulateGroup(dados, idgrupo):

	response = {}
	# data = [{'id_selecao':0, 'qtd_jogos':0, 'num_vitorias':0,'num_empates':0,'num_derrotas':0,'pontos':0,'gols_pro':0,'gols_sofridos':0,'saldo_gols':0}]
	data = [{},{},{},{}]
	#ids da partida
	# grupoIdPartida = {"A": [1,2,17,18,33,34], "B": [3,4,19,20,35,36], "C":[5,6,21,22,37,38], "D":[7,8,23,24,39,40], "E":[10,9,25,26,41,42], "F":[12,11,27,28,43,44], "G":[13,14,30,29,45,46], "H":[16,15,31,32,47,48] }

	teamsByGroup = routers.getIdGrupo2(idgrupo)

	for x in range(0,4):
		# print (teamsByGroup['Data'][x])
		data[x]['id_selecao'] = teamsByGroup['Data'][x]['id_selecao']
		data[x]['qtd_jogos'] = teamsByGroup['Data'][x]['qts_jogos']
		data[x]['num_vitorias'] = teamsByGroup['Data'][x]['vitorias']
		data[x]['num_empates'] = teamsByGroup['Data'][x]['empates']
		data[x]['num_derrotas'] = teamsByGroup['Data'][x]['derrotas']
		data[x]['pontos'] = teamsByGroup['Data'][x]['pontos']
		data[x]['gols_pro'] = teamsByGroup['Data'][x]['gols_pro']
		data[x]['gols_sofridos'] = teamsByGroup['Data'][x]['gols_sofrido']
		data[x]['saldo_gols'] = teamsByGroup['Data'][x]['saldo_gols']


	for x in range(0,6):

		matchAtual = routers.getIdPartida2(dados['data'][x]['id_partida'])

		for y in range(0,4):

			if (data[y]['id_selecao'] == matchAtual['data']['selecao_a']):
				data[y]['qtd_jogos'] += 1
				data[y]['gols_pro'] += dados['data'][x]['selecao_a'][0]['gols']
				data[y]['gols_sofridos'] += dados['data'][x]['selecao_b'][0]['gols']
				data[y]['saldo_gols'] = data[y]['gols_pro'] - data[y]['gols_sofridos']

				if dados['data'][x]['selecao_a'][0]['gols']>dados['data'][x]['selecao_b'][0]['gols']:
					data[y]['num_vitorias'] += 1
				elif dados['data'][x]['selecao_a'][0]['gols']<dados['data'][x]['selecao_b'][0]['gols']:
					data[y]['num_derrotas'] += 1
				else:
					data[y]['num_empates'] += 1


			if (data[y]['id_selecao'] == matchAtual['data']['selecao_b']):
				data[y]['qtd_jogos'] += 1
				data[y]['gols_pro'] += dados['data'][x]['selecao_b'][0]['gols']
				data[y]['gols_sofridos'] += dados['data'][x]['selecao_a'][0]['gols']
				data[y]['saldo_gols'] = data[y]['gols_pro'] - data[y]['gols_sofridos']

				if dados['data'][x]['selecao_b'][0]['gols']>dados['data'][x]['selecao_a'][0]['gols']:
					data[y]['num_vitorias'] += 1
				elif dados['data'][x]['selecao_b'][0]['gols']<dados['data'][x]['selecao_a'][0]['gols']:
					data[y]['num_derrotas'] += 1
				else:
					data[y]['num_empates'] += 1

			data[y]['pontos'] = (data[y]['num_vitorias']*3)+data[y]['num_empates']

		# print (dados['data'][x])

	print (data)
	ordem = sorted(data, key=itemgetter('pontos', 'saldo_gols', 'gols_pro'),reverse=True) #Regra 1 e 2

	try:

		response = {
			"Error": False,
			"Message": ordem
		}
		# response = dbSimulation.collection.insert()

	except:
		response = {
			"Error": True,
			"Message": "FAIL"
		}
	return response
