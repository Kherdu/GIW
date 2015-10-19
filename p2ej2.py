import urllib
import json

#termino va a ser lo que introducimos nosotros para la busqueda

def tweets():    
    manf = open('tweets.txt')
    dic = dict()
    for linea in manf:
        data = linea
        js = json.loads(data)
        if 'text' in js:
            js['text']
            terminos = js['text'].split()
            for term in terminos:
                if term in dic:
                    dic[term] = dic[term] + 1
                else:
                    dic[term] = 1
        archivo = open("frecuenciaTweets.txt", 'w')
        for clave in dic:
            archivo.write(clave.encode('utf-8')+' - ' + str(dic[clave]) + '\n')
       


def hashtag():
    manf = open('tweets.txt')
    dic = dict()
    for linea in manf:    
        data = linea
        js = json.loads(data)
        if 'entities' in js:
            ent=js['entities']
            if ent and 'hashtags' in ent:
                hasht=ent['hashtags'] #aqui nos metemos en la lista de hashtag de entities
                for h in hasht:
                    twt=h['text'] #aqui cogemos el texto del hashtag
                    if twt in dic:
                        dic[twt] = dic[twt] + 1
                    else:
                        dic[twt] = 1
                        
                   
        archivo = open("frecuenciahashtags.txt", 'w')
        for clave in dic:
            archivo.write(clave.encode('utf-8')+' - ' + str(dic[clave]) + '\n')
