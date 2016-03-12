(Scribbled version of /tmp/ink_ext_XXXXXX.svgKFRAEY @ 3500.00)
( tinycnc.py /tmp/ink_ext_XXXXXX.svgKFRAEY )
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
G1 X15.09 Y69.91 F3500.00
Z20.00 (pen down)
G4 P150 (wait 150ms)
G1 X74.91 Y69.91 F3500.00
G1 X74.91 Y10.09 F3500.00
G1 X15.09 Y10.09 F3500.00
G1 X15.09 Y69.91 F3500.00
Z0.00 (pen up)
G4 P150 (wait 150ms)

(Polyline consisting of 1 segments.)
G1 X30.05 Y54.95 F3500.00
Z20.00 (pen down)
G4 P150 (wait 150ms)
G1 X59.95 Y54.95 F3500.00
G1 X59.95 Y25.05 F3500.00
G1 X30.05 Y25.05 F3500.00
G1 X30.05 Y54.95 F3500.00
Z0.00 (pen up)
G4 P150 (wait 150ms)


(end of print job)
Z0.00 (pen up)
G4 P150 (wait 150ms)
Z0 (turn off servo)
G1 X0 Y0 F3500.00
G1 Z0.00 F150.00 (go up to finished level)
G1 X45.00 Y40.00 F3500.00 (go home)
M18 (drives off)
