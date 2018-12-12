# -*- coding: utf-8 -*-

'''
Daniel Bastarrica Lacalle y Gabriel Sellés Salvà declaramos que esta solución es
fruto exclusivamente de nuestro trabajo personal. No hemos sido ayudados por ninguna
otra persona ni hemos obtenido la solución de fuentes externas, y tampoco hemos com-
partido nuestra solución con nadie. Declaramos además que no hemos realizado de manera
deshonesta ninguna otra actividad que pueda mejorar nuestros resultados ni perjudicar los
resultados de los demás.
'''

import requests
import xml.etree.ElementTree as ET


def ejercicio1():

    q = """ 
        for $x in doc("/db/sgdi/books.xml")/catalog/book
        where $x/genre = "Computer"
        return $x/title
        """
    req = {'_query': q}
    r = requests.post( 'http://localhost:8080/exist/rest/db', data = req) 
    root = ET.fromstring(r.text)
    
    resul = list()
    for e in root:
        resul.append(e.text)
    return resul

def ejercicio2():

    q = """ 
        for $x in doc("/db/sgdi/books.xml")/catalog/book
        where $x/@id = "bk105"
        return $x/title
        """
    req = {'_query': q}
    r = requests.post( 'http://localhost:8080/exist/rest/db', data = req) 
    root = ET.fromstring(r.text)
    resul = list()
    for e in root:
        resul.append(e.text)
    return resul
    

def ejercicio3():

    q = """ 
        for $x in doc("/db/sgdi/books.xml")/catalog/book
        return <book>
                {$x/title}
                {$x/price}
                </book>
        """
    req = {'_query': q}
    r = requests.post( 'http://localhost:8080/exist/rest/db', data = req) 
    root = ET.fromstring(r.text)

    resul = list()
    for e in root:
        aux = {}
        for x in e:
            aux[x.tag] = x.text
        resul.append(aux)
    return resul

def ejercicio4():

    q = """ 
        for $x in doc("/db/sgdi/books.xml")/catalog/book[price>15]
        order by $x/publish_date ascending
        return $x/title
        """
    req = {'_query': q}
    r = requests.post( 'http://localhost:8080/exist/rest/db', data = req) 
    root = ET.fromstring(r.text)

    resul = list()
    for e in root:
        resul.append(e.text)
    return resul

def ejercicio5():

    q = """ 
        for $x in doc("/db/sgdi/books.xml")/catalog/book[price>40]
        where $x/genre = "Computer"
        return <book>
                {$x/title}
                {$x/author}
                {$x/price}
                </book>
        """
    req = {'_query': q}
    r = requests.post( 'http://localhost:8080/exist/rest/db', data = req) 
    root = ET.fromstring(r.text)

    resul = list()
    for e in root:
        aux = {}
        for x in e:
            aux[x.tag] = x.text
        resul.append(aux)
    return resul

if __name__ == "__main__":
    resul = ejercicio5 () 
    print( resul )
        