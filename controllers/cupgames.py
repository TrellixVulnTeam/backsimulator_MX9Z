#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

dbteam = mongoOP.OpMongoDB('worldcup2018','selecao')
dbMatch = mongoOP.OpMongoDB('worldcup2018','partida')

def createTeam(dados):
    return dbteam.save(dados)

def uploadTeams(id,dados):
    return dbteam.upload(id, dados)

def deleteTeam(id):
    return dbteam.remove(id)

def listTeam():
    return dbteam.list()

def getTeam(id,dados):
    return dbteam.findTeam(id)
    # return dbteam.findById(id)

def addLoc(id, dados):
    return dbteam.patch(id, dados)

########################

# def listMatch():
#     return dbMatch.list()
def listMatch():
    return dbMatch.list2()

def createMatch():
    pass
