# -*- coding: cp1252 -*-
import urllib
import re
import os
from BeautifulSoup import*

def saveImages(url, text, j):
    
     #Si no existe el directorio se crea
    if not os.path.exists('imagesPr4'):
        os.makedirs('imagesPr4')

    #Abrimos la pagina
    pagina = urllib.urlopen(url)
    sopa = BeautifulSoup(pagina)

    #Recogemos las imagenes
    imagenes = sopa("img")

    #Accedemos a cada imagen y las guardamos
    i = 0
    for imagen in imagenes:
        if imagen.get('width') == str(640):
            #Si no existe la subcarpeta se crea
            if not os.path.exists('imagesPr4/'+str(j)):
                os.makedirs('imagesPr4/'+str(j))
            
            #Abrimos la ruta de la imagen
            src = urllib.urlopen(imagen.get('src'))
        
            #Abrimos el archivo donde volcaremos la imagen
            archivo = open('imagesPr4/'+str(j)+'/'+str(i)+'.jpg', 'wb')

            #Escribimos la imagen
            while True:
                info = src.read(100000)
                if len(info) < 1: break
                archivo.write(info)
        
            #Cerramos el archivo
            archivo.close() 
            i+=1
        

def getImages():
    html = urllib.urlopen("http://trenesytiempos.blogspot.com.es/")
    sopa = BeautifulSoup(html)
    etiquetas = sopa("a")
    patron = re.compile('http://trenesytiempos.blogspot.com.es/2015_');
    urls = []
    j = 0
    for etiqueta in etiquetas:
        if etiqueta.get('class')  == 'post-count-link':
            url = etiqueta.get('href')
            if patron.match(url):
                saveImages(url, etiqueta.text, j)
                j+=1

if __name__ == "__main__":
    getImages()
