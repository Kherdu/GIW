# -*- coding: utf-8 -*-
"""
Autores: Rafael Caturla Torrecilla, Pablo Aragón Moreno , Jorge Alonso Fernández
Grupo 6

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

from bottle import post, request, run
from pymongo import MongoClient, cursor


# ¡MUY IMPORTANTE!
# Todas las inserciones se deben realizar en la colección 'users' dentro de la
# base de datos 'giw'.


@post('/add_user')
def add_user_post():
    client = MongoClient()
    db = client['giw']    
    
    _id=request.forms.get('id')
    country=request.forms.get('country')
    zip=request.forms.get('zip')
    email=request.forms.get('email')
    gender=request.forms.get('gender')
    likes=request.forms.get('likes').split(',')
    password=request.forms.get('password')
    year=request.forms.get('year')
    
    result=db.users.insert_one( { "_id": _id ,
                            "address": {
                                "country": country,
                                "zip": zip
                            },
                            "email": email,
                            "gender": gender,
                            "likes":likes,
                            "password":password,
                            "year":year})
    result.inserted_id
	
@post('/change_email')
def change_email(cosa1, cosa2):
    client = MongoClient()
    db = client['giw']

    #id1 = request.forms.get('id')
    #email = request.forms.get('email') 
    id1 = cosa1
    email = cosa2

    result = db.users.update_one({'_id': id1}, {'$set': {'email': email}})
    
    print result    
    print  result.matched_count  
    pass
    client.close()
    return result.matched_count  

@post('/insert_or_update')
def insert_or_update():
    
    c = MongoClient()
    
    db = c['giw']
    
    # Getting post variables
    _id = request.forms.get('_id')
    country = request.forms.get('country')
    zipValue = request.forms.get('zip')
    email = request.forms.get('email')
    gender = request.forms.get('gender')
    likes = request.forms.get('likes').split(',')
    password = request.forms.get('password')
    year = request.forms.get('year')
    
    cursor = db.users.find({"_id": _id})
    
    if cursor.count() > 0:
        ret = "Usuario encontrado. Actualizando usuario"
        db.users.update_one({'_id': _id}, { "$set": 
                            {"_id": _id, 
                             "address": {"country": country,
                                      "zip": zipValue, 
                                      },
                             "email": email,
                             "gender": gender,
                             "likes":likes,
                             "password":password,
                             "year": year} })
                                     
    else:
        ret = "Usuario no encontrado. Insertando usuario"
        db.users.insert_one({ "_id": _id, 
                           "address": {"country": country,
                                      "zip": zipValue, 
                                      },
                           "email": email,
                           "gender": gender,
                           "likes":likes,
                           "password":password,
                           "year": year} )
    
    c.close()
    
    return ret


@post('/delete')
def delete_id(cosa1):
    client = MongoClient()
    db = client['giw']

    #id1 = request.forms.get('id')  
    id1 = cosa1
    result = db.users.delete_one({'_id': id1})   
    
    pass
    client.close()
    print  result.deleted_count  
    return result.deleted_count  
    
    
@post('/delete_year')
def delete_year(cosa1):
    client = MongoClient()
    db = client['giw']

    #anio = request.forms.get('year')   
    anio = cosa1
    cursor = db.users.find({"year": anio})
    contador = 0
    for doc in cursor:        
        result = db.users.delete_one({'_id': doc['_id']})   
        contador = result.deleted_count  + contador
    pass
    print contador
    client.close()
    return contador
    
run(host='localhost', port=8080, debug=True)