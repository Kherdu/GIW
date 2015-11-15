from db import *
from makedicts import *

def addLoan(datos):
    #id, fecha_inicio, fecha_fin, juego_id, usuario_id, devuelto
    conn, cur = connectDb()

    cur.execute('INSERT INTO prestamo \
                    (fecha_inicio, fecha_fin, juego_id, usuario_prestado, dni_prestado, devuelto) \
                    VALUES (?, ?, ?, ?, ?, ?)',
                    (datos[""], datos[""], datos[""], datos[""], datos[""], datos[""]))

    cur.close()
    conn.commit()
    
    
def modifyLoan(datos):
    conn, cur = connectDb()

    cur.execute('UPDATE prestamo \
                    SET fecha_inicio = ?, fecha_fin = ?, juego_id =?, usuario_prestado=?, dni_prestado=?, devuelto=? \
                    WHERE id = ?',
                    (datos[""], datos[""], datos[""], datos[""], datos[""], datos [""], datos[""]))

    cur.close()
    conn.commit()

def deleteLoan(datos):
    #DELETE FROM table_name WHERE [condition];
    conn, cur = connectDb()

    cur.execute('DELETE FROM prestamo \
                    WHERE id = ?',
                    (datos[""]))

    cur.close()
    conn.commit()

def searchAllLoan():
    conn, cur = connectDb()

    cur.execute('SELECT * FROM prestamo' )

    cur.close()
    conn.commit()
    
def searchLoan(data):
    conn, cur = connectDb()

    cur.execute('SELECT * FROM prestamo WHERE ? = ?', (datos["campo"],datos["busqueda"]) )

    cur.close()
    conn.commit()