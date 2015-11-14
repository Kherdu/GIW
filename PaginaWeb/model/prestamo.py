from db import *
from makedicts import *

def addLoan(datos):
    #id, fecha_inicio, fecha_fin, juego_id, usuario_id, devuelto
    conn, cur = connectDb()

    cur.execute('INSERT INTO prestamo \
                    (fecha_inicio, fecha_fin, juego_id, usuario_id, devuelto) \
                    VALUES (?, ?, ?, ?, ?)',
                    (datos[""], datos[""], datos[""], datos[""], datos[""]))

    cur.close()
    conn.commit()
    
    
def modifyLoan(datos):
    conn, cur = connectDb()

    cur.execute('UPDATE prestamo \
                    SET fecha_inicio = ?, fecha_fin = ?, juego_id =?, usuario_id=?, devuelto=? \
                    WHERE id = ?',
                    (datos[""], datos[""], datos[""], datos[""], datos[""]))

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