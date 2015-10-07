# -*- coding: cp1252 -*-
#Crear un programa que simule una agenda personal que almacena de cada contacto el nombre,
#apellidos y teléfono. La agenda se almacena en un fichero de texto agenda.txt. Cada contacto
#ocupará 4 líneas del fichero. La agenda tendrá las siguientes funciones:
#Crear entrada.
#Borrar entrada.
#Buscar entrada por nombre, apellido o teléfono.
#Cargar entrada.

listado = 'agenda.txt'

def crearEntrada():
    
    name= raw_input('Introduzca nombre: ')
    apellido1= raw_input('Introduzca primer apellido: ')
    apellido2= raw_input('Introduzca segundo apellido: ')
    telefono= raw_input('Introduzca telefono: ')
    old=''
    
    try:
        fichero=open(listado)
        old=fichero.read()
        fichero.close()
    except:
        print('Fichero agenda.txt no encontrado')
        
    fichero=open(listado, 'w')
    new=old+telefono+'\n'+name+'\n'+apellido1+'\n'+apellido2+'\n'
    fichero.write(new)
    fichero.close()

    print('\nContacto añadido:\n\tNombre: '+name+'\n\tApellido1: '+apellido1+
          '\n\tApellido2: '+apellido2+'\n\tTelefono: '+telefono)
    
    

def borrarEntrada():
    
    tel= raw_input('Introduzca el telefono del contacto a borrar: ')
   
    try:
        fichero=open(listado)
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
        fichero=open(listado,'w')
        fichero.write(new)
        fichero.close()
        print('\n\tSe ha eliminado el contacto con numero: '+tel)
    else:
        print('\n\tContacto no encontrado')
        
    
def buscar():
    
    dato= raw_input('\nIntroduzca un dato del contacto: ')
    
    find=False
    nombre=''
    apellido1=''
    apellido2=''
    telefono=''
    
    try:
        
        fichero = open(listado)
        
        for linea in fichero:
            telefono=linea
            nombre=next(fichero)
            apellido1=next(fichero)
            apellido2=next(fichero)

            if telefono.find(dato) != -1 or apellido1.find(dato) != -1 or nombre.find(dato) != -1:
                find=True
                print('\nContacto encontrado: \n\tNombre: '+nombre+
                      '\tApellido1: '+apellido1+'\tApellido2: '+
                      apellido2+'\tTelefono: '+telefono) 


        if not find:
            print('\nContacto no encontrado')
            
        fichero.close()
        
    except:
        print('Agenda no encontrada o vacía')

def cargar():
    global listado
    listado = raw_input('\nIntroduzca la ruta de la agenda: ');

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
        
        print '\n1.-Añadir contacto'
        print '2.-Borrar contacto'
        print '3.-Buscar contacto'
        print '4.-Cargar agenda'
        print '5.-Salir'
        
        entrada= raw_input('Elija una opción: ')
        
        while entrada < '1' or entrada > '5':
            entrada=raw_input('introduce otra vez\n')
        if entrada == '5':
            exit()
        else: options[entrada]()
