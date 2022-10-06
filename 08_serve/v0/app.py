# Whole Lotta Coding: Prattay, Aden, Emerson
# SoftDev
# Oct 2022

# Prediction: Will print 'No hablo queso!' at the root of the webpage
# Outcome: Prediction was true

from flask import Flask
app = Flask(__name__) # __name__ set to current module that is being run. Allows Flask to locate module when connecting server and browser

@app.route("/") #  '/' points to the root, routing the function to the root URL.
def hello_world():
    print(__name__) # 
    return "No hablo queso!"  #

app.run()  # runs the module
