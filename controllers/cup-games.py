#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

dbteam = mongoOP.OpMongoDB('worldcup2018','selecao')
# dbuser = mongoOP.OpMongoDB('world-cup-20018', 'users')


def createFosseis( dados):
    return dbteam.save(dados)

def uploadFosseis(id,dados):
    return dbteam.upload(id, dados)

def deleteFosseis(id):
    return dbteam.remove(id)

def listTeams():
    return dbteam.list()

def getTeam(id):
    return dbteam.findById(id)

def addLoc(id, dados):
    return dbteam.patch(id, dados)
