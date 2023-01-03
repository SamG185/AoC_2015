import re

def double_double(sentence):
    match1 = re.search(r'(\w\w)(.){0,16}\1', sentence)
    
    if (match1):
        return True
    else:
        return False
    


def single_repeater(sentence):
    aMatch = re.search(r'(\w)\w\1', sentence)
    return aMatch


def is_nice(sentence):

    return double_double(sentence) and single_repeater(sentence)



f = open("C:/Users/samue/Documents/Projects/AOC_2015/day_5/input.txt")

x = f.readlines()


count = 0
for line in x:
    print(is_nice(line))
    if (is_nice(line)):
        count = count + 1

print(count)

