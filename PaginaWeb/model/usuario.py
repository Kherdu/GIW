from db import *
from makedicts import *

def getUsuarioById(usuarioId = 0):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM usuario WHERE id = ?', (usuarioId, ))

def getUsuarioByNick(nick = ''):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM usuario WHERE nick = ?', (nick, ))


def insertUsuario(datos):
    conn, cur = connectDb()
    
    cur.execute('INSERT INTO usuario \
                 (nick, password, nombre, dni) \
                 VALUES (?, ?, ?, ?)',
                (datos["nick"], datos["password"], datos["nombre"], datos["dni"]))

    cur.close()
    conn.commit()
	

