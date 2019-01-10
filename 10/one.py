import time

text = open('input.txt','r').read().split('\n')

coords = []

for line in text:
    x = int( line[10:16].strip() )
    y = int( line[18:24].strip() )
    xspd = int( line[36:38].strip() )
    yspd = int( line[40:42].strip() )
    coords.append( [x,y,xspd,yspd] )

while abs(coords[0][0]-coords[1][0]) > 20:
    for coord in coords:
        coord[0] += coord[2]
        coord[1] += coord[3]

maxX = 50
maxY = 50

while True:
    grid = [[' '] * (2*maxY) for i in range(2*maxX)]
    for coord in coords:
        coord[0] += coord[2]
        coord[1] += coord[3]
        if(abs(coord[0]) < len(grid)/2 and abs(coord[1]) < len(grid))/2:
            grid[coord[0]][coord[1]] = '#'
    
    print("------------------------------------")
    for line in grid:
        ts = ":"
        for char in line:
            ts = ts + char
        print(ts)

    time.sleep(1)

print("done")
print(maxX)
print(maxY)