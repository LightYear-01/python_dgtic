#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Ejercicio de clase 6
#• Hacer un diccionario por comprensión.
#• Las llaves son los números odiosos menores
#a 50 y el valor es una tupla de dos elementos:
#su representación en binario y su
#representación en hexadecimal.
#• Un número odioso (odious number) es todo
#aquél que su representación en binario tiene
#un número impar de unos.

diccionario = {}
lista = [n for n in range(50) if bin(n).count('1') % 2 != 0]
for l in lista:
	diccionario[bin(l)] = hex(l)
