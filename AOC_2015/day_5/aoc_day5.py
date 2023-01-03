import re


def no_of_vowels(sentence):
    vowels = 0
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels = vowels + 1
    return vowels

def duplicate_check(sentence):
    for s in range(len(sentence)-1):
        if sentence[s] == sentence[s + 1]:
            return True

        

def is_nice(sentence):
    three_vowels = False
    two_dupes = False
    no_strings = True
    

    if(no_of_vowels(sentence) >= 3):
        three_vowels = True
    
    if (sentence.find("ab") != -1 or sentence.find("cd") != -1 or sentence.find("pq") != -1 or sentence.find("xy") != -1):
        no_strings = False
    
    if(duplicate_check(sentence) == True):
        two_dupes = True
    
    
    
    if three_vowels == True and two_dupes == True and no_strings == True:
        return True
    else:
        return False




print(is_nice("aeiaaeed"))

f = open("C:/Users/samue/Documents/Projects/AOC_2015/day_5/input.txt")

x = f.readlines()


count = 0
for line in x:
    
    if (is_nice(line)):
        count = count + 1

print(count)

