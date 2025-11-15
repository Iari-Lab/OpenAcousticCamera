import pcbnew
from pcbnew import *
import math

base = '../'
file = 'array.kicad_pcb'
pcb_file = base + '/' + file
    
board = pcbnew.LoadBoard(pcb_file)

mic = 0
center = [110, 100]
mic_offset   = [ 0.0,  0.0]
radius = 20; #mm

print(f"mic,x,y,angle")

for ndx in range(1, 61):
    layer = int( round( math.sqrt( ndx/3.0 ) ))
    firstIdxInLayer = 3*layer*(layer-1) + 1
    side = (ndx - firstIdxInLayer) // layer
    idx  = (ndx - firstIdxInLayer) % layer
    x = radius *  (layer * math.cos( (side - 1) * math.pi/3 ) + (idx + 1) * math.cos( (side + 1) * math.pi/3 ) )
    y = radius * (-layer * math.sin( (side - 1) * math.pi/3 ) - (idx + 1) * math.sin( (side + 1) * math.pi/3 ) )
    rad = math.atan2(y,x)

    angle = -math.degrees(rad+math.pi/2)
    print(f"M{mic},{x:8.5f},{-y:8.5f},{angle:8.5f}")
    mic = mic + 1


