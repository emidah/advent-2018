# This solution is slow because it uses all that string crap
# But it works, so...

inputs = "637061"
recipes = "37"
current1 = 0
current2 = 1

while True:
    
    # Add the stuff to the string as described in the assignment

    if int(recipes[current1]) + int(recipes[current2]) < 10:
        recipes = recipes + str( int(recipes[current1]) + int(recipes[current2]) )
    else:
        recipes = recipes + "1"
        recipes = recipes + str( (int(recipes[current1]) + int(recipes[current2])) % 10)
    
    current1 = (current1 + 1 + int(recipes[current1])) % len(recipes)
    current2 = (current2 + 1 + int(recipes[current2])) % len(recipes)

    #print(recipes)

    # Only check the last 2x len(inputs) for matches

    if len(recipes) % (len(inputs)) == 0:
        if recipes[-2*len(inputs):].find(inputs) != -1:
            print(recipes.find(inputs))
            break
