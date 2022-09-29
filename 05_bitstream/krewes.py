'''
Prattay Dey, Emerson Gelobter
SoftDev
05_bitstream
2022-09-28
time spent:
'''

import random

with open("krewes.txt") as f:
    lines = f.readlines()


def parse():
    student = str(lines).split("@@@")[:-1]
    print(student)
    dict = {}
    for i in student:
        data = []
        data += i.split("$$$")

parse()

# def generateRandomDev():
#
#
#
# keys = list(krewes.keys())
# randIndex = rng.randint(0, len(krewes) - 1)
# randKey = keys[randIndex]
# fullPeriod = krewes[randKey]
# selectedDevo = rng.randint(0, len(fullPeriod)-1)
# return str(randKey) + ": " + fullPeriod[selectedDevo]
# generateRandomDev()
