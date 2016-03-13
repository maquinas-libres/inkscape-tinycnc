#!/bin/bash

cd /tmp
wget https://github.com/maquinas-libres/inkscape-tinycnc/archive/master.zip -O master.zip
unzip master.zip
cd inkscape-tinycnc-master
cp -r src/ ~/.config/inkscape/
