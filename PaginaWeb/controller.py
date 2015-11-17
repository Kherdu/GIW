# -*- coding: cp1252 -*-
import datetime
from model import usuario, prestamo, juego
from bottle import route, run, request, response, template, redirect, static_file

@route('/')
@route('/login')
def login():
    
    viewData = {'userType': 'guest',
                'title': 'Login',
                'err': '',
                'succ': ''}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
        
    return template('index', data=viewData)

@route('/registro', method='GET')
def registro(msg=''):
    
    viewData = {'userType': 'guest',
                'title': 'Registro',
                'err': '',
                'succ': ''}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
        
    return template('registro', data=viewData)

@route('/registro', method='POST')
def do_registro():
    
    username = request.forms.get('user')
    password = request.forms.get('password')
    password2 = request.forms.get('password2')
    name = request.forms.get('name')
    dni = request.forms.get('dni')

    if password != password2:
        response.set_cookie("err", "Las contrasenas no coinciden")
        redirect("/registro")
        return 0
        
    users = usuario.getUserByNick(username)
    
    if len(users) > 0:
        response.set_cookie("err", "Nick en uso")
        redirect("/registro") 

    datos = {"nick": username,
             "password": password,
             "nombre": name,
             "dni": dni}
    response.set_cookie("succ", "Usuario registrado")
    usuario.insertUsuario(datos)
    
    redirect("/")
    return 0

@route('/login', method="POST")
def do_login():
    
    username = request.forms.get('user')
    password = request.forms.get('password')

    users = usuario.getUserByNick(username)
    if len(users) == 0 or users[0]["password"] != password:
        response.set_cookie("err", "Contrasena incorrecta")
        redirect("/")
        return 0

    user = users[0]

    response.set_cookie("userNick", user["nick"], secret="asdf")
    response.set_cookie("userId", user["id"], secret="asdf")
    
    redirect("/inicio")
    return 0

@route('/inicio', method="GET")
def inicio():
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0
    
    viewData = {'userType': 'logged',
                'title': 'Inicio',
                'err': '',
                'succ': ''}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
    
    return template('inicio', data=viewData)

@route('/logout', method="GET")
def logout():
    
    response.set_cookie("userNick", '', expires=0)
    response.set_cookie("userId", '', expires=0)
    
    redirect("/")
    return 0
    
@route('/juegos', method="GET")
def juegos():
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        
    games = juego.searchAllGame()
    viewData = {'userType': 'logged',
                'title': 'Juegos',
                'err': '',
                'succ': '',
                'juegos': games}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
    
    return template('juegos', data=viewData)

@route('/juego/<gameId:int>', method="GET")
def viewGame(gameId=1):
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0

    game = juego.getGameById(gameId)
    
    if len(game) == 0:
        response.set_cookie('err', 'Juego no encontrado')
        redirect('/juegos')
        return 0
    
    loans= prestamo.getLoansByGameId(gameId)
        
    viewData = {'userType': 'logged',
                'title': game[0]["nombre"],
                'err': '',
                'succ': '',
                'juego': game,
                'prestamos': loans}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')

    return template("juego", data=viewData)
    
@route('/juego', method="POST")
def do_addGame():
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0
    
    nombre = request.forms.get('nombre')
    descripcion = request.forms.get('descripcion')
    disponible = request.forms.get('disponible')

    datos = {"nombre": nombre,
             "descripcion": descripcion,
             "disponible": disponible}
    
    juego.addGame(datos)
    response.set_cookie("succ", "Juego anadido")
    
    redirect("/juegos")
    return 0
    
@route('/juego/<gameId>/editar', method="POST")
def do_modifyGame(gameId=0):
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0
    
    nombre = request.forms.get('nombre')
    descripcion = request.forms.get('descripcion')
    disponible = request.forms.get('disponible')

    datos = {"nombre": nombre,
             "descripcion": descripcion,
             "disponible": disponible,
             "id": gameId}
    
    juego.modifyGame(datos)
    
    response.set_cookie("succ", "Juego modificado")
    redirect("/juego/"+gameId)
    return 0

@route('/juego/<gameId>/eliminar', method="GET")
def do_deleteGame(gameId=0):
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0
    
    juego.deleteGame(gameId) 
    response.set_cookie("succ", "Juego eliminado")
   
    redirect("/juego/"+gameId)
    return 0

@route('/prestamos', method="GET")
def prestamos():
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        
    loans = prestamo.searchAllLoan()
    games = juego.searchAllGame()
    viewData = {'userType': 'logged',
                'title': 'Prestamos',
                'err': '',
                'succ': '',
                'prestamos': loans,
                'juegos': games}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
    
    return template('prestamos', data=viewData)
    
@route('/prestamo/<prestamoId>', method="GET")
def viewPrestamo(prestamoId=0):
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        
    loans = prestamo.getLoanById(prestamoId)
    
    if len(loans) == 0:
        response.set_cookie('err', 'Prestamo no encontrado')
        redirect('/prestamos')
        return 0
    
    loan = loans[0]
    viewData = {'userType': 'logged',
                'title': 'Prestamo',
                'err': '',
                'succ': '',
                'prestamo': loan}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
    
    return template('prestamo', data=viewData)

@route('/prestamo', method="POST")
def do_addLoan():
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0
    
    juego_id = request.forms.get('juegoPrest')
    user = request.forms.get('personaPrest')
    dni = request.forms.get('dniPrest')
    inicio = datetime.datetime.now()
    fin = inicio + datetime.timedelta(days=7)
    
    datos = {"fecha_inicio": inicio,
             "fecha_fin": fin,
             "juego_id": juego_id,
             "usuario_prestado": user,
             "dni_prestado": dni,
             "devuelto": 0}
    
    prestamo.addLoan(datos)

    juego.modifyAvailableGame(juego_id, 0)
    response.set_cookie("succ", "Prestamo anadido")
    
    response.set_cookie('succ', 'Prestamo anadido')
    redirect("/prestamos")
    return 0
    
@route('/prestamo/<loanId>/editar', method="POST")
def do_modifyLoan(loanId=0):
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0
    
    juego_id = request.forms.get('juegoPrest')
    persona = request.forms.get('personaPrest')
    dni = request.forms.get('dniPrest')
    devuelto = request.forms.get('devuelto')
    inicio = datetime.datetime.now()
    fin = inicio + datetime.timedelta(days=7)

    
    datos = {"id": loanId,
             "fecha_inicio": inicio,
             "fecha_fin": fin,
             "juego_id": juego_id,
             "usuario_prestado": persona,
             "dni_prestado": dni,
             "devuelto": devuelto}
    response.set_cookie("succ", "Prestamo modificado")
    prestamo.modifyLoan(datos)
    juego.modifyAvailableGame(juego_id, devuelto)

    response.set_cookie('succ', 'Prestamo modificado')
    redirect("/prestamo/"+loanId)
    return 0

@route('/prestamo/<loanId>/eliminar', method="GET")
def do_deleteLoan(loanId=0):
    
    if not request.get_cookie("userId"):
        response.set_cookie('err', 'Por favor, introduce tus datos para entrar')
        response.set_cookie('userId', '', expires=0)
        redirect("/logout")
        return 0

    
    prestamo.deleteLoan(loanId)

    response.set_cookie('succ', 'Prestamo eliminado')
    redirect("/prestamos")
    return 0

@route('/buscar', method="GET")
def buscar():
    
    viewData = {'userType': 'logged',
                'title': 'Buscar',
                'err': '',
                'succ': ''}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
        
    return template('busqueda', data=viewData)

@route('/browseByField', method="POST")
def do_browseElementByField():
    
    table = request.forms.get('tabla')
    
    what = request.forms.get('busqueda')
    
    if table=='prestamo':
        field = request.forms.get('campoPrestamo')
        datos={"field": field,
           "value": what
           }
        reqData=prestamo.searchLoan(datos)
    elif table=='usuario':
        field = request.forms.get('campoUsuario')
        datos={"field": field,
           "value": what
           }
        reqData=usuario.searchUser(datos)
    elif table=='juego':
        field = request.forms.get('campoJuego')
        datos={"field": field,
           "value": what
           }
        reqData=juego.searchGame(datos)
        
    viewData = {'userType': 'logged',
                'title': 'Buscar',
                'err': '',
                'succ': '',
                'reqData': reqData}
    
    if request.get_cookie("err"):
        viewData["err"] = request.get_cookie("err")
        response.set_cookie('err', '')
    
    if request.get_cookie("succ"):
        viewData["succ"] = request.get_cookie("succ")
        response.set_cookie('succ', '')
        
    return template('resultado-busqueda', data=viewData)

@route('<path:path>')
def server_static(path):
    return static_file(path, root='static')

run(host='localhost', port=8080, debug=True)
