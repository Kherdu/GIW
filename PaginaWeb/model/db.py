# -*- coding: cp1252 -*-
import sqlite3

def createDatabase():
    conn = sqlite3.connect('juegos.sqlite3')
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS usuario")
    cur.execute("CREATE TABLE usuario \
                (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                nick VARCHAR(256), \
                password VARCHAR(256), \
                nombre VARCHAR(256), \
                dni VARCHAR(10))")
    print "Tabla usuario creada"
    
    cur.execute("DROP TABLE IF EXISTS juego")
    cur.execute("CREATE TABLE juego \
                (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                nombre VARCHAR(256), \
                descripcion  VARCHAR(256), \
                disponible INTEGER)")
    print "Tabla jueg creada"
    
    cur.execute("DROP TABLE IF EXISTS prestamo")
    cur.execute("CREATE TABLE prestamo \
                (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                fecha_inicio TIMESTAMP, \
                fecha_fin  TIMESTAMP, \
                juego_id INTEGER REFERENCES juego, \
                usuario_id INTEGER REFERENCES usuario, \
                devuelto INTEGER)")
    print "Tabla prestamo creada"

    cur.close()

    conn.commit()
