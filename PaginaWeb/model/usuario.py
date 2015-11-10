import sqlite3
from makedicts import *

def getUsuarioById(usuarioId = 0):
    conn = sqlite3.connect('juegos.sqlite3')
    cur = conn.cursor()

    return makedicts(cur, 'SELECT * FROM usuario WHERE id = ?', (usuarioId, ))

def insertUsuario(datos):
    print "insertanto usuario"
    conn = sqlite3.connect('juegos.sqlite3')
    cur = conn.cursor()

    cur.execute('INSERT INTO usuario \
                 (nick, password, nombre, dni) \
                 VALUES ("?", "?", "?", "?")',
                (datos["nick"], datos["password"], datos["nombre"], datos["dni"] ))

    cur.close()
    conn.commit()
