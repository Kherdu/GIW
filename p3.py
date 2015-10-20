import urllib
import json
from xml.dom.minidom import parse
import xml.dom.minidom

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Entrar ciudad: ')
    if len(address) < 1 or address == 'stop' : break
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Recuperando', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Recuperados',len(data),'characters'

    doc= open ('datos.xml','w')
    doc.write(data)
    doc.close()

    ArbolDOM=xml.dom.minidom.parse('datos.xml')
    datos=ArbolDOM.documentElement
    info=datos.getElementsByTagName('status')[0]
    print info.childNodes[0].data
   
    for d in info:
        if d.hasAttribute('formatted_address'):
            direccion=d.getAttribute('formatted_address')
        if d.hasAttribute('location'):
            latitud=d.getAttribute('lat')
            longitud=d.getAttribute('lng')
##        if d.hasAttribute('address_component'):
##            if d.hasAttribute('type') and d.getAttribute('type')== 'locality':
##                nombre=d.
    #address_component/ extraer nombre (short_name)
    #                   pais () type country-> long_name
    #                   pais, short name
    #                   administrative area lelvel 1 long name
    #formatted adress
    #geometry/location
    
