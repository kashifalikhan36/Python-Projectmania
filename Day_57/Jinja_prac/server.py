from flask import Flask, render_template
import requests

app=Flask(__name__)

@app.route('/guess/<string:name>')
def home(name):
    data=requests.get(url=f'https://api.agify.io?name={name}').json()
    data_2=requests.get(url=f'https://api.genderize.io?name={name}').json()
    print(data_2)
    age_data=data['age']
    name_data=data['name']
    gender_data=data_2['gender']
    return render_template('index.html',age=age_data,name=name_data,gender=gender_data)

@app.route('/blog')
def blog():
    blog_url='https://api.npoint.io/5b86cb1c2278d8471563'
    blog_posts=requests.get(url=blog_url).json()
    print(blog_posts)
    return render_template('blog.html',blogs=blog_posts)

app.run(debug=True)
