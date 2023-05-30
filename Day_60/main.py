from flask import Flask, render_template, request

app=Flask(__name__)

# @app.route("/")
# def ho():
#     return render_template("index.html")
name=None
password=None
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login", methods=['POST'])
def recieve_data():
    name=request.form["name"]
        # email=request.form["email"]
    password=request.form["password"]
        # message=request.form["name"]
    return f"<h1> Name:- {name}, Password:- {password} </h1>"
        
        

app.run(debug=True)