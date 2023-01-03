f = open("C:/Users/samue/Documents/Projects/AOC_2015/day_3/input.txt")

santaX = 0
santaY = 0
santa_position = [santaX, santaY]

robotX = 0
robotY = 0
robot_position = [robotX, robotY]

directions = f.read()

list_of_positions = []
counter = 0
for i in directions:
    
    #santas instruction
    if(counter % 2 == 0):
        match i:
            case '<':
                santa_position[1] -= 1
            
            case '^':
                santa_position[0] += 1
            
            case 'v':
                santa_position[0] -= 1
            
            case '>':
                santa_position[1] += 1
        
        if(tuple(santa_position) not in list_of_positions):
            list_of_positions.append(tuple(santa_position))

    #robot instruction
    if(counter % 2 == 1):
        match i:
            case '<':
                robot_position[1] -= 1
            
            case '^':
                robot_position[0] += 1
            
            case 'v':
                robot_position[0] -= 1
            
            case '>':
                robot_position[1] += 1
        
        if(tuple(robot_position) not in list_of_positions):
            list_of_positions.append(tuple(robot_position))
    counter += 1
    


        
print(len(list_of_positions))   
    

f.close()