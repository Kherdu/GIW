from db import connectDb
from makedicts import makedicts

def addLoan(datos):
    #id, fecha_inicio, fecha_fin, juego_id, usuario_id, devuelto
    conn, cur = connectDb()

    cur.execute('INSERT INTO prestamo \
                    (fecha_inicio, fecha_fin, juego_id, usuario_prestado, dni_prestado, devuelto) \
                    VALUES (?, ?, ?, ?, ?, ?)',
                    (datos["fecha_inicio"], datos["fecha_fin"], datos["juego_id"], datos["usuario_prestado"], datos["dni_prestado"], datos["devuelto"]))

    cur.close()
    conn.commit()
    
    
def modifyLoan(datos):
    conn, cur = connectDb()

    cur.execute('UPDATE prestamo \
                    SET fecha_inicio = ?, fecha_fin = ?, juego_id =?, usuario_prestado=?, dni_prestado=?, devuelto=? \
                    WHERE id = ?',
                    (datos["fecha_inicio"], datos["fecha_fin"], datos["juego_id"], datos["usuario_prestado"], datos["dni_prestado"], datos["devuelto"], datos["id"]))

    cur.close()
    conn.commit()

def deleteLoan(id):
    #DELETE FROM table_name WHERE [condition];
    conn, cur = connectDb()

    cur.execute('DELETE FROM prestamo \
                    WHERE id = ?',
                    (id, ))

    cur.close()
    conn.commit()

def getLoanById(loanId=0):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM prestamo WHERE id = ? ORDER BY fecha_inicio', (loanId, )) 
    
def getLoansByGameId(gameId=0):
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM prestamo WHERE juego_id = ? ORDER BY fecha_inicio', (gameId, ))  

def searchAllLoan():
    conn, cur = connectDb()

    return makedicts(cur, 'SELECT * FROM prestamo ORDER BY fecha_inicio')

def searchLoan(data):
    conn, cur = connectDb()

    return makedicts(cur, "SELECT * FROM prestamo WHERE {f} LIKE '%{v}%'".format(f=data["field"], v=data["value"]))  