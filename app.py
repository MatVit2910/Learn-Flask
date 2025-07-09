from flask import Flask, render_template
from flask_behind_proxy import FlaskBehindProxy
import requests
import random

app = Flask(__name__)               
proxied = FlaskBehindProxy(app)
@app.route("/")                          
def home():
    names = [
    'James', 'Olivia', 'Charlotte', 'Mason', 'Isabella', 'Henry', 'Liam', 'Emma', 'Sophia', 'Noah',
    'Benjamin', 'Amelia', 'Evelyn', 'Alexander', 'Mia', 'Michael', 'Harper', 'Ethan', 'Ava', 'Lucas'
]
    i = random.randint(0, len(names)-1)
    response = requests.get("https://random-d.uk/api/random")
    data = response.json()
    return render_template('home.html', image_url=data["url"], name=names[i])

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/facts")
def gallery():
    return render_template('facts.html')
  
if __name__ == '__main__':               
    app.run(debug=True, host="0.0.0.0")
   