#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoOP
import pymongo
# from controllers import team
# from controllers import match

dbuser = mongoOP.OpMongoDB('worldcup2018', 'usuario')

# dbuser.collection.create_index([("email", pymongo.ASCENDING)], unique=True)

def createUser(dados):
    print(dados)
    team = team.listTeam()
    matches = match.listMatch()

    for match in matches:
        print(match)
    return dbuser.save(dados)

def uploadUser(id, dados):
    return dbuser.upload(id, dados)

def patchUser(id, dados):
    return dbuser.patch(id,dados)

def deleteUser(id):
    return dbuser.remove(id)

def listUser():
    return dbuser.list()

def getUser(id):
    return dbuser.findById(id)
