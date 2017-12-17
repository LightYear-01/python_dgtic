#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Tarea 5
#
#Modificar el archivo req.py del ejercicio anterior.
#Implementar la bandera del modo verboso(-v)                    #done   
#Implementar una bandera que permita peticiones vía HTTPS.      #done   
#
#
#Se debe de poder indicar un usuario o una lista de usuarios.   #done   
#Se debe de poder indicar una contraseña o una lista de
#contraseñas.
#
#
#La bandera de reporte debe de servir para determinar si los    
#hallazgos se escriben en la pantalla, en un archivo o en ambos.#done
#El archivo de reporte debe de contener toda la información
#correspondiente al ataque.                                     
#
#Implementar el ataque para autenticación DIGEST.
#Debe de tener todas las validaciones necesarias para que           #done
#funcione correctamente.
#
#
import sys
import optparse
from requests import get
from requests.exceptions import ConnectionError
debug = False
listofusers = []

def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():
    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-D', '--digest', dest='digest', default=False, help='Autenticacion por metodo Digest')
    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options):
    if options.verbose is not None:
        debug = True
        if debug: print '[INFO]: Se ha activado el modo verboso ...'
    else:
        debug = False

    print debug

    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    else:
        if debug: print '[INFO]: Se ha registrado el servidor a atacar ...'

    if options.port is not None:
        if debug: print '[INFO]: Se ha escogido el puerto %s ...' %(options.port)

    #debug2 : revisar esta parte de codigo
    if options.report is not None:
        if options.report == 'both':
            if debug: print '[INFO]: Se ha habilitado reporte en pantalla y archivo'
        elif options.report == 'screen':
            if debug: print '[INFO]: Se ha habilitado solo el reporte en pantalla'
    


def reportResults(options,response):
    #pass

    if options.report == 'both':
        
        file_report = open("file_report.txt","w")
        
        file_report.write('================================Reporte===================================')
        file_report.write('\nSevidor = \t\t'        + str(options.server)       + '\n')
        file_report.write('Puerto = \t\t'           + options.port              + '\n')
        file_report.write('Url = \t\t'              + response.encoding         + '\n')
        file_report.write('Codificacion = \t\t'     + response.encoding         + '\n')
        file_report.write('Status Code = \t\t'      + str(response.status_code) + '\n')
        file_report.write('Cookies = \t\t'          + str(response.cookies)     + '\n')
        file_report.write('Cabeceras = \t\t\n')
        file_report.write('Redireccionado? = \t\t'  + str(response.is_redirect)  + '\n')
        file_report.write('Tiempo de Respuesta = '  + str(response.elapsed)      + '\n')
        file_report.write('Historial = \t\t'        + str(response.history)      + '\n') 
        file_report.write('Texto = \t\t'            + str(response.text)         + '\n') 
        file_report.close()
        #if debug: print 'El contenido de la variable es: '
        #if debug: print debug
        if debug: print '[INFO]: Se ha escrito el reporte en el archivo ./file_report.txt'

    print ('================================Reporte===================================')
    print ('Sevidor = \t\t'          + options.server        + '\n')
    print ('Puerto = \t\t'           + options.port          + '\n')
    print ('Url = \t\t'              + response.encoding     + '\n')
    print ('Codificacion = \t\t'     + response.encoding     + '\n')
    print ('Status Code = \t\t'      + str(response.status_code)  + '\n')
    print ('Cookies = \t\t')
    print (response.cookies)  
    print ('Cabeceras = \t\t')
    print (response.headers)
    print ('Redireccionado? = \t\t'  + str(response.is_redirect)  + '\n')
    print ('Tiempo de Respuesta = '  + str(response.elapsed)      + '\n')
    print ('Historial = \t\t'        + str(response.history)      + '\n') 
    print ('Texto = \t\t'            + response.text         + '\n')   



def buildURL(server,port, protocol = 'http'):
    url = '%s://%s:%s' % (protocol,server,port)
    return url


def makeRequest(host, user, password,digest):
    try:
        print ('[INFO]: El contenido de la variable digest = ' + str(digest))
        if digest == True:
            response = get(host, auth=HTTPDigestAuth(user, password))
            print '[INFO]: Se ha realizado autenticacion Digest'
        else:
            response = get(host, auth=(user,password))
            print '[INFO]: Se ha realizado autenticacion basica'


	print response
	#print dir(response)
	if response.status_code == 200:
	    print '>>> CREDENCIALES ENCONTRADAS!: %s\t%s' % (user,password)
	else:
	    print 'NO FUNCIONO :c '
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

    return response


if __name__ == '__main__':
    try:
        opts = addOptions()
        checkOptions(opts)
        url = buildURL(opts.server, port = opts.port)
        print url
        request1 = makeRequest(url, opts.user, opts.password,opts.digest)
        #print request1
        reportResults(opts,request1)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
