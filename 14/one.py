recipeCount = 637061 #637061
recipes = [3,7]
current1 = 0
current2 = 1

while len(recipes) < recipeCount+10:
    #print(recipes)
    #print(recipes[current1])
    #print(recipes[current2])
    #print("")
    if recipes[current1] + recipes[current2] < 10:
        recipes.append(recipes[current1] + recipes[current2])
    else:
        recipes.append(1)
        recipes.append((recipes[current1] + recipes[current2]) % 10)
    
    current1 = (current1 + 1 + recipes[current1]) % len(recipes)
    current2 = (current2 + 1 + recipes[current2]) % len(recipes)
    
outst = ""
for value in recipes[recipeCount:recipeCount+10]:
    outst = outst + str(value)
print(outst)