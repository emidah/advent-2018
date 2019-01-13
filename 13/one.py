import numpy as np

cartSyms = set([ '^', 'v', '<', '>' ])

text = open('input.txt','r').read().split('\n')

grid = [[i for i in j] for j in text]

carts = []

# Get all carts' data and remove them from the grid
# Assumes no cart is at an intersection or corner
for y in range(len(grid)):
    for x in range(len(grid[0])):
        #print(str(x) + " " + str(y))
        if grid[y][x] == '^' or grid[y][x] == 'v':
            # save data
            l = [grid[y][x], y, x]
            carts.append(l)
            # remove from grid
            grid[y][x] = '|'

        elif grid[y][x] == '<' or grid[y][x] == '>':
            # save data
            l = [grid[y][x], y, x]
            carts.append(l)
            # remove from grid
            grid[y][x] = '-'
    
# Simulation
collision = False
count = 0

while not collision:
    count += 1
    for cart in carts:
        print("in: " + cart[0] + " at " + str(cart[1]) + "," + str(cart[2]))

        if cart[0] == '>':
            
            cart[2] += 1

            if grid[cart[1]][cart[2]] == "/":
                cart[0] = '^'

            elif grid[cart[1]][cart[2]] == "\\":
                cart[0] = 'v'

        
        elif cart[0] == '<':
            
            cart[2] -= 1
        
            if grid[cart[1]][cart[2]] == '/':
                print("wew")
                cart[0] = 'v'

            elif grid[cart[1]][cart[2]] == "\\":
                cart[0] = '^'

            

        elif cart[0] == '^':

            cart[1] -= 1

            if grid[cart[1]][cart[2]] == "/":
                cart[0] == '>'

            elif grid[cart[1]][cart[2]] == "\\":
                cart[0] == '<'

            
        
        elif cart[0] == 'v':

            cart[1] += 1

            if grid[cart[1]][cart[2]] == '/':
                cart[0] = '<'

            elif grid[cart[1]][cart[2]] == "\\":
                cart[0] = '>'

        else: 
            print("Something went terribly wrong")

        print("out: " + cart[0] + " at " + str(cart[1]) + "," + str(cart[2]))
    if count == 2:
        collision = True
    print("---------")




            
