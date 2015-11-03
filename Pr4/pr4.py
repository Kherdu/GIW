# -*- coding: cp1252 -*-
import sqlite3

def createDatabase():
    conn = sqlite3.connect('Universidad')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS universidades")
    cur.execute("CREATE TABLE universidades \
                (nombre_univ VARCHAR(256) PRIMARY KEY, \
                comunidad VARCHAR(256), \
                plazas INTEGER)")

    cur.execute("DROP TABLE IF EXISTS estudiantes")
    cur.execute("CREATE TABLE estudiantes \
                (id INTEGER PRIMARY KEY, \
                nombre_est VARCHAR(256), \
                nota REAL, \
                valor INTEGER)")

    cur.execute("DROP TABLE IF EXISTS solicitudes")
    cur.execute("CREATE TABLE solicitudes \
                (id INTEGER REFERENCES estudiantes, \
                nombre_univ VARCHAR(256) REFERENCES universidades, \
                carrera  VARCHAR(256), \
                decision VARCHAR(2))")

    cur.close()

    conn.commit()

def fillDatabase():
    conn = sqlite3.connect('Universidad')
    cur = conn.cursor()

    #Inser universidades
    cur.execute("INSERT INTO universidades VALUES(\
                'Universidad Complutense de Madrid', 'Madrid', '15000')")
    cur.execute("INSERT INTO universidades VALUES(\
                'Universidad de Barcelona', 'Barcelona', '36000')")
    cur.execute("INSERT INTO universidades VALUES(\
                'Universidad de Valencia', 'Valencia', '10000')")
    cur.execute("INSERT INTO universidades VALUES(\
                'UPM', 'Madrid', '21000')")

    #Insert estudiantes
    cur.execute("INSERT INTO estudiantes VALUES(\
                123, 'Antonio', 8.9, 1000)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                234, 'Juan', 8.6, 1500)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                345, 'Isabel', 8.5, 500)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                456, 'Doris', 7.9, 1000)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                543, 'Pedro', 5.4, 2000)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                567, 'Eduardo', 6.9, 2000)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                654, 'Alfonso', 7.9, 1000)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                678, 'Carmen', 5.8, 200)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                765, 'Javier', 7.9, 1500)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                789, 'Isidro', 8.4, 800)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                876, 'Irene', 6.9, 400)")
    cur.execute("INSERT INTO estudiantes VALUES(\
                987, 'Elena', 6.7, 800)")

    #Insert solicitudes
    cur.execute("INSERT INTO solicitudes VALUES(\
                123, 'Universidad Complutense de Madrid', 'Informatica', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                123, 'Universidad Complutense de Madrid', 'Economia', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                123, 'Universidad de Barcelona', 'Informatica', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                123, 'UPM', 'Economia', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                234, 'Universidad de Barcelona', 'Biologia', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                345, 'Universidad de Valencia', 'Bioingenieria', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                345, 'UPM', 'Bioingenieria', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                345, 'UPM', 'Informatica', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                345, 'UPM', 'Economia', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                678, 'Universidad Complutense de Madrid', 'Historia', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                987, 'Universidad Complutense de Madrid', 'Informatica', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                987, 'Universidad de Barcelona', 'Informatica', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                876, 'Universidad Complutense de Madrid', 'Informatica', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                876, 'Universidad de Valencia', 'Biologia', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                876, 'Universidad de Valencia', 'Biologia Marina', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                765, 'Universidad Complutense de Madrid', 'Historia', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                765, 'UPM', 'Historia', 'No')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                765, 'UPM', 'Psicologia', 'Si')")
    cur.execute("INSERT INTO solicitudes VALUES(\
                543, 'Universidad de Valencia', 'Informatica', 'No')")

    cur.close()

    conn.commit()

def consultas():
    
    from makedicts import makedicts
    from dumpdb import showformat
    from loaddb import login
    
    conn, curs = login('Universidad')

    print "\n\n1.- Obtener los nombres y notas de los estudiantes así como el resultado de su solicitud de \
manera que tengan un valor de corrección menor que 1000 y hayan solicitado la carrera de \
Informática en la Universidad Complutense de Madrid.\n"
    
    rows = makedicts(curs, "SELECT nombre_est, nota \
                            FROM estudiantes, solicitudes \
                            WHERE estudiantes.id = solicitudes.id \
                              AND estudiantes.valor < 1000 \
                              AND solicitudes.carrera = 'Informatica' \
                              AND solicitudes.nombre_univ = 'Universidad Complutense de Madrid'")
    showformat(rows)

    print "\n\nObtener  los  estudiantes  cuya  nota ponderada  cambia  en  más  de\
un  punto  respecto  a  la nota original.\n"
    
    rows = makedicts(curs, "SELECT * \
                            FROM estudiantes \
                            WHERE estudiantes.nota - (estudiantes.valor * estudiantes.nota / 1000)  > 1")
    showformat(rows)

    print '\n\nModificar la tabla solicitudes de forma que aquellos estudiantes que no solicitaron ninguna\
universidad, soliciten "Informática" en la "Universidad de Jaen".\n'

    rows = makedicts(curs, "SELECT id FROM estudiantes WHERE id NOT IN (SELECT id FROM solicitudes)")
    for row in rows:
        curs.execute('''INSERT INTO solicitudes VALUES (?, 'Universidad de Jaen', 'Informatica', 'No')''', (row["id"], ))

    rows = makedicts(curs, "SELECT * FROM solicitudes WHERE nombre_univ = 'Universidad de Jaen'")
    showformat(rows)

    print '\n\nAdmitir  en  la  "Universidad  de  Jaen"  a  todos  los  estudiantes  de  Económicas  quienes  no \
fueron admitidos en dicha carrera en otras universidades.\n'
    
    rows = makedicts(curs, "SELECT id\
                            FROM solicitudes\
                            WHERE carrera = 'Economia'\
                            AND decision = 'No'\
                            AND nombre_univ != 'Universidad de Jaen'\
                            AND id NOT IN (SELECT id\
                                           FROM solicitudes\
                                           WHERE carrera = 'Economia'\
                                           AND decision = 'Si')");
    for row in rows:
        curs.execute('''INSERT INTO solicitudes VALUES (?, 'Universidad de Jaen', 'Economia', 'Si')''', (row["id"], ))
        
    rows = makedicts(curs, "SELECT * FROM solicitudes WHERE nombre_univ = 'Universidad de Jaen' AND carrera = 'Economia'")
    showformat(rows)
    
    print "\n\nBorrar a todos los estudiantes que solicitaron más de 2 carreras diferentes.\n"
    
 
    rows = makedicts (curs, 'SELECT id,count(DISTINCT carrera) AS c FROM solicitudes GROUP BY id HAVING c>2')
    for r in rows:
        curs.execute('DELETE FROM estudiantes WHERE id = ?',(r['id'], ))

    rows = makedicts(curs, 'SELECT * FROM estudiantes')
    showformat(rows)

if __name__ == '__main__':
    
    createDatabase()
    fillDatabase()
    consultas()
