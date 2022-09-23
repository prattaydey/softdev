'''
Jing Feng, Anna Fang, Prattay Dey
SoftDev
04_choose
2022-09-22
time spent: 
DISCO:
- You can have multiple key-value pairs for an index
- You can access a specific value by entering its index after the key 
- Using randint will return integers while simply using random will return floats 
QCC:
OPS SUMMARY:
- We're thinking of importing the random python library for our RNG
- We're thinking of using randint(a,b) twice. 
    - The first time we'll use it to find a random key
    - The 2nd time we'll find a random value within that key
- We will have two methods
    - The first method will use random to generate the class (2/7/8) that the random dev will be selected from
    - The next will use random to provide the index of a randomly selected dev inside of the selected class
'''

import random as rng

krewes = {2:["a","b","c"], 7:["d","e","f"], 8:["g","h","i"]}

# first, use random to randomly choose the class the random devo will be chosen from 
def generateRandomClass():
    selected = rng.randint(1,3)
    randClass = 0
    if selected == 1:
        randClass = 2
    elif selected == 2:
        randClass = 7
    else:
        randClass = 8 
    return randClass

# using the genenerated class, find the length of that list and randomly select from it. Then, return the chosen devo! 
def generateRandomDev():
    selectedClass = generateRandomClass()
    fullClass = krewes[selectedClass]
    selectedDevo = rng.randint(0, len(fullClass)-1)
    #print(selectedClass)
    #print(selectedDevo) 
    return fullClass[selectedDevo] 
    
print(generateRandomDev())
 
