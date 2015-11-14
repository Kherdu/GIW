from db import *
from makedicts import *

def addGame(datos):
#id, nombre, descripcion, disponible
    conn, cur = connectDb()

    cur.execute('INSERT INTO juego \
                    (nombre, descripcion, disponible) \
                    VALUES (?, ?, ?)',
                    (datos[""], datos[""], datos[""]))

    cur.close()
    conn.commit()



def modifyGame(datos):
    #update table_name SET column1=value1 WHERE ID = id
    conn, cur = connectDb()

    cur.execute('UPDATE juego \
                    SET nombre = ?, descripcion = ?, disponible = ? \
                    WHERE id = ?',
                    (datos[""], datos[""], datos[""], datos[""]))

    cur.close()
    conn.commit()

def deleteGame(datos):
    #DELETE FROM table_name WHERE [condition];
    conn, cur = connectDb()

    cur.execute('DELETE FROM juego \
                    WHERE id = ?',
                    (datos[""]))

    cur.close()
    conn.commit()

def getGameById(id = 0):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT id FROM usuario WHERE id = ?', (id, ))
