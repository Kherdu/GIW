# -*- coding: cp1252 -*-
import urllib
import re
import os
import collections
from BeautifulSoup import*

def auxiliar(url, l):
    
    pagina = urllib.urlopen(url)
    sopa = BeautifulSoup(pagina)
    
    for it in l:
       enc = sopa.find(text=re.compile(it))
      
       if enc:
           print url
            

def ej2():

    lst = raw_input('Introduce la lista de palabras: ')
    l=[]
    if not isinstance(l,list):
        print pene
        l.append(lst)
    else:
        l = map(str, lst.split())
    
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
                auxiliar(url, l)

ej2()
        
        
            
