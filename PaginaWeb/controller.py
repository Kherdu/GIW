# -*- coding: cp1252 -*-
from model import usuario
from bottle import route, run, request, response, template, redirect, static_file

@route('<path:path>')
def server_static(path):
    return static_file(path, root='static')

@route('/login')
@route('/')
def login():
    
    viewData = {'userType': 'guest'}
    
    if request.get_cookie("msg"):
        viewData["msg"] = request.get_cookie("msg")
        response.set_cookie('msg', '')
        
    return template('index', data=viewData)

@route('/registro', method='GET')
def registro(msg=''):
    
    viewData = {'userType': 'guest'}
    
    if request.get_cookie("msg"):
        viewData["msg"] = request.get_cookie("msg")
        response.set_cookie('msg', '', expires=0)
        
    return template('registro', data=viewData)

@route('/registro', method='POST')
def do_registro():
    username = request.forms.get('user')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    name = request.forms.get('name')
    dni = request.forms.get('dni')

    if password != password2:
        response.set_cookie("msg", "Las contrasenas no coinciden")
        redirect("/registro")
        
    users = usuario.getUsuarioByNick(username)
    if len(users) > 0:
        response.set_cookie("msg", "Nick en uso")
        redirect("/registro") 

    datos = {"nick": username,
             "password": password,
             "nombre": name,
             "dni": dni}
    response.set_cookie("msg", "Usuario registrado")
    usuario.insertUsuario(datos)
    
    redirect("/")

@route('/login', method="POST")
def do_login():
    username = request.forms.get('user')
    password = request.forms.get('password')

    users = usuario.getUsuarioByNick(username)
    if len(users) == 0 or users[0]["password"] != password:
        response.set_cookie("msg", "Contrasena incorrecta")
        redirect("/")

    user = users[0]

    response.set_cookie("userNick", user["nick"], secret="asdf")
    response.set_cookie("userId", user["id"], secret="asdf")
    redirect("/inicio")
	
	
	
##AÑADIR JUEGO
@route('/juego', method="POST")
def do_addGame():
    nombre = request.forms.get('nombre')
    descripcion = request.forms.get('descripcion')
    
    disponible = request.forms.get('disponible')

    datos = {"nombre": nombre,
             "descripcion": descripcion,
             "disponible": disponible}
    response.set_cookie("msg", "Juego añadido")
    juego.addGame(datos)

    
    redirect("/inicio")
    
#AÑADIR PRESTAMO
@route('/prestamo', method="POST")
def do_addLoan():
    nombre = request.forms.get('juegoPrest')
    inicio = datetime.datetime.now()
    disponible = request.forms.get('disponible')
    fin = inicio + datetime.timedelta(days=7)
    user = ""
    if request.get_cookie("userId"):
        user = str(request.get_cookie("userId"))
    
    datos = {"fecha_inicio": inicio,
             "fecha_fin": fin,
             "juego_id": nombre,
             "usuario_id": user,
             "devuelto": disponible}
    response.set_cookie("msg", "Prestamo añadido")
    prestamo.addLoan(datos)

    
    redirect("/inicio")

#ELIMINAR JUEGO
@route('/juego', method="POST")
def do_deleteGame():
    id = request.forms.get('id')
    
    datos = {"id": id}
    response.set_cookie("msg", "Juego eliminado")
    juego.deleteGame(datos)
    
    redirect("/inicio")


#ELIMINAR PRESTAMO
@route('/prestamo', method="POST")
def do_deleteLoan():
    id = request.forms.get('id')
    
    datos = {"id": id}
    response.set_cookie("msg", "Prestamo eliminado")
    prestamo.deleteGame(datos)
    
    redirect("/inicio")

#MODIFICAR JUEGO
@route('/juego', method="POST")
def do_modifyGame():
    nombre = request.forms.get('nombre')
    descripcion = request.forms.get('descripcion')
    disponible = request.forms.get('disponible')

    datos = {"nombre": nombre,
             "descripcion": descripcion,
             "disponible": disponible}
    response.set_cookie("msg", "Juego modificado")
    juego.modifyGame(datos)

    
    redirect("/inicio")
	
#MODIFICAR PRESTAMO/RENOVAR EL PRESTAMO
@route('/prestamo', method="POST")
def do_modifyLoan():
    nombre = request.forms.get('juegoPrest')
    
	persona = request.forms.get('personaPrest')
    inicio = datetime.datetime.now()
	fin = inicio + datetime.timedelta(days=7)

	
    datos = {"fecha_inicio": inicio,
			 "fecha_fin": fin,
             "juego_id": nombre,
			 "usuario_id": persona,
             "devuelto": disponible}
    response.set_cookie("msg", "Prestamo modificado")
    prestamo.modifyLoan(datos)

    
    redirect("/inicio")
	
	

@route('/inicio', method="GET")
def inicio():
    
    if not request.get_cookie("userId"):
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
    
    viewData = {'userType': 'logged'}
    viewData["logged"] = True
    return template('inicio', data=viewData)

@route('/logout', method="GET")
def logout():
    response.set_cookie('msg', 'Por favor, introduce tus datos para entrar')
    response.set_cookie("userNick", '', expires=0)
    response.set_cookie("userId", '', expires=0)
    redirect("/")

run(host='localhost', port=8080, debug=True)