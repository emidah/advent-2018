def main():
    numfile = open('input.txt','r')
    
    twolet = 0
    threelet = 0
    
    for line in numfile:
        for letter in line:
            if line.count(letter) == 2:
                print("double " + letter + " in " + line)
                twolet += 1
                break
            
        for letter in line:
            if line.count(letter) == 3:
                print("triple " + letter + " in " + line)
                threelet += 1 
                break
    print("tally: " + str(twolet) + " doubles and " + str(threelet) + " triples")
    print("result: " + str(twolet*threelet))

if __name__ == "__main__":
    main()