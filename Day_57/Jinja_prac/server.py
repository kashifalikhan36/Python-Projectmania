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
app.run(debug=True)
