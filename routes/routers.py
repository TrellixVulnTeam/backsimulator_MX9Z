# -*- coding: utf-8 -*-

# Este modulo carrega todas as funções do flask

from flask import Flask, request
from flask_cors import CORS, cross_origin
from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from bson.objectid import ObjectId
from bson.json_util import dumps
from bson.errors import InvalidId
from flask import jsonify


class ObjectIDConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(base64_decode(value))
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()
    def to_url(self, value):
        return base64_encode(value.binary)


# Importando controller de teste
from controllers import user
from controllers import cupgames

import json

# Flask app
application = Flask(__name__)
application.url_map.converters['objectid'] = ObjectIDConverter
CORS(application)
# Rota index para teste


@application.route("/", methods=['GET'])
def ctrlRoot():
    return "<h1>World Cup Simulator 2018</h1> <p>Web Service</p><a href='http://world-cup-20018.herokuapp.com/'>Link Externo</a>"




"""
----------------------------------------------------
                    USER
----------------------------------------------------
"""



def getIdSelecao2(idselecao):

    if (request.method == "GET"):
        res = cupgames.getTeam(idselecao,request.json)
        return res



@application.route("/user", methods=['POST','GET'])
# Função da rota indextree
def ctrlUser():

    if (request.method == 'POST'):
        res = user.createUser(request.json)
        return dumps(request.json)

    elif (request.method == 'GET'):
        res = user.listUser()
        return dumps(res)

@application.route('/user/<iduser>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdUser(iduser):

    if (request.method == "GET"):
        res = user.getUser(iduser,request.json)
        return dumps(res)

    elif (request.method == 'DELETE'):
        res = user.deleteUser(iduser,request.json)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = user.uploadUser(iduser,request.json)
        return dumps(res)

    elif (request.method == 'PATCH'):
        res = user.patchUser(iduser,request.json)
        return dumps(res)

@application.route('/selecao/<idselecao>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdSelecao(idselecao):

    if (request.method == "GET"):
        res = cupgames.getTeam(idselecao,request.json)
        return dumps(res)

    elif (request.method == 'DELETE'):
        res = cupgames.deleteTeam(idselecao,request.json)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = cupgames.uploadTeams(idselecao,request.json)
        return dumps(res)

################# PARTIDA e SIMULACAO #####################
@application.route("/hello", methods=['GET'])
def hello():
    if (request.method == 'GET'):
        return "hello"

@application.route("/selecao", methods=['POST','GET'])
# Função da rota indextree
def ctrlSelecao():

    if (request.method == 'POST'):
        res['id_selecao']=1;
        res = cupgames.createTeam(request.json)
        return dumps(request.json)

    elif (request.method == 'GET'):
        res = cupgames.listTeam()
        print (res)
        return dumps(res)

@application.route("/partida", methods=['POST','GET'])
# Função da rota indextree
def ctrlPartida():

    if (request.method == 'POST'):

        res = cupgames.createMatch(request.json)
        return dumps(request.json)

    elif (request.method == 'GET'):
        res = cupgames.listMatch()
        return dumps(res)




@application.route("/simulacao", methods=['POST','GET'])
# Função da rota indextree
def postSimulation():

    if (request.method == 'POST'):
        res = cupgames.uploadSimulation(request.json)
        return dumps(res)



@application.route('/simulacao/<iduser>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdSimulation(iduser):

    if (request.method == "GET"):
        res = cupgames.getSimulations(iduser,request.json)
        return dumps(res)
    # elif (request.method == 'POST'):
    #     res = cupgames.uploadSimulation(request.json)
    #     return dumps(request.json)

    # elif (request.method == 'DELETE'):
    #     res = cupgames.deleteTeam(idselecao,request.json)
    #     return dumps(res)

    # elif (request.method == 'PUT'):
    #     res = cupgames.uploadTeams(idselecao,request.json)
    #     return dumps(res)
