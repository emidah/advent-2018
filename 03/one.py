def main():

    tally = 0
    numfile = open('input.txt','r')
    squareset = set([])     #set of squares already selected
    selectedset = set([])   #set of squares set of squares selected twice

    for line in numfile:                # initial format: #1 @ 393,863: 11x29

        # data extraction
        edited = line.split('@')[1]
        editedfurther = edited.split(':')
        
        xcoord = int(editedfurther[0].split(',')[0].strip()) #393
        ycoord = int(editedfurther[0].split(',')[1].strip()) #863
        xsize = int(editedfurther[1].split('x')[0].strip())  #11
        ysize = int(editedfurther[1].split('x')[1].strip())  #29

        for x in range(xsize):
            for y in range(ysize):
                finalX = xcoord+x
                finalY = ycoord+y
                formattedString = str(finalX) + "," + str(finalY) # key used in set

                if formattedString not in squareset:
                    squareset.add(formattedString)
                elif formattedString not in selectedset:
                    tally += 1
                    selectedset.add(formattedString)

    print(tally)

if __name__ == "__main__":
    main()