#Reading lines from file
lines = []
with open("S12018CCCTestData.txt") as file:
    for line in file: 
        line = line.strip()
        lines.append(line)
        
#Converting into integer list instead of string
intlist = list(map(int, lines))

#Removing first number because it's irrelevant
intlist.pop(0)

#Sort and finding differences
intlist.sort(key=int)
differences = [intlist[i+1]-intlist[i] for i in range(len(intlist)-1)]
differences[:] = [x / 2 for x in differences]
differences.append(0)
differences.insert(0, 0)

#Dividing differences by 2
territory = [(x + y) for (x, y) in zip(differences[:-1], differences[1:])]

#Remove the ends, as they are infinite
territory.pop(0)
territory.pop(len(territory)-1)

#Finding distance
lowestdistance = min(float(s) for s in territory)
print(lowestdistance)
