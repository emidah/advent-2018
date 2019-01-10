import numpy as np

inputs = int(9221)

def main():

    # partial rewrite of one.py... 

    length = 300 # 300x300 grid 

    #print(getPower(100,152))

    coordRange = np.array([[0]*length for i in range(length)]) #initialize grid

    # populate grid
    for x in range(length):
        for y in range(length):
            coordRange[x][y] = getPower(x,y)
            #print(str(x) + str(y))
        
    #for row in coordRange:
        #print(row)

    maxPower = -45
    maxX = -1
    maxY = -1
    size = 3

    # THIS IS A PARALLELIZABLE PROBLEM. I DID NO SUCH EFFORT HERE.

    counter = 0

    #Go through every size, small to big
    for z in range(3,300):

        if(counter == 5): break #If we've gone through 5 new sizes with no improvement, we're probably done.
        
        for x in range(length-(z-1)):
            for y in range(length-(z-1)):

                #For each egligible coordinate, go through z x z 

                summ = sum( coordRange[x+a][y+b] for b in range(z) for a in range(z) )
                    
                if summ > maxPower:
                    counter = 0 # A record was found in this size

                    maxPower = summ
                    maxX = x+1
                    maxY = y+1
                    size = z
                    
                    print("Max X: " + str(maxX) + ", max Y: " + str(maxY) + ", power " + str(maxPower) + ", size " + str(size))
                    
        counter += 1   

    print("END")

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