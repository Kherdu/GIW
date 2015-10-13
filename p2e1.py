import csv

def acumanyos():
    
    archivo= open("PitchingPost.csv")
    lector= csv.reader(archivo)
    datos=list(lector)
    dicc= dict()

    datos.pop(0)
    for dato in datos:
        fecha=dato[1]
        if(fecha in dicc):
            dicc[fecha] = 1 + dicc[fecha]
        else:
            dicc[fecha] = 1
            
    archivo.close()
    new = open("AcumAnnos.csv", "w")
    newWriter = csv.writer(new)
    
    for clave in dicc:
        newWriter.writerow([clave, dicc[clave]])
    new.close()

def acumjug():
    archivo= open("PitchingPost.csv")
    lector= csv.reader(archivo)
    datos=list(lector)
    dicc= dict()

    datos.pop(0)
    for dato in datos:
        nombre=dato[0]
        if(nombre in dicc):
            dicc[nombre] = 1 + dicc[nombre]
        else:
            dicc[nombre] = 1
            
    archivo.close()
    new = open("AcumJugadores.csv", "w")
    newWriter = csv.writer(new)
    
    for clave in dicc:
        newWriter.writerow([clave, dicc[clave]])
    new.close()

def ordenado():
    archivo= open("PitchingPost.csv")
    lector= csv.reader(archivo)
    datos=list(lector)
    datos.pop(0)
    ordenado = sorted(datos, key=lambda tup: tup[0])
    archivo.close()
    
    new = open("Ordenado.csv", "w")
    newWriter = csv.writer(new)
    for dato in ordenado:
        newWriter.writerow(dato)
    new.close()

ordenado()
acumjug()
acumanyos()
