def main(): 
    f = open("input.txt",'r').read().split()
    
    k = [int(line) for line in f]
    print(sumUp(k)) 

def sumUp(f):
    childCount = f.pop(0)
    metaCount = f.pop(0)
    meta = 0

    if childCount == 0:
        for i in range(metaCount):
            meta += f.pop(0)
    else:
        kids = [sumUp(f) for i in range(childCount)]

        for i in range(metaCount):
            m = f.pop(0)
            if m-1 < len(kids): 
                meta += kids[m-1]
    
    return meta

if __name__ == "__main__":
    main()