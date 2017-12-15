#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

sistemas = ['angie','juan','jonatan']
op_interna = ['quintero','fernando','yeudiel']
incidentes = ['demian','anduin','diana','victor','vacante']
auditorias = ['juan','fernando','oscar','daniel','gonzalo','cristian','jorge','virgilio']


#expresion funcional:
# 1) funcion lambda que sume las cuatro listas
# 2) filtre la lista resuloptante para obtener todos los nombres que tienen una "i"
# 3) convierta a mayusculas el resultado anterior
#UNA SOLA EXPRESION



j = map(lambda y: y.upper(),(filter(lambda x: 'i' in x,(lambda x,y,z,w: x + y + z + w)(sistemas,op_interna,incidentes,auditorias))))
print j