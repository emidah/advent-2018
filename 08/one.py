def main(): 
    f = open("input.txt",'r').read().split()
    for line in f:
        line = int(line)

    sumUp(f)

def sumUp(f):
    childCount = f[0]
    metaCount = f[1]
    if(childCount > 0):
        sumUp(f[2:])
    

if __name__ == "__main__":
    main()