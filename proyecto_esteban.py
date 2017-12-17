#!/usr/bin/python
# -*- coding: utf-8 -*-
#UNAM-CERT

#Extraccion de informacion de un servidor web
#
#- Obtener la version del servidor web analizando las                               #done
#cabeceras de la respuesta a una peticion HTTP
#
#- Obtener la version de PHP analizando las cabeceras de                            #done
#la respuesta a una peticion HTTP
#
#- Determinar los metodos HTTP habilitados en el Servidor                           #done
#
#- Obtener CMS del servicio web analizando la Respuesta                             #done
#
#- Extraer todos los correos de la pagina
#
#- Buscar en el servidor archivos/directorios mediante una                          #done   
#lista (cuidado con el historial de redirecciones)
#
#- Posibilidad de enviar peticiones a traves de tor                                 #done
#
#- Generar reporte en un archivo .text                                              #done
#
#- Implementar un modo verboso                                                      #done
#
#- Debe implementar un archivo de configuracion en el que se                        #done
#habiliten o deshabiliten las opciones anteriores (el archivo 
#se indica a traves de una bandera)
#
#- Debe implementar banderas para recibir argumentos desde la                       #done
#linea de comandos.  Los argumentos tienen prioridad sobre      
#el archivo de configuracion.

#    - habilitar analisis de cabeceras
#    - habilitar deteccion de metodos HTTP
#    - habilitar extraccion de correos
#    - habilitar peticiones a traves de tor
#    - indicar lista para busqueda de archivos (habilita la busqueda)
#    - indicar nombre del archivo de reporte

#- Cambiar el agente de usuario por uno indicado en el archivo de configuracion     #done   

#- Manejar excepciones para evitar que el programa termine abruptamente             #done


##############################################################################################
######################################### DOCSTRING ##########################################
##############################################################################################

"""

Este software se encarga de realizar consultas a sitios web mediante los metodos definiddos
en http.

Archivo_Configuracion:
    proyecto_esteban.txt

Example:
    >>  python proyecto_esteban.py -p 80 -s proteco.mx -v -w -j -c -e -a
    >>  python proyecto_esteban.py -p 80 -s people.com -v -w -j -c -e -a
    >>  python proyecto_esteban.py -p 80 -s people.com -v -r [both | screen]

Attributes:
    > -v ............................Modo Verbose
    > -w ............................Ver version del Server
    > -j ............................Ver version de php
    > -c ............................Obtener CMS (si lo hay
    > -e ............................Obtener los emails
    > -r ............................Determina donde se mostraran los resultados (both | screen)
    > -t ............................Habilita la solicitudes por tor
    > -m ............................Habilia la deteccion de metodos http
    > -a ............................Habilita la busqueda de archivos
setup:
    pip install requests
    pip install requests[socks]
    pip install pysocks
    apt-get install tor

Aditional Notes:
    >   Si en algún momento durante el envio de solicitud parece que se traba, solo dejalo correr y
        eventualmente vuelve a correr
    >   Antes de probar utilice las pruebas que se adjuntan en el archivo pruebas.txt en este repositorio

"""


import sys
import optparse
import requests
from requests import get
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
debug = False
listofusers = []
metodos = []
listoffiles = ['dump.sql', 'root.txt', 'install', 'admin', 'robots.txt', 'index.php', 'repository.git', 'plugin-cfg.xml', 'src', 'img', 'css', 'logs', 'js']
listofvalidfiles = []
lista = []
dic = {}
reporte = "file_report.txt"
proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}




def printError(msg, exit = False):
        sys.stderr.write('Error:\t%s\n' % msg)
        if exit:
            sys.exit(1)

def addOptions():

    """ 
        Esta metodo sirve para administrar la funcionalidad de las banderas

    """

    parser = optparse.OptionParser()
    parser.add_option('-v','--verbose', dest='verbose', default=None, action='store_true', help='If specified, prints detailed information during execution.')
    parser.add_option('-p','--port', dest='port', default='80', help='Port that the HTTP server is listening to.')
    parser.add_option('-s','--server', dest='server', default=None, help='Host that will be attacked.')
    parser.add_option('-r','--report', dest='report', default=None, help='File where the results will be reported.')
    #parser.add_option('-U', '--user', dest='user', default=None, help='User that will be tested during the attack.')
    #parser.add_option('-P', '--password', dest='password', default=None, help='Password that will be tested during the attack.')
    parser.add_option('-D', '--digest', dest='digest', default=False, help='Autenticacion por metodo Digest')
    parser.add_option('-w','--version', dest='server_version', default=None, action='store_true', help='If specified, returns the servers version')
    parser.add_option('-j','--php', dest='php_version', default=None, action='store_true', help='If specified, returns the servers  php version')
    parser.add_option('-c','--cms', dest='cms_version', default=None, action='store_true', help='If specified, returns the servers  CMS version')
    parser.add_option('-e','--mails', dest='emails', default=None, action='store_true', help='If specified, returns the servers  CMS version')
    parser.add_option('-a','--archivos', dest='archivos', default=None, action='store_true', help='If specified, returns the files founded')
    parser.add_option('-t','--tor', dest='tor', default=None, action='store_true', help='If specified, stablish a connection using tor')
    parser.add_option('-m','--methods', dest='methods', default=None, action='store_true', help='If specified, returns all the methods used by the page')
    

    opts,args = parser.parse_args()
    return opts
    
def checkOptions(options,dic):

    """ 
        Esta metodo sirve para Validar que los datos ingresados sean correctos
        y activar el modo verboso

    """
    if options.verbose is not None:
        debug = True
        if debug: print '[INFO]: Se ha activado el modo verboso ...'
    else:
        debug = False

    print debug
    print (dic['cabeceras'])

    if options.server is None:
        printError('Debes especificar un servidor a atacar.', True)
    else:
        if debug: print '[INFO]: Se ha registrado el servidor a atacar ...'
        
        



    if options.port is not None:
        if debug: print '[INFO]: Se ha escogido el puerto %s ...' %(options.port)

    #debug2 : revisar esta parte de codigo
    if options.report is not None:
        if options.report == 'both':
            if debug: print '[INFO]: Se ha habilitado reporte en pantalla y archivo ...'
        elif options.report == 'screen':
            if debug: print '[INFO]: Se ha habilitado solo el reporte en pantalla ...'


    if options.server_version is not None:
        if debug: print '[INFO]: Se habilita la deteccion de la version del servidor ...'
    else:
        if debug: print '[INFO]: Se intenta localizar la configuración de deteccion de cabeceras en archivo de configuración...'
        if dic['cabeceras'] == 'True':
            if debug: print "[INFO]: Se establece configuración de deteccíon de cabeceras a traves del archivo de configuracion.."
        else:
            if debug: print "[INFO]: No se detecto configuración de deteccion de cabeceras en el archivo..."
            


    if options.php_version is not None:
        if debug: print '[INFO]: Se habilita la deteccion de la version de PHP ...'

    if options.cms_version is not None:
        if debug: print '[INFO]: Se habilita la deteccion de la version de CMS ...'



    if options.emails is not None:
        if debug: print  '[INFO]: Se habilita la deteccion de los correos electronicos...'
    else:
        if debug: print '[INFO]: Se intenta localizar la configuración de deteccion de correos en archivo de configuración...'
        if dic['correos'] == 'True':
            if debug: print "[INFO]: Se establece configuración de deteccíon de correos a traves del archivo de configuracion.."
        else:
            if debug: print "[INFO]: No se detecto configuración de deteccion de correos en el archivo..."
            



    if options.archivos is not None:
        if debug: print '[INFO]: Se habilita la deteccion de archivos en el servidor ...'
    else:
        if debug: print '[INFO]: Se intenta localizar la configuración de deteccion de archivos en archivo de configuración...'
        if dic['lista'] != ' ':
            #[PEND] Quiza de error por el salto de linea del final, revisar
            lista = dic['lista'].split(",")
            if debug: print "[INFO]: Se establece configuración de deteccion de archivos a traves del archivo de configuracion.."
        else:
            if debug: print "[INFO]: No se detecto configuración de deteccion de archivos en el archivo..."
        


    if options.tor is not None:
        if debug: print '[INFO]: Se ha habilitado el uso de conexion mediante tor ...'
    else:
        if debug: print '[INFO]: Se intenta localizar la configuración de solicitudes con tor en archivo de configuración...'
        if dic['tor'] == 'True':
            if debug: print "[INFO]: Se establece configuración de solicitudes con tor a traves del archivo de configuracion.."
        else:
            if debug: print "[INFO]: No se detecto configuración de solicitudes con tor en el archivo..."
        


    if options.methods is not None:
        if debug: print '[INFO]: Se ha habilitado la detección de metodos http usados por el servidor ...'
    else:
        if debug: print '[INFO]: Se intenta localizar la configuración de deteccion de metodos en archivo de configuración...'
        if dic['metodos'] == 'True':
            if debug: print "[INFO]: Se establece configuración de deteccíon de metodos a traves del archivo de configuracion.."
        else:
            if debug: print "[INFO]: No se detecto configuración de deteccion de metodos en el archivo..."
        

    if dic['reporte'] != ' ':
        #[PEND] Quiza de error por el salto de linea del final, revisar
        reporte = dic['reporte']

    if dic['agent'] != ' ':
        return dic['agent']





def reportResults(options,response,dic,agente_usuario):
    #pass
    """ 
        Esta metodo sirve para reportar al usuario por medio de pantalla
        o de archivo los resultados del escaneo

    """

    soup = BeautifulSoup(response.text,"lxml")
    #print (soup.find_all(attrs={"name": "generator"}))
    emails = [a["href"] for a in soup.select('a[href^=mailto:]')]
    #print (emails)
    metodos = pruebas_metodos_http()
    #for m in metodos:
    #    print (m)
    
    
    if options.report == 'both':
        
        file_report = open(reporte,"w")
        file_report.write ('\n\n\n\n')
        file_report.write ('==========================================================================')
        file_report.write ('================================Reporte===================================')
        file_report.write ('==========================================================================')
        file_report.write ('\n\n')
        file_report.write('\nSevidor = \t\t\t\t'    + str(options.server)               + '\n')
        file_report.write('Puerto = \t\t\t\t'       + options.port                      + '\n')
        file_report.write('Url = \t\t\t\t\t'        + response.url                      + '\n')
        file_report.write('Codificacion = \t\t\t\t' + response.encoding                 + '\n')
        file_report.write('Status Code = \t\t\t\t'  + str(response.status_code)         + '\n')
        #file_report.write('Cookies = \t\t'          + str(response.cookies)             + '\n')
        file_report.write('Cabeceras = \t\t\t\n')
        file_report.write('Redireccionado? = \t\t\t'+ str(response.is_redirect)         + '\n')
        file_report.write('Respuestan(seg) =\t\t\t '+ str(response.elapsed)             + '\n')
        file_report.write('Historial = \t\t\t\t'    + str(response.history)             + '\n') 
        file_report.write("User Agent = \t\t\t\t"     + str(agente_usuario)                      + '\n')
        #file_report.write('Texto = \t\t'            + str(response.text)                + '\n') 
        if options.server_version is not None: 
            file_report.write('Version del Servidor= \t\t\t:'           + str(response.headers['Server'])       + '\n')
        else:
            if dic['cabeceras'] == 'True':
                file_report.write('Version del Servidor= \t\t\t:'           + str(response.headers['Server'])       + '\n')


        if options.emails is not None:
            file_report.write('Emails encontrados = \t\t\t' + str(emails)+ '\n')
        else:
            if dic['correos'] == 'True':
                file_report.write('Emails encontrados = \t\t\t' + str(emails)+ '\n')

        if options.methods is not None:
            file_report.write('Metodos usado por el servidor = \t'      + str(metodos) + '\n')
        else:
            if dic['metodos'] == 'True':
                file_report.write('Metodos usado por el servidor = \t'      + str(metodos) + '\n')



        if options.php_version is not None: 
            file_report.write('Version de PHP =  \t\t\t'                + str(response.headers['X-Powered-By']) + '\n')
        
        if options.archivos is not None:
            file_report.write('Archivos encontrados = \t\t\t'           + str(listofvalidfiles)                 + '\n')
        
        if options.cms_version is not None:
            if soup.find_all(attrs={"name": "generator"}):
                file_report.write ('Version del CMS = \t\t\t ' + str(soup.find_all(attrs={"name": "generator"})))
            else:
                file_report.write ('Version del CMS = \t\t\t¡NO SE ECONTRO CMS!')
        file_report.write ('\n\n')
        file_report.write ('==========================================================================')
        file_report.write ('==========================================================================')
        file_report.write ('\n\n\n\n\n\n')


        file_report.close()
        #if debug: print 'El contenido de la variable es: '
        #if debug: print debug
        if debug: print '[INFO]: Se ha escrito el reporte en el archivo ./file_report.txt'
    print ('\n\n\n\n')
    print ('==========================================================================')
    print ('================================Reporte===================================')
    print ('==========================================================================')
    print ('\n\n')
    print ('Sevidor = \t\t\t\t'        + options.server                           + '\n')
    print ('Puerto = \t\t\t\t'         + options.port                             + '\n')
    print ('Url = \t\t\t\t\t'          + response.url                             + '\n')
    print ('Codificacion = \t\t\t\t'   + response.encoding                        + '\n')
    print ('Status Code = \t\t\t\t'    + str(response.status_code)                + '\n')
    print ('Redireccionado? = \t\t\t'  + str(response.is_redirect)                + '\n')
    print ('Respuesta (seg) = \t\t\t'  + str(response.elapsed)                    + '\n')
    print ('Historial = \t\t\t\t'      + str(response.history)                    + '\n')
    print ("User Agent = \t\t\t\t"     + str(agente_usuario)                      + '\n')
    #print ('Cookies = \t\t')
    #print (response.cookies)  
    #print ('Cabeceras = \t\t')
    #print (response.headers) 
    if options.server_version is not None: 
        print ('Version del Sevidor = \t\t\t'+ str(response.headers['Server'])+ '\n')
    else:
        if dic['cabeceras'] == 'True':
                print ('Version del Servidor= \t\t\t:'+ str(response.headers['Server'])+ '\n')
    
    if options.emails is not None:
        print('Emails encontrados = \t\t\t'+ str(emails)+ '\n')
    else:
        if dic['correos'] == 'True':
            print('Emails encontrados = \t\t\t'+ str(emails)+ '\n')

    if options.methods is not None:
        print('Metodos usado por el servidor = \t'+ str(metodos)+ '\n')
    else:
        if dic['metodos'] == 'True':
            print('Emails encontrados = \t\t\t'+ str(emails)+ '\n')

    if options.php_version is not None: 
        print ('Version de PHP = \t\t\t'+ str(response.headers['X-Powered-By']) + '\n')       
    if options.archivos is not None:
        print('Archivos encontrados = \t\t\t '            + str(listofvalidfiles)                 + '\n')
    if options.cms_version is not None:
        if soup.find_all(attrs={"name": "generator"}):
            print ('Version del CMS = \t\t\t ' + str(soup.find_all(attrs={"name": "generator"})))
        else:
            print ('Version del CMS =\t\t\t¡NO SE ECONTRO CMS!')
    print ('\n\n')
    print ('==========================================================================')
    print ('==========================================================================')
    print ('\n\n\n\n\n\n')

def get_tor_session():
    session = requests.sesion()
    sesion.proxies =    {
                            'http':     'socks5://localhost:9050',
                            'https':    'socks5://localhost:9050'
                        }
    return session

def archivo_configuracion():
    file_config = open("proyecto_esteban.txt","r+")
    renglones = file_config.readlines()
    contnido = file_config.read()
    #print (renglones)
    #print (contnido)
    for line in renglones:
        if '#' not in  line:
            #print (line)
            lista = line.split(':')
            dic[lista[0]] = lista[1][:-1]

    return dic


def pruebas_metodos_http():
    r = requests.get(url)
    if r.status_code == 200: metodos.append('get')
    r = requests.post(url)
    if r.status_code == 200: metodos.append('post')
    r = requests.head(url)
    if r.status_code == 200: metodos.append('head')
    r = requests.put(url)
    if r.status_code == 200: metodos.append('put') 
    r = requests.delete(url)
    if r.status_code == 200: metodos.append('delete')
    r = requests.options(url)
    if r.status_code == 200: metodos.append('options')
    r = requests.get(url)
    if r.status_code == 200: print metodos.append('trace')

    #<form action="fichero.py/funcion" method="post"
    #print (soup.meta['name'])
    #print ("###############################################")
    #for sub_heading in soup.find_all('form'):
    #    if sub_heading['action']:
    #         print (str(soup.find_all('form')))
        #print "\n\n\n$$$$$$$$$$$$$$$$$$$44yeah"
        #print(str(sub_heading) + '\n')
        #print(str(sub_heading.text))
        #print(soup.meta['content'])
        #print(sub_heading.text)
        #print(sub_heading.contents['meta'])
        #letters = soup.find_all("div", class_="ec_statements")
        #data_soup.find_all(attrs={"name": "generator"})


    return metodos



def buildURL(server,port, protocol = 'http',file = ""):
    """ 
        Esta metodo sirve para administrar la funcionalidad de las banderas

    """
     #for i in string:
     #   if (i == '/'):
     #       bandera = True

    if '/' in server:
        url = '%s://%s/%s' % (protocol,server,file)
    else:
        url = '%s://%s:%s/%s' % (protocol,server,port,file)
    return url


def makeRequest(host,digest,opts,agente_usuario,dic):
    """ 
        Esta metodo sirve para realizar las consultas al servidor web
    """
    try:
            if debug: print '[INFO]: Eviando la solicitud al servidor ...'
            #user_agent = {'User-agent': 'Mozilla/5.0'}
            #print (agente_usuario)
            user_agent = {'User-agent':agente_usuario}
            #print (user_agent)

            if opts.tor is not None:
                #Do something related to tor connection
                print '[INFO]: Enviando solicitud por medio de tor ...'
                #url = 'http://ifconfig.me/ip'   
                response = requests.get(host, proxies=proxies)
                #print('tor ip: {}'.format(response.text.strip()))
            elif opts.tor is None and dic['tor'] != 'True':
                #response  = requests.get(url, headers = user_agent, config=debug)
                response = requests.get(host, headers = user_agent)
                print(response.status_code)
                if response.status_code == 200:
                    print '[INFO]: Respuesta obtenida con exito '
                else:
                    print '[INFO]: NO FUNCIONO la respuesta :c '  
                    #print response
                    #print dir(response)

                for archivo in listoffiles:
                    hostforfiles = buildURL(opts.server, port = opts.port,file = archivo)
                    respuesta = requests.get(hostforfiles, headers = user_agent)
                    if respuesta.status_code == 200:
                        listofvalidfiles.append(archivo)
                        if debug: print ('[INFO]: Se ha podido localizar al archivo: %s' %archivo)
            else:
                if dic['tor'] == 'True':
                    print '[INFO]: Enviando solicitud por medio de tor ...'
                    response = requests.get(host, proxies=proxies)

      
        
	
    except ConnectionError:
        printError('Error en la conexion, tal vez el servidor no esta arriba.',True)

    return response


if __name__ == '__main__':
    try:
        opts = addOptions()
        config_file = archivo_configuracion()
        agente_usuario = checkOptions(opts,config_file)
        url = buildURL(opts.server, port = opts.port)
        print url
        request1 = makeRequest(url,opts.digest,opts,agente_usuario,config_file)
        #print request1
        reportResults(opts,request1,config_file,agente_usuario)
    except Exception as e:
        printError('Ocurrio un error inesperado')
        printError(e, True)
