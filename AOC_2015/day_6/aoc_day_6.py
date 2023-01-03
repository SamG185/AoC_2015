f = open("C:/Users/samue/Documents/Projects/AOC_2015/day_6/input.txt")

input = f.readlines()


gridDict = {}



for x in range(0,1000):
    for y in range(0,1000):
        gridDict.update({(x, y): False})





for line in input:
    splitInstructions = line.split()
    firstInstruction = splitInstructions[0]

    if(firstInstruction == "turn"):
        modifier = splitInstructions[1]

        #get start coordinates for grid range
        startCoords = splitInstructions[2]
        splitStartCoords = startCoords.split(",")
        startX = int(splitStartCoords[0])
        startY = int(splitStartCoords[1])
        
        #get end coordinates for grid range
        endCoords = splitInstructions[4]
        splitEndCoords = endCoords.split(",")
        endX = int(splitEndCoords[0])
        endY = int(splitEndCoords[1])

        #get real input for modifier
        if(modifier == "on"):
            lightState = True
        else:
            lightState = False
        count = 0

        for x in range(startX, endX+1):
            for y in range(startY, endY+1):
                gridDict.update({(x,y): lightState})        


    else:
        startCoords = splitInstructions[1]
        splitStartCoords = startCoords.split(",")
        startX = int(splitStartCoords[0])
        startY = int(splitStartCoords[1])
        
        #get end coordinates for grid range
        endCoords = splitInstructions[3]
        splitEndCoords = endCoords.split(",")
        endX = int(splitEndCoords[0])
        endY = int(splitEndCoords[1])
        

        for x in range(startX, endX+1):
            for y in range(startY, endY+1):
                gridDict.update({(x,y): not gridDict.get((x, y))})


lightCount = 0
for light in gridDict.values():
    if light == True:
        lightCount += 1
        
print(lightCount)
    