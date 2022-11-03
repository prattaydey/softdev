#Team Jelly Jam Pancakes: Jacob, Jeremy, Prattay
#SoftDev
#Sessions Greetings
#Oct 2022
#time spent: ______

@app.route("/", methods=['GET', 'POST'])
def disp_loginpage():
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
    return render_template( 'login.html' )


@app.route("/auth", methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.form) #used for a POST request
    #print(request.args) # used for a GET request
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'response.html', user = request.form['username'], method = request.method )  #response to a form submission