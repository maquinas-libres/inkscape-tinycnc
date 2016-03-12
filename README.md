G-Code de TinyCNC para Inkscape
===============================

Extensión de inkscape para exportar codigo G-Code para TinyCNC

Instalar
========

Copiar la extensión y templates en inkscape:

* OS X - `/Applications/Inkscape.app/Contents/Resources/`
* GNU/Linux - `/usr/share/inkscape/extensions` o `~/.config/inkscape/`
* Windows - `C:\Program Files\Inkscape\share\`

Uso
===

![img](img/template.png)
> Al abrir el inkscape elegí como template "TinyCNC" esto va a mostrarnos el area dibujable

![img](img/dibujar.png)
> Dibuja lo que quieras :D

![img](img/exportar.png)
> Grabalo como "G-Code para TinyCNC"

Una vez obtenido el G-Code vamos a tener que usar un programa para comunicarnos con la impresora por ahora el más recomendable es [cncgcodecontroller](...)

Creditos
========

* [Marty McGuire](http://github.com/martymcguire) pulled this all together into an Inkscape extension.
* [Inkscape](http://www.inkscape.org/) is an awesome open source vector graphics app.
* [Scribbles](https://github.com/makerbot/Makerbot/tree/master/Unicorn/Scribbles%20Scripts) is the original DXF-to-Unicorn Python script.
* [The Egg-Bot Driver for Inkscape](http://code.google.com/p/eggbotcode/) provided inspiration and good examples for working with Inkscape's extensions API.


Quehaceres
==========

* Más ejemplos
