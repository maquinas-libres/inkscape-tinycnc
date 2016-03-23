#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

#----------------------------------------------------------------------------
# sg-eco1.py  Ejemplo de manejo del puerto serie desde python utilizando la
# libreria multiplataforma pyserial.py (http://pyserial.sf.net)
#
#  Se envia una cadena por el puerto serie y se muestra lo que se recibe
#
#  (C)2002 Chris Liechti (cliechti@gmx.net)
#  (C)2007 Juan Gonzalez
#
#  LICENCIA GPL
#----------------------------------------------------------------------------

import sys
import serial


#-- Valor por defecto del puerto a usar
#-- Para que sea multiplataforma hay que emplear numeros entre 0 y 255
#-- Pero tambien se pueden usar cadenas ej. /dev/ttyUSB0 en Linux
Puerto = 0

#-- Cadena de pruebas a enviar
Cadena = "Hola como estas"


#-- Sacar mensaje inicial
print "Pruebas del puerto serie"


#----------------------------------------------------------
#-- Abrir el puerto serie. Si hay algun error se termina
#----------------------------------------------------------
try:
  s = serial.Serial(Puerto, 9600)
  s.timeout=1;
  
except serial.SerialException:
  #-- Error al abrir el puerto serie
  sys.stderr.write("Error al abrir puerto (%s)\n" % str(Puerto))
  sys.exit(1)

#-- Mostrar el nombre del dispositivo serie utilizado
print "Puerto (%d): %s" % (Puerto,s.portstr)


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
