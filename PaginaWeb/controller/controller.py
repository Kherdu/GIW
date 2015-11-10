# -*- coding: cp1252 -*-
import os, sys
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)

from model.usuario import *
from bottle import Bottle, route, run, request, response, template

@route('/login')
@route('/')
def login(msg=''):
    return template('index', msg=msg)

@route('/registro', method='GET')
def registro(msg = ''):
    return template('registro', msg=msg)

@route('/registro', method='POST')
def do_registro():
    username = request.forms.get('user')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    name = request.forms.get('name')
    dni = request.forms.get('dni')

    if password != password2:
        return registro('Las contrasenas no coinciden'.encode('utf8'))

    datos = {"nick": username,
             "password": password,
             "nombre": name,
             "dni": dni}

    insertUsuario(datos)
    
    return registro('Usuario insertado con exito')

run(host='localhost', port=8080, debug=True)
