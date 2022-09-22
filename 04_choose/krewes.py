'''
DISCO:
- You can have multiple key-value pairs for an index
- You can access a specific value by entering its key after the index
-
QCC:

OPS SUMMARY:
- We're thinking of importing the random python library for our RNG
- We're thinking of using randint(a,b) twice.
    - The first time we'll use it to find a random key
    - The 2nd time we'll find a random value within that key
'''
import random

krewes = {2:["a","b","c"], 7:["d","e","f"], 8:["g","h","i"]}

def krewes(devdict):
    return devdict[0]

print(krewes[0])

# print(krewes(krewes))