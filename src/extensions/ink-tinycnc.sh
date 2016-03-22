#!/bin/bash
#
#	Imprimir desde la terminal un gcode
#	AGPLv3 © Ernesto Bazzano
#

PUERTO=$(ls /dev/ttyUSB* | head -n1)
echo $PUERTO

[ "$PUERTO" == "" ] && exit

T=$(cat $1 | grep ^G1 | wc -l)
N=0
(sleep 3; $( dirname $0 )/tinycnc.py | grep ^G1 | cut -d'(' -f1 | cut -dF -f1 )| while read A; do
	echo $((100/$T*$N)) > /dev/stderr
	N=$((N=N+1))
	echo $A
	sleep 1
done | cu -l $PUERTO -s 115200 > /dev/null
