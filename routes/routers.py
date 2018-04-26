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


# Importando controllers
from controllers import user
from controllers import team
from controllers import simulation
from controllers import match


import json

# Flask app
application = Flask(__name__)
application.url_map.converters['objectid'] = ObjectIDConverter
CORS(application)
# Rota index para teste


@application.route("/", methods=['GET'])
def ctrlRoot():
    return "<h1>World Cup Simulator 2018FF</h1> <p>Web Service</p><a href='http://world-cup-20018.herokuapp.com/'>Front</a>"




"""
----------------------------------------------------
                    USER
----------------------------------------------------
"""

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

"""
----------------------------------------------------
                    SIMULATION
----------------------------------------------------
"""

@application.route("/simulacao", methods=['POST','GET'])
# Função da rota indextree
def postSimulation():

    if (request.method == 'POST'):
        res = simulation.createSimulation(request.json)
        return dumps(res)


@application.route('/simulacao/<iduser>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdSimulation(iduser):

    if (request.method == "GET"):
        res = simulation.getSimulations(iduser,request.json)
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

"""
----------------------------------------------------
                    TEAM
----------------------------------------------------
"""
@application.route("/selecao", methods=['POST','GET'])
# Função da rota indextree
def ctrlSelecao():

    if (request.method == 'POST'):
        res['id_selecao']=1;
        res = team.createTeam(request.json)
        return dumps(request.json)

    elif (request.method == 'GET'):
        res = team.listTeam()
        print (res)
        return dumps(res)


def getIdSelecao2(idselecao):

    if (request.method == "GET"):
        res = team.getTeam(idselecao,request.json)
        return res

@application.route('/selecao/<idselecao>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdSelecao(idselecao):

    if (request.method == "GET"):
        res = team.getTeam(idselecao,request.json)
        return dumps(res)

    elif (request.method == 'DELETE'):
        res = team.deleteTeam(idselecao,request.json)
        return dumps(res)

    elif (request.method == 'PUT'):
        res = team.uploadTeams(idselecao,request.json)
        return dumps(res)


# @application.route("/selecao", methods=['POST','GET'])
# # Função da rota indextree
# def ctrlSelecao():
#
#     if (request.method == 'POST'):
#         res['id_selecao']=1;
#         res = team.createTeam(request.json)
#         return dumps(request.json)
#
#     elif (request.method == 'GET'):
#         res = team.listTeam()
#         print (res)
#         return dumps(res)

"""
----------------------------------------------------
                    MATCH
----------------------------------------------------
"""

@application.route("/partida", methods=['POST','GET'])
# Função da rota indextree
def ctrlPartida():

    if (request.method == 'POST'):
        res = match.createMatch(request.json)
        return dumps(request.json)

    elif (request.method == 'GET'):
        res = match.listMatch()
        return dumps(res)


############################################
################## grupos ##################
############################################

@application.route('/grupo/<idgrupo>',  methods=['GET', 'DELETE', 'PUT', 'PATCH'])
def getIdSelecao(idgrupo):

    if (request.method == "GET"):
        res = team.getGroup(idgrupo,request.json)
        return dumps(res)