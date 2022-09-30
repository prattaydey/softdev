'''
Prattay Dey, Emerson Gelobter
SoftDev
05_bitstream
2022-09-28
time spent: 1.0 hr

DISCO:
- We can open and read a txt file in python using open('filename', mode)
- mode options are r (read), a (append), w (write), x (create)
- read() converts the contents of the txt file into one long string, readlines() converts each line into individual lists

QCC:
- Is there a way to complete this using only one dictionary?
  Since there are 3 distinct values (name, pd, ducky) would it be possible to have a key within a key that points to a value?

OPS SUMMARY:
- Process the text file into one large string
- Split each individual devo by split(@@@)
- Split each devo's info with split($$$)

- Use 2 different dictionaries
  1st (name -> period)
  2nd (name -> ducky)

- Select a random devo using one of the methods from HW04
- Print devo name,
  then access the name's value in the 1st dict to print their period
  finally access the name's value in 2nd dict to print their ducky
'''

import random

# Opens and reads text file
with open('krewes.txt', 'r') as f:
    krewes = f.read()

# Get a random key from a dictionary
def getRandKey(dic):
    keys = list(dic.keys())
    keyIndex = random.randint(0, len(keys)-1)
    return keys[keyIndex]

def getDevo():
  list = krewes.split("@@@") #Makes list with each devos info
  name_pd = {} #makes dictionary with name as key and period as value
  name_ducky = {} #makes dictionary with name as key and ducky as value

  for i in list: #Splits each devos info
      m = i.split("$$$")
      name_pd[m[1]] = m[0] #Adds name and pd
      name_ducky[m[1]] = m[2] #Adds name and ducky


  p = getRandKey(name_ducky) # Gets name of random devo

  print("name:", p,"period:", name_pd[p],"ducky:", name_ducky[p]) #prints devo and their values


getDevo()
