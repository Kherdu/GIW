# -*- coding: utf8 -*-
#Crear un programa que simule una agenda personal que almacena de cada contacto el nombre,
#apellidos y teléfono. La agenda se almacena en un fichero de texto agenda.txt. Cada contacto
#ocupará 4 líneas del fichero. La agenda tendrá las siguientes funciones:
#Crear entrada.
#Borrar entrada.
#Buscar entrada por nombre, apellido o teléfono.
#Cargar entrada.

def crearEntrada():
    
    name= raw_input('Introduzca nombre: ')
    apellido1= raw_input('Introduzca primer apellido: ')
    apellido2= raw_input('Introduzca segundo apellido: ')
    telefono= raw_input('Introduzca telefono: ')
    old=''
    try:
        fichero=open('agenda.txt')
        old=fichero.read()
        fichero.close()
    except:
        print('Fichero agenda.txt no encontrado')
        
    fichero=open('agenda.txt', 'w')
    new=old+telefono+'\n'+name+'\n'+apellido1+'\n'+apellido2+'\n'
    fichero.write(new)
    fichero.close()

    print('\nContacto añadido:\n\tNombre: '+name+'\n\tApellido1: '+apellido1+
          '\n\tApellido2: '+apellido2+'\n\tTelefono: '+telefono)
    
    

def borrarEntrada():
    
    
    tel= raw_input('Introduzca el telefono del contacto a borrar: ')
   
    try:
        fichero=open('agenda.txt')
        cont = 0
        new = ''
        find = False
        for linea in fichero:
            if linea.find(tel)!= -1 or cont > 0 and cont < 4:
                cont+=1
                find = True
            else:
                cont = 0
                new += linea
        fichero.close()
    except:
        print('Fichero agenda.txt no encontrado')

    if find:
        fichero=open('agenda.txt','w')
        fichero.write(new)
        fichero.close()
        print('\n\tSe ha eliminado el contacto con numero: '+tel)
    else:
        print('\n\tContacto no encontrado')
        
    
def buscar():
    dato= raw_input('Introduzca un dato del contacto: ')
    find=False
    nombre=''
    apellido1=''
    apellido2=''
    telefono=''
    try:
        fichero=open('agenda.txt')
        for linea in fichero:
            telefono=next(fichero)
            nombre=next(fichero)
            apellido1=next(fichero)
            apellido2=next(fichero)
            if telefono==dato or apellido1==dato or nombre==dato:
                find=True
                break
        if find:
            print('Contacto encontrado: \n\tNombre: '+nombre+'\n\tApellido1: '+apellido1+
          '\n\tApellido2: '+apellido2+'\n\tTelefono: '+telefono)              
        else:
            print('Contacto no encontrado')
        fichero.close()
    except:
        print('Agenda no encontrada')

def cargar():
    return 0

def agenda():
    
    options = {
        '1': crearEntrada,
        '2': borrarEntrada,
        '3': buscar,
        '4': cargar
        }

    print 'bienvenido a la agenda'
    entrada = 0
    while entrada != '5':
        
        print '\n1.-Añadir entrada'
        print '2.-Borrar entrada'
        print '3.-Buscar entrada'
        print '4.-Cargar entrada'
        print '5.-Salir'
        
        entrada= raw_input('Elija una opción: ')
        
        while entrada < '1' or entrada > '5':
            entrada=raw_input('introduce otra vez\n')
        if entrada == '5':
            exit()
        else: options[entrada]()
