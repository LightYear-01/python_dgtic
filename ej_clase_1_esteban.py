#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

aprobados = []

def aprueba_becario(nombre_completo):
    #Toma la cadena con el nombre completo, la corta usando el espacio como delimitador y 
    #y lo que se obtiene se mete en una lista, es decir la  lista tendra el nombre y los apellidos 
    #Ahora itera sobre la lista , en caso de ser cualquiera de los descritos abajo sale, de lo contario los agrega
    #A la lista de aprobados (ingresa el nombre completo)
    nombre_separado = nombre_completo.split()
    for n in nombre_separado:
        if n in ['Gerardo', 'Alan', 'Guadalupe', 'Rafael', 'Karina']:
            return False
            
    aprobados.append(nombre_completo.upper())
    aprobados.sort()
    return True

def borra_becario(nombre_completo):
    for n in aprobados:
        if nombre_completo in aprobados:
            aprobados.remove(nombre_completo)
            return True
        else:
            print 'no se encontro al becario %s' %(n)
            return False
            


becarios = ['Becerra Alvarado Hugo Alonso',
            'Cabrera Balderas Carlos Eduardo',
            'Corona Lopez Gerardo',
            'Diez Gutierrez Gonzalez Rafael',
            'Disner Lopez Marco Antonio',
            'Garcia Romo Claudia Fernanda',
            'Gonzalez Ramirez Miguel Angel',
            'Gonzalez Vargas Andrea Itzel',
            'Orozco Avalos Aline Karina',
            'Palacio Nieto Esteban',
            'Reyes Aldeco Jairo Alan',
            'Santiago Mancera Arturo Samuel',
            'Sarmiento Campos Jose',
            'Sarmiento Campos Maria Guadalupe',
            'Valle Juarez Pedro Angel',
            'Viveros Campos Ulises']
for b in becarios:
    if aprueba_becario(b):
        print 'APROBADOO: ' + b.upper()
    else:
        print 'REPROBADO: ' + b.upper()


#print becarios
