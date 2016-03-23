#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
#----------------------------------------------------------------------------
# scan.py  Modulo para obtener una lista de los puertos series disponibles
#----------------------------------------------------------------------------
# Notas: En Linux solo se detectan los puertos del tipo /dev/ttySx 
# disponibles, que son a los que la libreria pyserial les asigna los 
# valores 0, 1, 2, etc.  Los dispositivos del tipo /dev/ttyUSBx no se
# detectan. Para poder usarlos como cualquier otro dispositivo, se 
# puede hacer un enlace simbolico:
#   # ln -s /dev/ttyUSB0 /dev/ttyS10
# Asociamos el dispositivo ttyUSB0 a uno del tipo ttyS10. En ese caso si 
# se detecta correctamente con esta rutina. En este ejemplo devolveria el
# valor 10 (si realmente en /dev/ttyUSB0 hay un conversor usb-serie)
#----------------------------------------------------------------------------
#
#  (C)2002 Chris Liechti (cliechti@gmx.net)
#  (C)2007 Juan Gonzalez
#
#  LICENCIA GPL
#----------------------------------------------------------------------------

import sys
import serial

#-----------------------------------------------------------------------------
# Buscar puertos series disposibles. 
# ENTRADAS:
#   -num_ports : Numero de puertos a escanear. Por defecto 20
#   -verbose   : Modo verboso True/False. Si esta activado se va 
#                imprimiendo todo lo que va ocurriendo
# DEVUELVE: 
#    Una lista con todos los puertos encontrados. Cada elemento de la lista
#    es una tupla con el numero del puerto y el del dispositivo 
#-----------------------------------------------------------------------------
def scan(num_ports = 20, verbose=True):
   
    #-- Lista de los dispositivos serie. Inicialmente vacia
    dispositivos_serie = []
    
    if verbose:
      print "Escanenado %d puertos serie:" % num_ports
    
    #-- Escanear num_port posibles puertos serie
    for i in range(num_ports):
    
      if verbose:
        sys.stdout.write("puerto %d: " % i)
        sys.stdout.flush()
    
      try:
      
        #-- Abrir puerto serie
        s = serial.Serial(i)
        
        if verbose: print "OK --> %s" % s.portstr
        
        #-- Si no hay errores, anadir el numero y nombre a la lista
        dispositivos_serie.append( (i, s.portstr))
        
        #-- Cerrar puerto
        s.close()
            
      #-- Si hay un error se ignora      
      except:
        if verbose: print "NO"
        pass
        
    #-- Devolver la lista de los dispositivos serie encontrados    
    return dispositivos_serie


#--------------------------
# Pruebas del modulo Scan 
#--------------------------
if __name__=='__main__':

  
  #-- Escanear los puertos.
  #-- Se puede indicar el numero de puertos a escaner
  #-- El modo "verbose" esta activado por defecto. Se desactiva con False
  puertos_disponibles=scan(num_ports=20,verbose=True)
  
  #-- Recorrer la lista mostrando los que se han podido abrir
  print ""
  print "Puertos detectados:"
  if len(puertos_disponibles)!=0:
    for n,nombre in puertos_disponibles:
      print "  (%d) %s" % (n,nombre)
  else:
    print "  Ninguno"
