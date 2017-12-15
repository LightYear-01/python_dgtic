#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT
from random import choice

calificacion_alumno = {}
aprobados = []
reprobados = []
calificaciones = (0,1,2,3,4,5,6,7,8,9,10)
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
            'Alan',
            'Samuel',
            'Jose',
            'Guadalupe',
            'Angel',
            'Ulises']

def asigna_calificaciones():
    for b in becarios:
        calificacion_alumno[b] = choice(calificaciones)

def imprime_calificaciones():
    for alumno in calificacion_alumno:
        print '%s tiene %s\n' % (alumno,calificacion_alumno[alumno])

def whoiswho():
    for b in becarios:
        if calificacion_alumno[b] >= 8:
            aprobados.append(b)
        elif calificacion_alumno[b] < 8:
            reprobados.append(b)
    return (tuple(aprobados),tuple(reprobados))

def promedio():
    sum = 0
        
    for b in becarios:
        sum += calificacion_alumno[b]
    prom = float(sum / len(calificacion_alumno))
    return prom

def conjunto_calificaciones():
    calification_set = set() 
    for b in becarios:
        calification_set.add(calificacion_alumno[b])
    return calification_set



asigna_calificaciones()
imprime_calificaciones()





#Ejercicio de clase 3
#•
#•
#Descargar: ejercicio3.py
#Hacer función que regrese dos tuplas:
#•
#•
#Nombres de los alumnos aprobados (calificación >= 8)
#Nombres de los alumnos reprobados (calificación < 8 )
#• Hacer función que regrese el promedio de calificaciones
#de los alumnos (número real)
#• Hacer función que regrese el conjunto de las
#calificaciones obtenidas.