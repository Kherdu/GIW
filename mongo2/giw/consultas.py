# -*- coding: utf-8 -*-
"""
Autores: Jorge Alonso Fernández, Pablo Aragón Moreno, Rafael Caturla Torrecilla
Grupo 6

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

#2,3,4,5, y 7 usan la misma plantilla
from bottle import get, run, template, route, static_file, request
from pymongo import MongoClient, cursor
import pymongo
# Resto de importaciones


@get('/find_user_id') #ok
def find_user_id():
    client= MongoClient()
    db = client['giw']
    _id= request.query['_id']
    print _id
    cursor= db.users.find({"_id": _id})
    x=[]
    for c in cursor:
        x.append(c)
    viewData= {
        'title' : 'find user id',
        'err' : 'asd',
        'users' : x
    }
	 
    # http://localhost:8080/find_user_id?_id=user_1
    return template('find_user_id', data=viewData)


@get('/find_users') #ok 
def find_users():
   # _id, email, gender y year
    # http://localhost:8080/find_users?gender=Male
    # http://localhost:8080/find_users?gender=Male&year=2009
    client = MongoClient()
    db = client["giw"]
    x=[]
    cont_errores=0
    _id=""
    email=""
    gender=""
    year=""
    my_dict = request.query.decode()
    
    errores=""
    for i in my_dict.keys():
        if i== "_id":
            _id=my_dict['_id']
        elif i== "email":
            email=my_dict['email']
        elif i== "gender":
            gender=my_dict['gender']
        elif i== "year":
            year=my_dict['year']
        else:
            errores = errores + " "+  i
            cont_errores+=1
            #print "fallo"
            del my_dict[i]
    
    if cont_errores == 0:
        query={}
        if _id:
            query["_id"]=_id 
        if email:
            query["email"]=email 
        if gender:
            query["gender"]=gender 
        if year:
            query["year"]=int(year) 
        
        cursor = db.users.find(dict(query))
        for i in cursor:
            x.append(i)    
        
        viewData={
            'title': 'find users',
            'users': x,
            'err': errores
        }   
    
        return template('find_users', data = viewData)
    else:
        viewData={
            'title': 'find users',
            'users': x,
            'err': errores
        }   
    
        return template('find_users', data = viewData)


@get('/find_users_or')
def find_users_or():
  # http://localhost:8080/find_users_or?gender=Male&year=2000

    client = MongoClient()
    db = client["giw"]
    x=[]
    cont_errores=0
    _id=""
    email=""
    gender=""
    year=""
    my_dict = request.query.decode()
    errores=""
    for i in my_dict.keys():
        if i== "_id":
            _id=my_dict['_id']
        elif i== "email":
            email=my_dict['email']
        elif i== "gender":
            gender=my_dict['gender']
        elif i== "year":
            year=my_dict['year']
        else:
            errores = errores + " "+  i
            cont_errores+=1
            #print "fallo"
            del my_dict[i]
     
    if cont_errores == 0:
        if _id:
            cursor=db.users.find({"_id":_id})
            for i in cursor:
                x.append(i)
        if email:
            cursor=db.users.find({"email":email})
            for i in cursor:
                x.append(i)  
        if gender:
            cursor=db.users.find({"gender":gender})
            for i in cursor:
                x.append(i)  
        if year:
            year=int(year)
            cursor=db.users.find({"year":year})
            for i in cursor:
                x.append(i)  
        viewData={
            'title': 'find users',
            'users': x,
            'err': errores
        }   
    
        return template('find_users', data = viewData)
    else:
        viewData={
            'title': 'find users or',
            'users': x,
            'err': errores
        }   
    
        return template('find_users', data = viewData)

       
@get('/find_like') # ok
def find_like():
    client= MongoClient()
    db = client['giw']
	
    like= request.query['like']
    cursor= db.users.find({"likes": like})
    x=[]
    for c in cursor:
        x.append(c)

    viewData= {
	'title' : 'find like',
    	'users' : x,
        'err': ""
    }
    # http://localhost:8080/find_like?like=football
    return template('find_users', data=viewData)



@get('/find_country') #ok
def find_country():
    client= MongoClient()
    db = client['giw']
	
    country= request.query['country']
    cursor= db.users.find({"address.country": country})
    x=[]
    for c in cursor:
    	x.append(c)
		
    viewData= {
	'title' : 'find like',
	'users' : x,
        'err': ""
    }
    # http://localhost:8080/find_like?like=football
    return template('find_users', data=viewData)


@get('/find_email_year')
def email_year():
    client= MongoClient()
    db = client['giw']
	
    year= request.query['year']
    year= int(year)
    cursor= db.users.find({"year": year}, {"email":1})
    x=[]
    for c in cursor:
        print c
        x.append(c)
        
    viewData= {
	'title' : 'find like',
	'users' : x,
        'err': ""
    }
    return template('find_email_year', data=viewData)
    # http://localhost:8080/find_email_year?year=1992


@get('/find_country_limit_sorted')
def find_country_limit_sorted():

    client= MongoClient()
    db = client['giw']
	
    country = request.query['country']
    maxnum = request.query['limit']
    maxnum= int(maxnum)
    order = request.query['ord']
    if order == 'asc':
        nord=pymongo.ASCENDING
    elif order == 'desc':
        nord=pymongo.DESCENDING
    cursor= db.users.find({"address.country": country }).sort("year",nord).limit(maxnum)
    x=[]
    for c in cursor:
    	x.append(c)
		
    viewData= {
	'title' : 'find like',
	'users' : x,
        'err' : ""
    }
    return template('find_users', data=viewData)
    # http://localhost:8080/find_country_limit_sorted?country=Spain&limit=20&ord=asc
    


###############################################################################
################# Funciones auxiliares a partir de este punto #################
###############################################################################
@route('<path:path>')
def server_static(path):
    return static_file(path, root='static')


###############################################################################
###############################################################################

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)
