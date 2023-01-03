floor = 0
charnumber = 0
f = open("C:/Users/samue/Documents/Projects/input.txt")

for x in f.read():
    charnumber = charnumber + 1
    if x == "(":
        floor = floor + 1
    elif x == ")":
        floor = floor - 1
    if floor == -1:
        print(charnumber)
        break

print(floor)
f.close()


