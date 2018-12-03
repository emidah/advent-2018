def main():
    numfile = open('input.txt','r')
    total = 0
    
    for line in numfile:
        total += int(line) # Do or do not. There is no 'try'.

    print(total)

if __name__ == "__main__":
    main()