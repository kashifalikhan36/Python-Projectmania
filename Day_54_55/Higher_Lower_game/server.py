from flask import Flask
import random
gen_num=0
app=Flask(__name__)

# @app.route('/')
# def Home():
#     global gen_num
#     gen_num=random.randint(0,9)
#     return "<h1 style='text-align:center>Guess a number between 0 and 9</h1>" \
#     '<img src="https://giphy.com/embed/3o7aCSPqXE5C6T8tBC" width="480" height="480" >' 
@app.route('/')
def Home():
    global gen_num
    gen_num = random.randint(0, 9)
    return "<h1 style='text-align:center'>Guess a number between 0 and 9</h1>" \
        '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWEwODk5MDYwYjRhZjNlNTc0ZTMzNjhiMDA1MzMzMzMzMmIwOGEyMiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o7aCSPqXE5C6T8tBC/giphy.gif" width="480" height="480">'


@app.route('/<int:number>')
def num(number):
    if number==gen_num:
        return '<h1> Gotcha u got it </h1>' + right_num()
    elif number<gen_num:
        return '<h1> Its too low </h1>' + low_num()
    elif number>gen_num:
        return '<h1> Its too high </h1>' + high_num()
def low_num():
    return '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExODU4NWMwZGU2MzZhNzI4MjI2Yzk4OGM1NmYxNjg5NmQ2NmJmZTk4YyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/TgmiJ4AZ3HSiIqpOj6/giphy.gif" width="480" height="270">'
def high_num():
    return '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTFmOTYzZjM2MjViMmJmNThhMTlhMmFmZGQ5OTc3ZjkxYTZkM2NiNCZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/l2YWy9pD8sZEUMF0s/giphy.gif" width="480" height="270" >'
def right_num():
    global gen_num
    gen_num = random.randint(0, 9)
    return '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzc4MjdkODc3NDYwMmIwNzQzMjdlYzc1MTQwMmZkZTU5OGVhYjllMyZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/jB57cmKYDKuNw68W1G/giphy.gif" width="480" height="270" >'
if __name__=="__main__":
    app.run(debug=True)