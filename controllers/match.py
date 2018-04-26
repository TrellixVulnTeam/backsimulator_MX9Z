#importando o documento Tree
# -*- coding: utf-8 -*-
from bson.json_util import dumps
from models import mongoOP

dbMatch = mongoOP.OpMongoDB('worldcup2018','partida')

def listMatch():
    return dbMatch.listarSelecoes()

def createMatch():
    pass

def listMatchbyId(id):
	return dbMatch.listarSelecoesbyId(id)