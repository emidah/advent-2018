def main():
    text = open('input.txt','r').read().split('\n')
    
    letterDict = {}

    # Parse dictionary that tells the dependencies of each letter
    
    for line in text:
        lkey = line[36]
        ldepend = line[5]

        if lkey not in letterDict.keys():
            letterDict[lkey] = set([ldepend])
        else:
            letterDict[lkey].add(ldepend)
        if ldepend not in letterDict.keys():
            letterDict[ldepend] = set([ ])

    print(letterDict)

    processed = []
    keynum = len(letterDict.keys())

    while len(processed) < keynum:
        # Get the letters with no remaining dependencies
        nexts = getNext(letterDict)
        nexts.sort() # Alphabetical order
        nextOne = nexts[0] 

        print(nextOne)
        processed.append(nextOne) # This letter has been processed 
        letterDict.pop(nextOne) # Remove this letter from the dictionary keys
        for s in letterDict.values(): # Remove this letter from the dictionary values (dependencies)
            s.discard(nextOne) 

    # Print solution

    endstr = ""
    for letter in processed:
        endstr = endstr + letter
    
    print(endstr)
            
            




def getNext(ld: dict):
    nexts = [ ]
    for letter in ld:
        if len(ld[letter]) == 0:
            nexts.append(letter)
    return nexts


if __name__ == "__main__":
    main()