#Team Jelly Jam Pancakes: Jacob, Jeremy, Prattay
#SoftDev
#Sessions Greetings
#Oct 2022
#time spent: ______

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

app = Flask(__name__)    #create Flask object
username = "JJP"
password = "abc123"

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request) # prints webpage address that is making the request
    print("***DIAG: request.args ***")
    print(request.form) #used for a POST request
    #print(request.args) # used for a GET request
    # print("***DIAG: request.args['username']  ***")
    # print(request.args['username']) # results in a BadRequestKeyError
    print("***DIAG: request.headers ***")
    print(request.headers)
    '''
    return render_template( 'login.html' )


@app.route("/login", methods=['GET', 'POST'])
def authenticate():
    
    '''
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username']  ***")
    print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)

    #Use this to force a post request
    print("***DIAG: request.form ***")
    print(request.form)
    #print(request.args['username'] + request.args['sub1'])
    #return render_template('response.html')
    #print(request.form)
    '''
    if request.method == 'GET':
        if request.args['username'] == username and request.args['password'] == password:
            return render_template('response.html', username = request.args['username'], password = request.args['password'], method = request.method)  #For 'get'

        else: 
            if request.args['username'] == username:
                if request.args['password'] != password:
                    return render_template('fail.html', username = request.args['username'], method = request.method) #password fail
                return render_template('fail.html', username = request.args['username'], )

    if request.method == 'POST':
        return render_template('response.html', username = request.form['username'], password = request.form['password'],  method = request.method)  #For 'post'

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()