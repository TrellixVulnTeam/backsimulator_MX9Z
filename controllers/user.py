#importando o documento Tree
# -*- coding: utf-8 -*-
from models import mongoOP
import pymongo
from controllers import team
from controllers import match

dbuser = mongoOP.OpMongoDB('worldcup2018', 'usuario')

# dbuser.collection.create_index([("email", pymongo.ASCENDING)], unique=True)

def createUser(id,dados):

    if dbuser.findUser(dados['id'])==True:
        print ("tem")
    else:
        return dbuser.save(dados)
        print ("nao tem")


def saveSimulation(id,dados):
    return dbuser.saveSimulation(id,dados)

def getSimulation(id):
    return dbuser.getSimulation(id)

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

##########################
def teste(dados):
    return dbuser.saveIW(dados)
