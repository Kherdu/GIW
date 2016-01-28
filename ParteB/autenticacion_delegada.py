# -*- coding: cp1252 -*-
from bottle import run, get, static_file, route, template, request, app
import bottle
import requests
from beaker.middleware import SessionMiddleware
import hashlib
import os

# Credenciales. 
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
# Copiar los valores adecuados.
CLIENT_ID     = "1057639190052-qn8e4v6vmuq9bebh3p1imeln5dfnlam1.apps.googleusercontent.com"
CLIENT_SECRET = "T3JVvOwCIuTeQCk9MQn3soE9"
REDIRECT_URI  = "http://localhost:8080/token"

# Fichero de descubrimiento para obtener el 'authorization endpoint' y el 
# 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"


# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKEN_VALIDATION_ENDPOINT = "https://www.googleapis.com/oauth2/v4/token"
AUTHORIZATION_ENDPOINT = "https://accounts.google.com/o/oauth2/v2/auth"

@get('/login_google')
def login_google():
    
    client_id = "?client_id="+CLIENT_ID
    response_type = "&response_type=code"
    scope = "&scope=openid%20email"
    redirect_uri = "&redirect_uri="+REDIRECT_URI
    
    uri = AUTHORIZATION_ENDPOINT + client_id + response_type + scope + redirect_uri

    s = request.environ.get('beaker.session')
    s.invalidate() # Regenera la sesión para evitar posible session fixation
    s['token'] = hashlib.sha256(os.urandom(1024)).hexdigest()
    s.save()

    return template("index", btn_uri = uri)


@get('/token')
def token():
    
    session = request.environ.get('beaker.session')
    if 'state' in session:
        return template("error", error = "Error")
    
    code = request.query['code']
    
    r = requests.post(TOKEN_VALIDATION_ENDPOINT,
                      data={'code': code,
                            'client_id': CLIENT_ID,
                            'client_secret': CLIENT_SECRET,
                            'redirect_uri':REDIRECT_URI,
                            'grant_type': 'authorization_code'})
    
    try:
        id_token = r.json()['id_token']
        
    except:
        return template("error", error = "No se ha encotrado el id_token")

    user_data = requests.get("https://www.googleapis.com/oauth2/v3/tokeninfo?id_token="+id_token)
    email = user_data.json()
    
    return template("welcome", email)

@route('<path:path>')
def server_static(path):
    return static_file(path, root='static')


if __name__ == "__main__":
    session_opts = {
        'session.type' : 'file',
        'session.cookie_expires': 300,
        'session.data_dir': './data',
        'session.auto': True, # se salva automaticamente sin llamar a save()
        'session.httponly': True,
    }
    app = SessionMiddleware(app(), session_opts)
    run(host='localhost',port=8080,debug=True,app=app)
