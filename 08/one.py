def main(): 
    f = open("input.txt",'r').read().split()
    
    k = [int(line) for line in f]
    print(sumUp(k)) 

def sumUp(f):
    childCount = f.pop(0)
    metaCount = f.pop(0)
    meta = 0
    for i in range(childCount):
        meta += sumUp(f)
    
    for i in range(metaCount):
        meta += f.pop(0)
    return meta

if __name__ == "__main__":
    main()