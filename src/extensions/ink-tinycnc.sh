#!/bin/bash
#
#	Imprimir desde la terminal un gcode
#	AGPLv3 © Ernesto Bazzano
#

PUERTO=$(ls /dev/ttyUSB* 2> /dev/null | head -n1)
[ "$PUERTO" == "" ] && echo "Conecte el tinyCNC" > /dev/stderr && exit

(sleep 3; $( dirname $0 )/tinycnc.py $@ | grep ^G1 | cut -d'(' -f1 | cut -dF -f1 )| while read A; do
	echo $A
	sleep .5
done | cu -l $PUERTO -s 115200 > /dev/null
