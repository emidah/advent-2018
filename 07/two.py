def main():
    text = open('input.txt','r').read().split('\n')
    
    letterDict = {} 
    workerCount = 5
    stepOffset = 60 #60

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

    #print(letterDict)

    
    processed = [] # List of processed letters
    keynum = len(letterDict.keys()) # Length of key list
    workers = [Worker() for i in range(workerCount)] # Init workers
    currentStep = 0 # Set simulation at 0

    while len(processed) < keynum:
        # Get the letters with no remaining dependencies
        nexts = getNext(letterDict)
        nexts.sort() # Alphabetical order
        nexts.reverse()

        # Check for finishing workers
        for worker in workers:
            if worker.finishesOn == currentStep: # Is worker set to finish on this step?
                
                processed.append(worker.workingOn) # This letter has been processed

                for s in letterDict.values(): # Remove this letter from the dictionary values (dependencies)
                    s.discard(worker.workingOn) 
                
                # Reload nexts
                nexts = getNext(letterDict) 
                nexts.sort() # Alphabetical order
                nexts.reverse()
                
                worker.workingOn = ' ' # Remove letter fromw worker

        # Add new letters to workers
        for worker in workers:
            if len(nexts) > 0 and worker.workingOn == ' ': # If worker is free and there are available nodes
                newLet = nexts.pop() # Remove this letter from the nexts
                letterDict.pop(newLet) # Remove this letter from the dictionary keys
                worker.workingOn = newLet
                worker.finishesOn = currentStep + stepOffset + 1 + ord(newLet) - ord('A')
            
        
        print(str(currentStep) + "::" + workers[0].workingOn + ":" + workers[1].workingOn + ":" + workers[2].workingOn + ":" + workers[3].workingOn + ":" + workers[4].workingOn)
        currentStep += 1

    # Print solution

    endstr = ""
    for letter in processed:
        endstr = endstr + letter
    
    print(endstr)
            
            

class Worker:
    workingOn = ' '
    finishesOn = -1



def getNext(ld: dict):
    nexts = [ ]
    for letter in ld:
        if len(ld[letter]) == 0:
            nexts.append(letter)
    return nexts


if __name__ == "__main__":
    main()