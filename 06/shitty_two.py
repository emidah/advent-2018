
def main(): 
    f = open("input.txt",'r').read().split('\n')
    
    xcoords = list(map(getX,f))
    ycoords = list(map(getY,f))
    #print(xcoords)
    #print(ycoords)
    maxX = max(xcoords)
    maxY = max(ycoords)
    grid = [[-1] * maxX for i in range(maxY)]

    dougScore = 0
    
    for y in range(maxY):
        for x in range(maxX):
            dist = 0        
            for i in range(len(xcoords)):
                dist += getDistance(xcoords[i], ycoords[i], x, y)            
                
            if(dist < 10000):
                dougScore += 1
    
    print(dougScore)
    


def getX(item):
    return int(item[:item.find(',')])    

def getY(item):
    return int(item[item.find(' '):])   

def getDistance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

if __name__ == "__main__":
    main()