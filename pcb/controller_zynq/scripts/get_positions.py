#!/bin/python

import math
pinout = {
    "D0":    {"bank": 34, "type": "LP", "io": 12},
    "MCLK0": {"bank": 13, "type": "LP", "io": 21},
    "MCLK1": {"bank": 34, "type": "LP", "io": 14},
    "D2":    {"bank": 13, "type": "LN", "io": 18},
    "MCLK2": {"bank": 34, "type": "LP", "io": 11},
    "D4":    {"bank": 34, "type": "LN", "io": 14},
    "D6":    {"bank": 34, "type": "LP", "io": 18},
    "D8":    {"bank": 13, "type": "LN", "io": 14},
    "D10":   {"bank": 13, "type": "",   "io": 0},
    "D12":   {"bank": 13, "type": "LN", "io": 20},
    "D14":   {"bank": 34, "type": "LP", "io": 15},
    "D16":   {"bank": 34, "type": "LN", "io": 12},
    "D18":   {"bank": 34, "type": "LP", "io": 21},
    "D20":   {"bank": 34, "type": "LP", "io": 20},
    "D22":   {"bank": 13, "type": "LN", "io": 13},
    "D24":   {"bank": 13, "type": "LP", "io": 13},
    "D26":   {"bank": 13, "type": "LP", "io": 18},
    "D28":   {"bank": 13, "type": "LN", "io": 16},
    "D30":   {"bank": 34, "type": "LN", "io": 15},
    "D32":   {"bank": 34, "type": "LN", "io": 18},
    "D34":   {"bank": 34, "type": "LP", "io": 24},
    "D36":   {"bank": 34, "type": "",   "io": 0},
    "D38":   {"bank": 34, "type": "LN", "io": 24},
    "D40":   {"bank": 13, "type": "LN", "io": 19},
    "D42":   {"bank": 13, "type": "LP", "io": 19},
    "D44":   {"bank": 13, "type": "LN", "io": 15},
    "D46":   {"bank": 13, "type": "LP", "io": 14},
    "D48":   {"bank": 13, "type": "LP", "io": 20},
    "D50":   {"bank": 13, "type": "LP", "io": 16},
    "D52":   {"bank": 34, "type": "LP", "io": 10},
    "D54":   {"bank": 34, "type": "LN", "io": 20},
    "D56":   {"bank": 34, "type": "LN", "io": 21},
    "D58":   {"bank": 34, "type": "",   "io": 25}
}

mic = 0
center = [110, 100]
radius = 20; #mm

def odd(n):
    return n if n % 2 == 0 else n - 1


print(f"mic,x,y,angle")

for ndx in range(1, 61):
    layer = int( round( math.sqrt( ndx/3.0 ) ))
    firstIdxInLayer = 3*layer*(layer-1) + 1
    side = (ndx - firstIdxInLayer) // layer
    idx  = (ndx - firstIdxInLayer) % layer
    x = radius *  (layer * math.cos( (side - 1) * math.pi/3 ) + (idx + 1) * math.cos( (side + 1) * math.pi/3 ) )
    y = radius * (-layer * math.sin( (side - 1) * math.pi/3 ) - (idx + 1) * math.sin( (side + 1) * math.pi/3 ) )
    rad = math.atan2(y,x)


    
    signal="D"+str(odd(mic))
    if signal in pinout:
        angle = -math.degrees(rad+math.pi/2)
        IO = f"IO_B{pinout[signal]['bank']}_{pinout[signal]['type']}{pinout[signal]['io']}"
        print(f"M{mic},{x:8.5f},{-y:8.5f},{angle:8.5f},{signal},{IO}")    

    mic = mic + 1


