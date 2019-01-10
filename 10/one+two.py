import time
import numpy as np

text = open('input.txt','r').read().split('\n')

coords = []

# Create initial state: Each dot is a list with 4 values: x, y, x speed and y speed
for line in text:
    x = int( line[18:24].strip() )
    y = int( line[10:16].strip() )
    xspd = int( line[40:42].strip() )
    yspd = int( line[36:38].strip() )
    coords.append( [x,y,xspd,yspd] )


breaker = False
counter = 0
lastVar = 9999999999999

#Fast forward until dots reach the minima of variance
while not breaker:
    for coord in coords:
        coord[0] += coord[2]
        coord[1] += coord[3]
    
    #Check X variance
    var = np.var([coord[0] for coord in coords])

    if var > lastVar:
        
        #undo last step
        for coord in coords:
            coord[0] -= coord[2]
            coord[1] -= coord[3]
        break

    lastVar = var
    counter += 1

print("It took " + str(counter) + " simulation \"seconds\" for us to get here") 

#Which one is X and which one is Y is a little confusing at this point, but this is the window size:

maxX = 20
maxY = 100

# Move the window center to the average point
xbias = int(np.average([coord[0] for coord in coords]))
ybias = int(np.average([coord[1] for coord in coords]))

# Init grid for drawing
grid = [[' '] * (maxY) for i in range(maxX)]

for coord in coords:

    # If dot is inside window bounds, draw dot in grid
    if(coord[0] < xbias + maxX//2 and coord[0] > xbias - maxX//2 and coord[1] < ybias + maxY//2 and coord[1] > ybias - maxY//2): 
        grid[coord[0]-xbias+maxX//2][coord[1]-ybias+maxY//2] = '#'

# Draw the grid.
for line in grid:
    ts = ":"
    for char in line:
        ts = ts + char
    ts = ts + ":"
    print(ts)
