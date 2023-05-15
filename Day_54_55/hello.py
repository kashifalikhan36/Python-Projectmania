from flask import  Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello_world!"

@app.route("/bye/<whazzup>")
def bye(whazzup):
    return f"HEllo There! woohooo {whazzup}"


if __name__=="__main__":
    app.run(debug=True)