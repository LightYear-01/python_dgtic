#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT


#Tarea 3 – Generador de diccionarios
#•
#•
#Se deberá leer un archivo que contendrá en cada
#renglón una palabra sobre alguna persona (nombre,
#nombre de mascota, color favorito, etc). Al menos 10
#renglones.
#Deberá generar una lista de posibles contraseñas
#usando diversas técnicas:


#•Cambiar letras por números
#•Cambiar numeros por letras
#•Pasar de mayúsculas a minúsculas
#•Pasar de minúsculas a mayúsculas

#•Concatenar usando números y símbolos especiales
#•Etcétera
import random 
listofnumbers = ['0','1','2','3','4','5','6','7','8','9']
numtochar = {'0':'O','1':'L','3':'E','4':'A','5':'S','6':'G','7':'T','8':'B'}
chartonum = {'O':'0','L':'1','E':'3','A':'4','S':'5','G':'6','T':'7','B':'8'}
specialcaracterslist = ['#','!','$','%','&','?','¡','¿','+',':',';','*']
listapasswords = []
contenido = ''
password = ''	
listaletrascambiables=[]
listanumeroscambiables=[]
	#listapasswords = []


#La lista generada deberá escribirse en un nuevo
#archivo (una contraseña por línea)



def mapchartonum(n):
	return chartonum[n]

def mapnumtochar(n):
	return numtochar[n]

def readfile():
	diccionario = open('diccionario.txt','r')
	contenido = diccionario.readlines()

def genpassword():

	#Primer unir un numero de palabras aleatorias de la lista mediante caracteres especiales
	#password = ''	
	#listaletrascambiables=[]
	#listanumeroscambiables=[]
	#listapasswords = []

     cuantos = contenido.count()
     for i in range(0,random.randrange(cuantos)):
		password += random.choice(contenido)
		password += random.choice(specialcaracterslist)

	#Segundo paso: cambiar letras por numeros y vice versa
	#primeosaber cuantos numeros y letras tiene
	#sacar un random de esa cantidad para determinar el numero de cambios.
	#primero saber cuantos y luego cuales

	#playstation%america#rojo     (3,5,6,7,8,9,10,13,-1,17,19,22,24) 13 -> 5
	#pl4y574710n%4m3r1c4#r0j0

	#Determinando cuales letras y numeros pueden ser cambiadas
     cuantos = password.count()
     for i in range(0,cuantos):
		if password[i].upper() in ['O','L','E','A','S','G','T','B']:
			listaletrascambiables.append(i)
		elif password[i] in ['0','1','3','4','5','6','7','8']:
			listanumeroscambiables.append(i)

    #Determinando cuantos seran cambiados
    numeros = random.randrange(listanumeroscambiables.count())
    letras = random.randrange(listaletrascambiables.count())
    
	#Cuantas numeros seran cambiadas
	for i in range(0,numeros):
		#Determinando cuales seran cambiados
		donde = random.randrange(listanumeroscambiables.count())
		if donde != -1:
			password[listanumeroscambiables[donde]] = numtochar[password[listanumeroscambiables[donde]]]
			listanumeroscambiables[donde] = -1
		else:
			continue

	#Cuantas letras seran cambiadas
	for i in range(0,letras):
		#Determinando cuales seran cambiados
		donde = random.randrange(listaletrascambiables.count())
		if donde != -1:
			password[listaletrascambiables[donde]] = numtochar[password[listaletrascambiables[donde]]]
			listaletrascambiables[donde] = -1
		else:
			continue



	#Cuales a minusculas
	minusculas = random.randrange(password.count())
	for i in range(0,minusculas):
		#Determinando cuales seran cambiados
		whichminusculas = random.randrange(password.count())
		password[whichminusculas].lower
		


	listapasswords.append(password)




def creararchivocontrasenias():
	archivocontrasenias = open('archivocontrasenias.txt','w')
	for i in range (0,listapasswords.count()):
		archivocontrasenias.write(listapasswords[i])



	

diccionario = open('diccionario.txt','r')
contenido = diccionario.readlines()
genpassword()
creararchivocontrasenias()

















