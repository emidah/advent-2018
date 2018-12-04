def main():
    total = 0
    freqs = set([0]) # use a set so that it does't take all year
    match = False
    numfile = open('input.txt','r')

    filetext = numfile.read().split() # Eliminate I/O (if it doesn't automatically)

    while(not match):
        for line in filetext:
            total += int(line) # Do or do not. There is no 'try'.
            if total in freqs:
                print("MATCH")
                match = True
                break
            else:
                freqs.add(total)
    print(total)

if __name__ == "__main__":
    main()