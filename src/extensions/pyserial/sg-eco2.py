#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#----------------------------------------------------------------------------
# sg-eco2.py  Ejemplo de manejo del puerto serie desde python utilizando la
# libreria multiplataforma pyserial.py (http://pyserial.sf.net)
#
#  Se envia una cadena por el puerto serie y se muestra lo que se recibe
#  Se puede especificar por la linea de comandos el puerto serie a 
#  a emplear
#
#  (C)2002 Chris Liechti (cliechti@gmx.net)
#  (C)2007 Juan Gonzalez
#
#  LICENCIA GPL
#-----------------------------------------------------------------------------

import sys
import getopt
import serial

#--------------------------------
#-- Imprimir mensaje de ayuda  
#--------------------------------
def help():
    sys.stderr.write("""Uso: sg-eco2 [opciones]
    Ejemplo de uso del puerto serie en Python

    opciones:
    -p, --port=PORT: Puerto serie a emplear. Bien un numero o una cadena
    
    Ejemplo:
      sg-eco2 -p 0          --> Usar el primer puerto serie (Linux/Windos)
      sg-eco2 -p /dev/ttyS1 --> Especificar el dispositivo serie (Linux) 
      
    """)

#-----------------------------------------------------
#--  Analizar los argumentos pasados por el usuario
#--  Devuelve el puerto seleccionado
#-----------------------------------------------------
def Analizar_argumentos():
  
  Puerto = 0
  
  try:
    opts, args = getopt.getopt(sys.argv[1:],
          "hp:",
          ["help", "port="]
    )
  except getopt.GetoptError:
    # print help information and exit:
    help()
    sys.exit(2)

  #-- Leer argumentos pasados
  for o, a in opts:
    if o in ("-h", "--help"):
      help()
      sys.exit()
    elif o in ("-p", "--port"): 
      try:
        Puerto = int(a)
      except ValueError:
        Puerto = a

  return Puerto


#----------------------
#   MAIN
#----------------------

#-- Analizar los argumentos pasados por el usuario
Puerto = Analizar_argumentos()

#-- Cadena de pruebas a enviar
Cadena = "Hola como estas"

#-- Sacar Mensaje inicial
print "Pruebas del puerto serie"

#--------------------------------------------------------
#-- Abrir el puerto serie. Si hay algun error se termina
#--------------------------------------------------------
try:
  s = serial.Serial(Puerto, 9600)
  
  #-- Timeout: 1 seg
  s.timeout=1;
  
except serial.SerialException:
  #-- Error al abrir el puerto serie
  sys.stderr.write("Error al abrir puerto %s" % str(Puerto))
  sys.exit(1)

#-- Mostrar el nombre del dispositivo
print "Puerto (%s): (%s)" % (str(Puerto),s.portstr)

#-------------------------------------------------
#-- Aqui empieza la prueba
#-------------------------------------------------

#-- Enviar la cadena de pruebas
print "ENVIADO : " + Cadena
s.write(Cadena);

#-- Esperar hasta recibir la cadena enviada...
#-- O hasta que haya un timeout
recibido = s.read(len(Cadena));

#-- Comprobar lo recibido
if len(recibido)!=0:

  #--Cadena recibida. Imprimirla
  print "RECIBIDO: " + recibido
  
  #-- Comprobar si lo que se ha recibo es exactamente lo mismo que lo
  ##-- enviado
  if recibido==Cadena:
    print "OK!"
  else:
    print "Error!"
    
else:
  #-- No se ha recibido ninguna cadena: timeout
  print "TIMEOUT";

#-- Cerrar puerto serie
s.close()
