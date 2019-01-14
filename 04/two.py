log = open('input.txt','r').readlines()
log.sort()
guards = { }

guardString = ""
fellAsleepAt = 0
minute = 0

minlist = [ [] for i in range(60)]

# Log all activity per minute in minlist
for line in log:
    if '#' in line: 
        fellAsleepAt = 0
        guardString = line[line.find('#')+1:]
        guardString = guardString[:guardString.find(' ')]
        if guardString not in guards.keys(): guards[guardString] = 0
    elif 'falls asleep' in line:
        fellAsleepAt = int(line[line.find(':')+1 : line.find(']')])
        #print(guardString + " fell asleep at " + str(fellAsleepAt))
    elif 'wakes up' in line:
        wokeAt = int(line[line.find(':')+1 : line.find(']')])
        for i in range(fellAsleepAt,wokeAt):
            minlist[i].append(guardString)
        timeAsleep =  wokeAt - fellAsleepAt
        guards[guardString] += timeAsleep
        #print(guardString + " woke up after " + str(timeAsleep) + " for a total of " + str(guards[guardString]))


# Find count of best quard from best minute
mincounts = []
minguards = []

for minute in minlist:
    mostSleeping = ""
    count = 0

    for value in set(minute):
        newcount = minute.count(value)
        if newcount > count:
            count = newcount
            mostSleeping = value
    #print("Min " + str(minlist.index(minute)) + ", guard #" + mostSleeping + ", count " + str(count) )
    mincounts.append(count)
    minguards.append(mostSleeping)

bestmin = mincounts.index( max(mincounts) )
result = bestmin * int(minguards[bestmin])

print("Final answer: in " + str(bestmin) + ", guard #" + minguards[bestmin] + ", result " + str(result) )
    
