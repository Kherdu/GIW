import urllib
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
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
            if ent:
                for htg in ent: #aqui estamos haciendo el for de entities
                    if 'hashtags' in htg:
                        hasht=htg['hashtags'] #aqui nos metemos en la lista de hashtag de entities
                        if 'text' in hasht: 
                            twt=hasht['text'] #aqui cogemos el texto del hashtag
                            if twt in dic:
                                dic[twt] = dic[twt] + 1
                            else:
                                dic[twt] = 1
                        
                   
        archivo = open("frecuenciahashtags.txt", 'w')
        for clave in dic:
            archivo.write(clave.encode('utf-8')+' - ' + str(dic[clave]) + '\n')
       

    
