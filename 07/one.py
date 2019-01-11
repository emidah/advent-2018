letterDict = {}

def main():
    text = open('input.txt','r').read().split('\n')
    
    for line in text:
        lkey = line[5]
        ldepend = line[36]

        if lkey not in letterDict.keys():
            letterDict[lkey] = set([ldepend])
        else:
            letterDict[lkey].add(ldepend)
        if ldepend not in letterDict.keys():
            letterDict[ldepend] = set([])
    
    resolved = set([])
    
    for key in letterDict:
        resolveDependencies(letterDict, resolved, key)

    print(letterDict)

    letterlist = letterDict.keys()
    
    for i in range(100):
        letterlist = sorted(letterlist, key=cmp_to_key(compare))

        mystr = ''
        for sym in letterlist:
            mystr += sym

        print(mystr)


def compare(item1, item2):
    if item2 in letterDict[item1]:
        return -1
    elif item1 in letterDict[item2]:
        return 1
    elif ord(item1) < ord(item2):
        return -1
    else: 
        return 1
    

def resolveDependencies(letdic, resolved, ogkey):
    if(ogkey not in resolved):
        for letter in letdic[ogkey]:
            resolveDependencies(letdic, resolved, letter)
            letdic[ogkey] = letdic[ogkey].union(letdic[letter])
        resolved.add(ogkey)

def cmp_to_key(mycmp):
    'Convert a cmp= function into a key= function'
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K
        
        

if __name__ == "__main__":
    main()