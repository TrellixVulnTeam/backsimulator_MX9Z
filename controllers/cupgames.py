#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

dbteam = mongoOP.OpMongoDB('worldcup2018','selecao')
dbMatch = mongoOP.OpMongoDB('worldcup2018','partida')
dbSimulation = mongoOP.OpMongoDB('worldcup2018','simulacao')

def createTeam(dados):
    return dbteam.save(dados)

def uploadTeams(id,dados):
    return dbteam.upload(id, dados)

def deleteTeam(id):
    return dbteam.remove(id)

def listTeam():
    return dbteam.listSort()

def getTeam(id,dados):
    return dbteam.findTeam(id)
    # return dbteam.findById(id)

def addLoc(id, dados):
    return dbteam.patch(id, dados)

########################

# def listMatch():
#     return dbMatch.list()
def listMatch():
    return dbMatch.listarSelecoes()

def createMatch():
    pass

def getSimulations(id, dados):
	return dbSimulation.findSimulationByIdUser(id)

def createSimulation(dados):
    return dbSimulation.save(dados)
