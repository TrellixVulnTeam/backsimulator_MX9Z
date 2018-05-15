#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

dbteam = mongoOP.OpMongoDB('worldcup2018','selecao')
dbMatch = mongoOP.OpMongoDB('worldcup2018','partida')

def getGroup(letter, dados):

    response = {}
    #ids da partida
    grupoIdPartida = {"A": [1,2,17,18,33,34], "B": [3,4,19,20,35,36], "C":[5,6,21,22,37,38], "D":[7,8,23,24,39,40], "E":[10,9,25,26,41,42], "F":[12,11,27,28,43,44], "G":[13,14,30,29,45,46], "H":[16,15,31,32,47,48] }

    jsonTeams = dbteam.findGroup(letter)

    jsonMatches = [{"rodada1":[]},{"rodada2":[]},{"rodada3":[]}]

    contador_rodada1 = 0
    contador_rodada2 = 0
    contador_rodada3 = 0

    for id in grupoIdPartida[letter]:

        match = dbMatch.findMatchById(id)


        if (match['data']['rodada']==1):

            jsonMatches[0]['rodada1'].append(match['data'])

            query_teamA = dbteam.findTeam(match['data']['selecao_a'])
            query_teamB = dbteam.findTeam(match['data']['selecao_b'])
            teamA = {'id_selecao' : query_teamA['data']['id_selecao'], 'nome' : query_teamA['data']['nome'], 'bandeira': query_teamA['data']['bandeira']}
            teamB = {'id_selecao' : query_teamB['data']['id_selecao'], 'nome' : query_teamB['data']['nome'], 'bandeira': query_teamB['data']['bandeira']}

            jsonMatches[0]['rodada1'][contador_rodada1]['selecao_a'] = teamA
            jsonMatches[0]['rodada1'][contador_rodada1]['selecao_b'] = teamB

            contador_rodada1 += 1

        elif (match['data']['rodada']==2):

            jsonMatches[1]['rodada2'].append(match['data'])

            query_teamA = dbteam.findTeam(match['data']['selecao_a'])
            query_teamB = dbteam.findTeam(match['data']['selecao_b'])
            teamA = {'id_selecao' : query_teamA['data']['id_selecao'], 'nome' : query_teamA['data']['nome'], 'bandeira': query_teamA['data']['bandeira']}
            teamB = {'id_selecao' : query_teamB['data']['id_selecao'], 'nome' : query_teamB['data']['nome'], 'bandeira': query_teamB['data']['bandeira']}

            jsonMatches[1]['rodada2'][contador_rodada2]['selecao_a'] = teamA
            jsonMatches[1]['rodada2'][contador_rodada2]['selecao_b'] = teamB

            contador_rodada2 += 1

        else:

            jsonMatches[2]['rodada3'].append(match['data'])

            query_teamA = dbteam.findTeam(match['data']['selecao_a'])
            query_teamB = dbteam.findTeam(match['data']['selecao_b'])
            teamA = {'id_selecao' : query_teamA['data']['id_selecao'], 'nome' : query_teamA['data']['nome'], 'bandeira': query_teamA['data']['bandeira']}
            teamB = {'id_selecao' : query_teamB['data']['id_selecao'], 'nome' : query_teamB['data']['nome'], 'bandeira': query_teamB['data']['bandeira']}

            jsonMatches[2]['rodada3'][contador_rodada3]['selecao_a'] = teamA
            jsonMatches[2]['rodada3'][contador_rodada3]['selecao_b'] = teamB

            contador_rodada3 += 1


    try:

        response = {
            "Error": False,
            "selecoes": jsonTeams['Data'],
            "partidas": jsonMatches

        }
        # response = dbSimulation.collection.insert()

    except:
        response = {
            "Error": True,
            "Message": "FAIL"
        }

    return response
