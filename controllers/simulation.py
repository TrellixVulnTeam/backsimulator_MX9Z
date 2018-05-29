#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP
from operator import itemgetter

from routes import routers

dbSimulation = mongoOP.OpMongoDB('worldcup2018','simulacao')
dbteam = mongoOP.OpMongoDB('worldcup2018','selecao')

def simulate1(dados):

	#partidas das oitavas 49 a 56
	# response = [{},{},{},{},{},{},{},{}]
	partidas = []


	i = 0
	for x in range(49,57):
		partida = routers.getIdPartida2(x)
		partidas.append(partida['data'])
		partidas[i]['selecao_a'] = ""
		partidas[i]['selecao_b'] = ""
		partidas[i]['gols_a'] = ""
		partidas[i]['gols_b'] = ""
		i+=1


	if ("grupoA" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoA'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoA'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[0]['selecao_a'] = teamA
		partidas[2]['selecao_b'] = teamB

	if ("grupoB" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoB'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoB'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[0]['selecao_b'] = teamA
		partidas[2]['selecao_a'] = teamB

	if ("grupoC" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoC'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoC'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[1]['selecao_a'] = teamA
		partidas[3]['selecao_b'] = teamB

	if ("grupoD" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoD'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoD'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[1]['selecao_b'] = teamA
		partidas[3]['selecao_a'] = teamB

	if ("grupoE" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoE'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoE'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[4]['selecao_a'] = teamA
		partidas[6]['selecao_b'] = teamB

	if ("grupoF" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoF'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoF'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[4]['selecao_b'] = teamA
		partidas[6]['selecao_a'] = teamB

	if ("grupoG" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoG'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoG'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[5]['selecao_a'] = teamA
		partidas[7]['selecao_b'] = teamB

	if ("grupoH" in dados):

		fullTeamA = dbteam.findTeam(dados['grupoH'][0]['id_selecao'])
		fullTeamB = dbteam.findTeam(dados['grupoH'][1]['id_selecao'])

		teamA = {"id_selecao":0,"nome":"","bandeira":""}
		teamB = {"id_selecao":0,"nome":"","bandeira":""}

		teamA['id_selecao'] = fullTeamA['data']['id_selecao']
		teamA['nome'] = fullTeamA['data']['nome']
		teamA['bandeira'] = fullTeamA['data']['bandeira']

		teamB['id_selecao'] = fullTeamB['data']['id_selecao']
		teamB['nome'] = fullTeamB['data']['nome']
		teamB['bandeira'] = fullTeamB['data']['bandeira']

		partidas[5]['selecao_b'] = teamA
		partidas[7]['selecao_a'] = teamB

	return partidas

def simulate2(dados):

	#partidas das oitavas 49 a 56
	# response = [{},{},{},{},{},{},{},{}]
	partidas = []
	fullTeam = [{},{},{},{},{},{},{},{}]
	team = [{},{},{},{},{},{},{},{}]

	i = 0
	for x in range(57,61):
		partida = routers.getIdPartida2(x)
		partidas.append(partida['data'])
		partidas[i]['selecao_a'] = ""
		partidas[i]['selecao_b'] = ""
		partidas[i]['gols_a'] = ""
		partidas[i]['gols_b'] = ""
		i+=1

	for x in range(0,8):

		if dados[x]=={}:
			team[x] = ""
		else:
			fullTeam[x] = dbteam.findTeam(dados[x]['id_selecao'])
			team[x] = {"id_selecao":0,"nome":"","bandeira":""}
			team[x]['id_selecao'] = fullTeam[x]['data']['id_selecao']
			team[x]['nome'] = fullTeam[x]['data']['nome']
			team[x]['bandeira'] = fullTeam[x]['data']['bandeira']


	partidas[0]['selecao_a'] = team[0]
	partidas[0]['selecao_b'] = team[1]

	partidas[1]['selecao_a'] = team[2]
	partidas[1]['selecao_b'] = team[3]

	partidas[2]['selecao_a'] = team[4]
	partidas[2]['selecao_b'] = team[5]

	partidas[3]['selecao_a'] = team[6]
	partidas[3]['selecao_b'] = team[7]


	return partidas

def simulate3(dados):

	#partidas das oitavas 49 a 56
	# response = [{},{},{},{},{},{},{},{}]
	partidas = []
	fullTeam = [{},{},{},{}]
	team = [{},{},{},{}]

	i = 0
	for x in range(61,63):
		partida = routers.getIdPartida2(x)
		partidas.append(partida['data'])
		partidas[i]['selecao_a'] = ""
		partidas[i]['selecao_b'] = ""
		partidas[i]['gols_a'] = ""
		partidas[i]['gols_b'] = ""
		i+=1

	for x in range(0,4):

		if dados[x]=={}:
			team[x] = ""
		else:
			fullTeam[x] = dbteam.findTeam(dados[x]['id_selecao'])
			team[x] = {"id_selecao":0,"nome":"","bandeira":""}
			team[x]['id_selecao'] = fullTeam[x]['data']['id_selecao']
			team[x]['nome'] = fullTeam[x]['data']['nome']
			team[x]['bandeira'] = fullTeam[x]['data']['bandeira']

	print (partidas)

	partidas[0]['selecao_a'] = team[0]
	partidas[0]['selecao_b'] = team[1]

	partidas[1]['selecao_a'] = team[2]
	partidas[1]['selecao_b'] = team[3]

	return partidas

def simulate4(dados):

	#partidas das oitavas 49 a 56
	# response = [{},{},{},{},{},{},{},{}]
	partidas = []
	fullTeam = [{},{},{},{}]
	team = [{},{},{},{}]

	i = 0
	for x in range(63,65):
		partida = routers.getIdPartida2(x)
		partidas.append(partida['data'])
		partidas[i]['selecao_a'] = ""
		partidas[i]['selecao_b'] = ""
		partidas[i]['gols_a'] = ""
		partidas[i]['gols_b'] = ""
		i+=1

	for x in range(0,4):

		if dados[x]=={}:
			team[x] = ""
		else:
			fullTeam[x] = dbteam.findTeam(dados[x]['id_selecao'])
			team[x] = {"id_selecao":0,"nome":"","bandeira":""}
			team[x]['id_selecao'] = fullTeam[x]['data']['id_selecao']
			team[x]['nome'] = fullTeam[x]['data']['nome']
			team[x]['bandeira'] = fullTeam[x]['data']['bandeira']

	print (partidas)

	partidas[0]['selecao_a'] = team[0]
	partidas[0]['selecao_b'] = team[1]

	partidas[1]['selecao_a'] = team[2]
	partidas[1]['selecao_b'] = team[3]

	return partidas



def getSimulations(id, dados):
	return dbSimulation.findSimulationByIdUser(id)

def simulateGroup(dados, idgrupo):

	response = {}
	# data = [{'id_selecao':0, 'qtd_jogos':0, 'num_vitorias':0,'num_empates':0,'num_derrotas':0,'pontos':0,'gols_pro':0,'gols_sofridos':0,'saldo_gols':0}]
	data = [{},{},{},{}]
	# ids da partida
	# grupoIdPartida = {"A": [1,2,17,18,33,34], "B": [3,4,19,20,35,36], "C":[5,6,21,22,37,38], "D":[7,8,23,24,39,40], "E":[10,9,25,26,41,42], "F":[12,11,27,28,43,44], "G":[13,14,30,29,45,46], "H":[16,15,31,32,47,48] }

	teamsByGroup = routers.getIdGrupo2(idgrupo)

	for x in range(0,4):
		# print (teamsByGroup['Data'][x])
		data[x]['id_selecao'] = teamsByGroup['Data'][x]['id_selecao']
		data[x]['nome'] = teamsByGroup['Data'][x]['nome']
		data[x]['bandeira'] = teamsByGroup['Data'][x]['bandeira']
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
		matchAtual['data']['gols_a'] = ""
		matchAtual['data']['gols_b'] = ""

		for y in range(0,4):

			if (dados['data'][x]['selecao_a'][0]['gols'] != "" and dados['data'][x]['selecao_b'][0]['gols'] != ""):

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
				team = dbteam.findTeam(data[y]['id_selecao'])
				data[y]['nome'] = team['data']['nome']
				data[y]['bandeira'] = team['data']['bandeira']

			else:
				pass
				# data[x]['id_selecao'] = teamsByGroup['Data'][x]['id_selecao']
				# data[x]['qtd_jogos'] = null
				# data[x]['num_vitorias'] = "-"
				# data[x]['num_empates'] = "-"
				# data[x]['num_derrotas'] = "-"
				# data[x]['pontos'] = "-"
				# data[x]['gols_pro'] = "-"
				# data[x]['gols_sofridos'] = "-"
				# data[x]['saldo_gols'] = "-"

		# print (dados['data'][x])

	print (data)
	ordem = sorted(data, key=itemgetter('pontos', 'saldo_gols', 'gols_pro'),reverse=True) #Regra 1 e 2

	for y in range(0,4):
		if (data[y]['qtd_jogos']==0):
			data[y]['qtd_jogos'] = "-"
			data[y]['num_vitorias'] = "-"
			data[y]['num_empates'] = "-"
			data[y]['num_derrotas'] = "-"
			data[y]['pontos'] = "-"
			data[y]['gols_pro'] = "-"
			data[y]['gols_sofridos'] = "-"
			data[y]['saldo_gols'] = "-"

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
