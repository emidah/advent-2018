def main():
    text = open('input.txt','r').read().split()

    first = ""
    second = ""
    breaker = False

    for i in range(len(text)):
        for j in range(i+1, len(text)):
            counter = 0
            for k in range(len(text[0])):
                if(text[i][k] != text[j][k]):
                    counter += 1
            if(counter == 1):
                first = text[i] 
                second = text[j] 
                breaker = True
                break
        if(breaker):
            break

    print(first + " " + second)

if __name__ == "__main__":
    main()