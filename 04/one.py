log = open('input.txt','r').readlines()
log.sort()
guards = { }

guardString = ""
fellAsleepAt = 0
minute = 0

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
        timeAsleep = int(line[line.find(':')+1 : line.find(']')]) - fellAsleepAt
        guards[guardString] += timeAsleep
        #print(guardString + " woke up after " + str(timeAsleep) + " for a total of " + str(guards[guardString]))

biggest = 0
for guard in guards.keys():
    if(guards[guard] > biggest):
        biggest = guards[guard]
        guardString = guard

print("Total time asleep: " + str(biggest))
print("Guard number: " + guardString)
print("Finding out best minute...")

foundGuard = False
mins = {}
for line in log:
    if '#' in line:
        fellAsleepAt = 0
        foundGuard = ('#'+guardString) in line
    elif foundGuard:
        if 'falls asleep' in line:
            fellAsleepAt = int(line[line.find(':')+1 : line.find(']')])
        elif 'wakes up' in line:
            wokeUpAt = int(line[line.find(':')+1 : line.find(']')])
            for i in range(fellAsleepAt, wokeUpAt):
                if i in mins.keys(): mins[i] += 1
                else: mins[i] = 1

best = 0      
for min in mins.keys():
    if mins[min] > best:
        minute = min
        best = mins[min]

print("Best minute is " + str(minute))
result = int(guardString)*minute
print("Answer: " + str(result))