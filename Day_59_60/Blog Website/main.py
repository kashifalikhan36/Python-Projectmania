from flask import Flask, render_template, request
from post import Post

app=Flask(__name__)
post_exec=Post()

@app.route("/")
def home():
    return render_template("index.html",posts=post_exec.post())
@app.route("/post")
def details(num):
    print(num)
    for i in post_exec.post():
        if i['id']==int(num):
            return render_template("post.html",post=i)
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact", methods=["POST","GET"])
def contact():
    if request.method=="POST":
        print(request.form)
        return render_template("contact.html", head="We got ur info ! WE will contact u ater !")
    return render_template("contact.html", head="Contact Me")

app.run(debug=True)