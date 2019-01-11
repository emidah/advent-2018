# Go through text one symbol at a time
# Save last symbol
# remove when current and last are reactive
# move index to reaction start, put reaction - 1 to last
# continue
# once done, count symbols

import copy

def main(): 
    st = open("input.txt", 'r').read() 

    for s in set(st.lower()):
        st_temp = st.replace(s,'')
        st_temp = st_temp.replace(s.upper(),'')
        st_temp = process(st_temp)
        print(len(st_temp))

    
def process(st_og):
    st = copy.deepcopy(st_og)
    lastLetter = st[0]
    i = 1
    while i < len(st):
        if lastLetter != st[i] and lastLetter.lower() == st[i].lower():
            st = st[:i-1] + st[i+1:]
            i -= 1
            if i > 0:
                lastLetter = st[i-1]
            else: 
                lastLetter = ''
        else:
            lastLetter = st[i]
            i += 1
    return st



    print(len(st))

if __name__ == "__main__":
    main()