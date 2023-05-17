from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post_data=Post()

@app.route('/')
def home():
    return render_template("index.html",post_exec=post_data.post())
@app.route("/blog/<num>")
def blog_post_details(num):
    for i in post_data.post():
        if i['id']==int(num):
            return render_template("post.html",post_detail=i)
if __name__ == "__main__":
    app.run(debug=True)
