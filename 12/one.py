import copy

text = open('input.txt','r').read().split('\n')

rules = text[2:] # Extract rule lines
state = text[0][15:] # Extract initial state

offset = 0 # Index offset

for i in range(20): # For each step...

    # Dynamic string expansion when limits reached
    if state[:4].find('#') != -1:
        offset += 5
        state = 5*'.' + state
    if state[-4:].find('#') != -1:
        state = state + 5*'.'

    newState = len(state) * '.' # init new empty string

    print(state)

    for rule in rules: # Process each rule

        indices = [i for i in range(len(state)) if state.startswith(rule[0:5], i)] # Find all occurences of rule
        #print("rule: " + rule[0:5] + ", matches " + str(indices))
        
        for index in indices: # For each occurence, mark the result in the new state string
            if rule[9] == '#' :
                newState = newState[:index+2] + '#' + newState[index+3:]
            #else: 
                #newState = newState[:index+2] + '.' + newState[index+3:]
    state = newState

indices = [i for i in range(len(state)) if state.startswith('#', i)] # Get all indices of #s
indices = [index-offset for index in indices] # Take into account the index offset caused by expansion
total = 0
for index in indices:
    total += index

print(total)