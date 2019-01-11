import string

def main(): 
    f = open("input.txt",'r').read().split('\n')
    
    string.ascii_uppercase
    xcoords = list(map(getX,f))
    ycoords = list(map(getY,f))
    #print(xcoords)
    #print(ycoords)
    maxX = sorted(xcoords)[-1]
    maxY = sorted(ycoords)[-1]
    grid = [[-1] * maxX for i in range(maxY)]    
    blacklist = set([])
    blacklist.add(-1)
    
    for y in range(maxY):
        for x in range(maxX):
            minDist = 99999
            closestCoord = -1
            equals = False                     
            for i in range(len(xcoords)):
                dist = getDistance(xcoords[i], ycoords[i], x, y)            
                if dist < minDist:
                    equals = False
                    minDist = dist
                    closestCoord = i
                elif dist == minDist:
                    equals = True

            if equals: closestCoord = -1

            if closestCoord != -1 and (y == 0 or y == maxY-1 or x == 0 or x == maxX-1):
                blacklist.add(closestCoord)
            grid[y][x] = closestCoord
    
    richard = {}

    for x in range(maxX):
        for y in range(maxY):
            if grid[y][x] not in blacklist:
                if grid[y][x] not in richard.keys():
                    richard[grid[y][x]]= 1
                else:
                    richard[grid[y][x]] += 1    

    print(sorted(richard.values())[-1]) #fuck you   
    #print(richard)
    #print(maxX)
    #print(maxY)

def getX(item):
    return int(item[:item.find(',')])    

def getY(item):
    return int(item[item.find(' '):])   

def getDistance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

if __name__ == "__main__":
    main()