'''
Prattay Dey, Emerson Gelobter
SoftDev
06_py-csv
2022-09-29
time spent: _______

DISCO:
- When reading csv files, we can use DictReader() instead of reader(). This function is like a regular reader but also maps each row to a key-value pair.
  (https://docs.python.org/3/library/csv.html)
-
QCC:

HOW THIS SCRIPT WORKS:

'''

import csv
import random

with open("occupations.csv", "r") as file:
    reader = csv.DictReader(file)
    
    
    list_dict = []
    for row in reader:
        list_dict.append(row) 
        #print(row["Job Class"], row["Percentage"])
    
def pickOne(list1):
    x = 100.0
    for i in list1:
        if (random.uniform(0.0, x) < float(i["Percentage"])):
            return i["Job Class"]
        else:
            x -= float(i["Percentage"])
    
print(pickOne(list_dict))