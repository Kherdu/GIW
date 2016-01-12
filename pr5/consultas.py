# -*- coding: utf-8 -*-
"""
Autores: Jorge Alonso Fernández, Rafael Caturla Torrecilla, Pablo Aragón Moreno
Grupo 6

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

#2,3,4,5, y 7 usan la misma plantilla
from bottle import get, run, template, route, static_file
from pymongo import MongoClient, cursor
# Resto de importaciones


@get('/find_user_id')
def find_user_id():
    client= MongoClient()
	db = client['giw']
	
	
	_id= request.query['_id']
	cursor= db.users.find({"_id": _id})

	for c in cursor
		x.append(i)
		
	viewData= {
		'title' : 'find user id',
		'err' : 'asd',
		'users' : x
	}
	 
    # http://localhost:8080/find_user_id?_id=user_1
    return template('find_user_id', data=viewData)


@get('/find_users')
def find_users():
   # _id, email, gender y year
    # http://localhost:8080/find_users?gender=Male
    # http://localhost:8080/find_users?gender=Male&year=2009
    client = MongoClient()
    db = client["giw"]
    x=[]
    cont_errores=0
    my_dict = request.query.decode()
    errores=""
    for i in my_dict.keys():
        if i != "_id" or i != "email" or i != "gender" or i != "year":
            errores = errores + " "+  i
            cont_errores+=1
            #print "fallo"
            del my_dict[i]
        
    
     if cont_errores = 0:  
         str1 =  ""
         cont = len(i)
         for i in my_dict:
             str1 = str1 + '"'+ key(i) + '"' + ": "+ i.value
             cont-=1
             if cont !=1:
                 str1 = str1 + ", "
                
        cursor = db.users.find({str1})
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
    my_dict = request.query.decode()
    errores=""
    for i in my_dict.keys():
        if i != "_id" or i != "email" or i != "gender" or i != "year":
            errores = errores + " "+  i
            cont_errores+=1
            #print "fallo"
            del my_dict[i]
        
     
     if cont_errores = 0:  
         if my_dict.get('_id', 0)!=0:
              cursor = db.users.find({"_id": _id})
              for i in cursor:
                  x.append(i)   
         elif my_dict.get('email', 0)!=0:
              cursor = db.users.find({"email": email})
              for i in cursor:
                  x.append(i) 
         elif my_dict.get('gender', 0) and my_dict.get('year',0) != 0:
              cursor = db.users.find({"gender": gender, "year": year})
              for i in cursor:
                  x.append(i) 
         elif my_dict.get('gender', 0)!=0:
              cursor = db.users.find({"gender": gender})
              for i in cursor:
                  x.append(i) 
         else:
              cursor = db.users.find({"year": year})
              for i in cursor:
                  x.append(i) 
              
              
          
    
         viewData={
            'title': 'find users or',
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

       
@get('/find_like')
def find_like():
   client= MongoClient()
	db = client['giw']
	
	like= request.query['like']
	cursor= db.users.find({"likes": like})

	for c in cursor
		x.append(i)
		
	viewData= {
		'title' : 'find like',
		'users' : x
	}
    # http://localhost:8080/find_like?like=football
    return template('find_users', data=viewData)



@get('/find_country')
def find_country():
    client= MongoClient()
	db = client['giw']
	
	country= request.query['country']
	cursor= db.users.find({"address.country": country})

	for c in cursor
		x.append(i)
		
	viewData= {
		'title' : 'find like',
		'users' : x
	}
    # http://localhost:8080/find_like?like=football
    return template('find_users', data=viewData)


@get('/find_email_year')
def email_year():
    client= MongoClient()
	db = client['giw']
	
	year= request.query['year']
	cursor= db.users.find({"year": year }, {email : 1})

	for c in cursor
		x.append(i)
		
	viewData= {
		'title' : 'find like',
		'users' : x
	}
    return template('find_users', data=viewData)
    # http://localhost:8080/find_email_year?year=1992


@get('/find_country_limit_sorted')
def find_country_limit_sorted():
    # http://localhost:8080/find_country_limit_sorted?country=Spain&limit=20&ord=asc
    pass


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
