import copy

#SAME AS ONE.PY, BUT PRINTS THE DIFF OF EACH STEP.

text = open('input.txt','r').read().split('\n')

rules = text[2:]

state = text[0][15:]

offset = 0
lastTotal = 0

for i in range(1000):

    if state[:5].find('#') != -1:
        offset += 5
        state = 5*'.' + state
    if state[-6:].find('#') != -1:
        state = state + 5*'.'

    if(i % 100 == 0):
        indices = [i for i in range(len(state)) if state.startswith('#', i)]
        indices = [index-offset for index in indices]

        total = 0
        for index in indices:
            total += index

        print( "Diff to last: " + str(total-lastTotal))
        lastTotal = total
    newState = len(state) * '.'

    for rule in rules:
        indices = [i for i in range(len(state)) if state.startswith(rule[0:5], i)]
        #print("rule: " + rule[0:5] + ", matches " + str(indices))
        
        for index in indices:
            if rule[9] == '#' :
                newState = newState[:index+2] + '#' + newState[index+3:]
            #else:
                #newState = newState[:index+2] + '.' + newState[index+3:]
    state = newState
    
    

print("Use the repeating value to figure out the answer mathematically: the result grows in a linear fashion")