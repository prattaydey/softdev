'''
Prattay Dey, Emerson Gelobter
SoftDev
06_py-csv
2022-09-29
time spent: _______

DISCO:

QCC:

HOW THIS SCRIPT WORKS:

'''

import csv

with open("occupations.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Job Class"], row["Percentage"])
