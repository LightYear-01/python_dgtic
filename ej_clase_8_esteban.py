#Ejercicio de clase 8
#• Hacer una expresión regular que coincida con
#una dirección IP versión 4

^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$ 


#• Hacer expresión regular que coincida con una
#dirección de correo electrónico

^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$