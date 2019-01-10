inputs = int(9221)

def main():
    length = 300 #300x300 grid 

    #print(getPower(100,152))

    coordRange = [[0]*length for i in range(length)] #initialize grid

    #populate grid
    for x in range(length):
        for y in range(length):
            coordRange[x][y] = getPower(x,y)
            #print(str(x) + str(y))
        
    for row in coordRange:
        print(row)
    #Find 3x3
    maxPower = -45
    maxX = -1
    maxY = -1

    #Go through every coordinate
    for x in range(length-2):
        for y in range(length-2):
            summ = 0

            #For each coordinate, go through 3x3
 
            for a in range(3):
                for b in range(3):
                    summ += coordRange[x+a][y+b]
                    
                    #print(coordRange[x+a][y+b])
                    #print(str(x+a) + " " + str(y+b))

            #print('_')
            if summ > maxPower:
                print(summ)
                maxPower = summ
                maxX = x+1
                maxY = y+1
    
    print("Max X: " + str(maxX) + ", max Y: " + str(maxY) + ", power " + str(maxPower))

def getPower(x,y):
    rackID = x+1 + 10
    powStart = rackID * (y+1) + inputs
    powStart = powStart * rackID

    if powStart > 99:
        return int(str(powStart)[-3]) - 5
    else:
        return -5


if __name__ == "__main__":
    main()