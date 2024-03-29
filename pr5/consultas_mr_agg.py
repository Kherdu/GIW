# -*- coding: utf-8 -*-
"""
Autores: XXX
Grupo YYY

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""


# Importaciones
from bottle import get, run, template, route, static_file
from bson.code import Code
from pymongo import MongoClient


# MapReduce: usuarios en cada pais.
@get('/users_by_country_mr')
def users_by_country_mr():
    
    client = MongoClient('localhost', 27017)
    db = client.giw
    mapper = Code("function () {"
                  "   this.country.forEach(function(z) {"
                  "      emit(z, 1);"
                  "  }); "
                  "}")
    reducer = Code("""
                function (key, values) {
                  return values.length;
                }
                """)
                
    result = db.users.map_reduce(mapper, reducer, "myresults")            
    print myresults
    viewData={
            'title': 'Users by country',
            'data': result
        }   
    return template('users_by_country', data = viewData)
               


# Aggregation Pipeline: usuarios en cada pais (orden descendente por numero
# de usuarios).
@get('/users_by_country_agg')
def users_by_country_agg():
    pass
    
    
# MapReduce: gasto total en cada pais.
@get('/spending_by_country_mr')
def spending_by_country_mr():
    pass


# Aggregation Pipeline: gasto total en cada pais (orden descendente por nombre
# del pais).
@get('/spending_by_country_agg')
def spending_by_country_agg():
    pass


# MapReduce: gasto total realizado por las mujeres que han realizdo EXACTAMENTE
# 3 compras.
@get('/spending_female_3_orders_mr')
def spending_female_3_orders_mr():
    pass


# Aggregation Pipeline: gasto total realizado por las mujeres que han realizdo 
# EXACTAMENTE 3 compras.
@get('/spending_female_3_orders_agg')
def spending_female_3_orders_agg():
    pass

@route('<path:path>')
def server_static(path):
    return static_file(path, root='static')
    
    
###############################################################################
###############################################################################

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)





