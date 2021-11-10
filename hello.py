from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="static")

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/about")
def about():
    return render_template('about.html', title='About Me')
