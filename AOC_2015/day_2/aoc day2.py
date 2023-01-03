f = open("C:/Users/samue/Documents/Projects/AOC_2015/day_2/input.txt")
sqft = 0
ribbon = 0
for x in f:
    numbers = x.split("x")
    
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
        
    #part 1 only #sqft = sqft + (2 * numbers[0] * numbers[1]) + (2 * numbers[1] * numbers[2]) + ( 2 * numbers[0] * numbers[2])

    numbers.sort()
    
    ribbon = ribbon + (numbers[0] * 2) + (numbers[1] * 2) + (numbers[0] * numbers[1] * numbers[2]) 
    
    #part 1 only #sqft = sqft + int(numbers[0] * numbers[1])

    print(ribbon)
    
f.close()
