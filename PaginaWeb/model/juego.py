from db import *
from makedicts import *

def addGame(datos):
#id, nombre, descripcion, disponible
    conn, cur = connectDb()

    cur.execute('INSERT INTO juego \
                    (nombre, descripcion, disponible) \
                    VALUES (?, ?, ?)',
                    (datos["nombre"], datos["descripcion"], datos["disponible"]))

    cur.close()
    conn.commit()



def modifyGame(datos):
    #update table_name SET column1=value1 WHERE ID = id
    conn, cur = connectDb()

    cur.execute('UPDATE juego \
                    SET nombre = ?, descripcion = ?, disponible = ? \
                    WHERE id = ?',
                    (datos["nombre"], datos["descripcion"], datos["disponible"], datos["id"]))

    cur.close()
    conn.commit()
    
def modifyAvailableGame(gameId, available):
    conn, cur = connectDb()

    cur.execute('UPDATE juego \
                    SET disponible = ? \
                    WHERE id = ?',
                    (available, gameId))

    cur.close()
    conn.commit()

def deleteGame(gameId):
    #DELETE FROM table_name WHERE [condition];
    conn, cur = connectDb()

    cur.execute('DELETE FROM juego \
                    WHERE id = ?',
                    (gameId, ))

    cur.close()
    conn.commit()

def getGameById(gameId = 0):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM juego WHERE id = ?', (gameId, ))

def searchAllGame():
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM juego')

def searchGame(data):
    conn, cur = connectDb()

    return makedicts(cur, "SELECT * FROM juego WHERE {f} LIKE '%{v}%'".format(f=data["field"], v=data["value"])) 