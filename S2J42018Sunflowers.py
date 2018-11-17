import sys

#Reading lines from file
def column(matrix, i):
    return [row[i] for row in matrix]
#with open("S2J42018CCCTestData.txt") as file:
    #lines = file.readlines()
    
#print(lines)
lines = ['3\n', '3 7 9\n', '2 5 6\n', '1 3 4']
sunflowers = int(lines[0])
lines.pop(0)
sunflowerslist = [[] for i in range(0, sunflowers)]
sunflowerscolumn = []
for i in range(0, sunflowers):
    strdata = str.split(lines[i])
    sunflowerslist[i] = list(map(int, strdata))
sunflowerrow = sunflowerslist[0]
sunflowercolumn = column(sunflowerslist, 0)
if sunflowerrow == sorted(sunflowerrow) and sunflowercolumn == sorted(sunflowercolumn):
    print(sunflowerslist)
else:
    sunflowerslist90 = list(zip(*sunflowerslist[::-1]))
    sunflowerrow = list(sunflowerslist90[0])
    sunflowercolumn = column(sunflowerslist90, 0)
    if sunflowerrow == sorted(sunflowerrow) and sunflowercolumn == sorted(sunflowercolumn):
        print(sunflowerslist90)
    else:
        sunflowerslist180 = list(zip(*sunflowerslist90[::-1]))
        sunflowerrow = list(sunflowerslist180[0])
        sunflowercolumn = column(sunflowerslist180, 0)
        if sunflowerrow == sorted(sunflowerrow) and sunflowercolumn == sorted(sunflowercolumn):
            print(sunflowerslist180)
        else:
            sunflowerslist270 = list(zip(*sunflowerslist180[::-1]))
            print(sunflowerslist270)
            
