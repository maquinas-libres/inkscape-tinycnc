(Scribbled version of /tmp/ink_ext_XXXXXX.svgZ0E5DY @ 3500.00)
( tinycnc.py /tmp/ink_ext_XXXXXX.svgZ0E5DY )
G21 (metric ftw)
G90 (absolute mode)
G92 X45.00 Y40.00 Z0.00 (you are here)

Z20 (pen down)
G4 P150 (wait 150ms)
Z0 (pen up)
G4 P150 (wait 150ms)
M18 (disengage drives)
M01 (Was registration test successful?)
M17 (engage drives if YES, and continue)

(Polyline consisting of 1 segments.)
G1 X15.14 Y69.86 F3500.00
Z20.00 (pen down)
G4 P150 (wait 150ms)
G1 X74.86 Y69.86 F3500.00
G1 X74.86 Y10.14 F3500.00
G1 X15.14 Y10.14 F3500.00
G1 X15.14 Y69.86 F3500.00
Z0.00 (pen up)
G4 P150 (wait 150ms)

(Polyline consisting of 1 segments.)
G1 X30.14 Y54.86 F3500.00
Z20.00 (pen down)
G4 P150 (wait 150ms)
G1 X59.86 Y54.86 F3500.00
G1 X59.86 Y25.14 F3500.00
G1 X30.14 Y25.14 F3500.00
G1 X30.14 Y54.86 F3500.00
Z0.00 (pen up)
G4 P150 (wait 150ms)


(end of print job)
Z0.00 (pen up)
G4 P150 (wait 150ms)
Z0 (turn off servo)
M18 (drives off)
