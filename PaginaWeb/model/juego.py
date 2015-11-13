from db import *
from makedicts import *

def addGame(datos):
#id, nombre, descripcion, disponible
    conn, cur = connectDb()

    cur.execute('INSERT INTO juego \
                    (nombre, descripcion, disponible) \
                    VALUES (?, ?, ?)'),
                    (datos[""], datos[""], datos[""]))

    cur.close()
    con.commit()

def addLoan(datos):
    #id, fecha_inicio, fecha_fin, juego_id, usuario_id, devuelto
    conn, cur = connectDb()

    cur.execute('INSERT INTO prestamo \
                    (fecha_inicio, fecha_fin, juego_id, usuario_id, devuelto) \
                    VALUES (?, ?, ?, ?, ?)'),
                    (datos[""], datos[""], datos[""], datos[""], datos[""]))

    cur.close()
    con.commit()

def modifyGame(datos):
    #update table_name SET column1=value1 WHERE ID = id
    conn, cur = connectDb()

    cur.execute('UPDATE juego \
                    SET nombre = ?, descripcion = ?, disponible = ? \
                    WHERE id = ?'),
                    (datos[""], datos[""], datos[""], datos[""]))

    cur.close()
    con.commit()


def modifyLoan(datos):
    conn, cur = connectDb()

    cur.execute('UPDATE prestamo \
                    SET fecha_inicio = ?, fecha_fin = ?, juego_id =?, usuario_id=?, devuelto=? \
                    WHERE id = ?'),
                    (datos[""], datos[""], datos[""], datos[""], datos[""]))

    cur.close()
    con.commit()


def getGameById(id = 0):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT id FROM usuario WHERE nick = ?', (nick, ))
