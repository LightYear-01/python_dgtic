#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice
from poo1 import Becario

calificacion_alumno = {}
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
becarios_objects_lists = []
becarios = ['Alonso',
            'Eduardo',
            'Gerardo',
            'Rafael',
            'Antonio',
            'Fernanda',
            'Angel',
            'Itzel',
            'Karina',
            'Esteban',
            'Alan'
,            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    #for b in becarios:
    #    calificacion_alumno[b] = choice(calificaciones)
    for b in becarios:
        b_temp = Becario(b,choice(calificaciones))
        becarios_objects_lists.append(b_temp)


def imprime_calificaciones():
    for alumno in becarios_objects_lists:
        print '%s tiene %s\n' % (alumno.nombre,alumno.calificacion)

asigna_calificaciones()
imprime_calificaciones()



#POO – Ejercicio de clase 4
#• Descargar: poo1.py
#• Descargar: ejercicio4.py
#• Las clases deben mantenerse en un archivo
#separado (poo1.py)
#• Modificar el archivo ejercicio3.py para que no
#agregue los becarios y calificaciones en un
#@diccionario.
#• En lugar de generar un diccionario, generar
#una lista de objetos de la clase Becario.