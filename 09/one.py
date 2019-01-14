import time
start = time.time()

st = open("input.txt", 'r').read()
players = int( st[:st.find(' ')] )
lastMarble = int( st[34:( st[34:].find(' ') + 34)] )

print('players: ' + str(players) + ', last marble worth ' + str(lastMarble))

marblelist = [ 0 ]
scores = [0] * players

currentIndex = 0
currentValue = 0
breaker = False
while not breaker:
    for i in range(players):
        currentValue += 1
        
        if currentValue % 23 != 0:
            insertPoint = (currentIndex + 2) % len( marblelist )
            
            if insertPoint == 0:
                marblelist.append(currentValue)
                currentIndex = len(marblelist)-1
            else:
                marblelist.insert(insertPoint, currentValue)
                currentIndex = insertPoint

        else:
            scores[i] += currentValue
            if currentIndex - 7 < 0:
                currentIndex = len(marblelist) + (currentIndex - 7)
            else: 
                currentIndex -= 7

            #if len(marblelist)/2 > currentIndex:
            #    marblelist.reverse()
            #    scores[i] += marblelist.pop(len(marblelist)-1 - currentIndex)
            #    marblelist.reverse()
            
            #else: 
            scores[i] += marblelist.pop(currentIndex)
        
        
        #print( marblelist )
        
        if currentValue >= lastMarble:
            breaker = True
            break

print(max(scores))

end = time.time()
print(end - start)