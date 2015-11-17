from db import *
from makedicts import *

def getUserByNick(nick):
    conn, cur = connectDb()

    return makedicts(cur,'SELECT * FROM usuario WHERE nick = ?', (nick, ))

def searchAllUser():
    conn, cur = connectDb()

    return makedicts(cur,'SELECT * FROM usuario WHERE ? = ?')

def insertUsuario(datos):
    conn, cur = connectDb()
    
    cur.execute('INSERT INTO usuario \
                 (nick, password, nombre, dni) \
                 VALUES (?, ?, ?, ?)',
                (datos["nick"], datos["password"], datos["nombre"], datos["dni"]))
    
    cur.close()
    conn.commit();
    
def searchUser(data):
    conn, cur = connectDb()

    return makedicts(cur, "SELECT * FROM usuario WHERE {f} LIKE '%{v}%'".format(f=data["field"], v=data["value"]))  
