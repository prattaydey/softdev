'''
Team Whole Lotta Coding: Emerson Gelobter, Aden Garbutt, Prattay Dey
SoftDev
Flask
2022-10-7
time spent:@app.route("/") 
'''
import csv
import random

from flask import Flask

with open("occupations.csv", "r") as file:
    reader = csv.DictReader(file)
    list_dict = []

    for row in reader:
        # print(row)
        # print(row["Job Class"])
        # compiles all the different key-value pairs into one dictionary
        list_dict.append(row)
        #print(row["Job Class"], row["Percentage"])

    # removes Total row
    list_dict.pop()

app = Flask(__name__)

@app.route("/") 
def roster():
    return "Team Whole Lotta Coding: Emerson Gelobter, Aden Garbutt, Prattay Dey <br> SoftDev Period 07 <br> 2022-10-07"

@app.route("/") 
def weighted_pick():
    randnum = random.random() * 100
    current_sum = 0
    row = 0
    for key in list_dict:
        if (row != 0):
            current_sum += float(key["Percentage"])
        if (current_sum >= randnum):
            print(key["Job Class"])
            return key["Job Class"]
        row += 1
    print(key["Job Class"])
    return key["Job Class"]


app.run()


'''
DISCO:
QCC:
0.Can i run it with an input
1.how does the run command work
2.
3.
4.
5.
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''
