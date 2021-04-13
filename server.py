from flask import Flask, render_template
import requests
import datetime as dt

app = Flask(__name__)


@app.route("/")
def home():
    copyright_date = dt.datetime.now().year
    return render_template("index.html", year=copyright_date)


@app.route("/guess/<name>")
def guess(name):
    age = requests.get(f"https://api.agify.io?name={name}").json()['age']
    gender = requests.get(f"https://api.genderize.io?name={name}").json()['gender']

    return render_template("guess.html", name=name, age=age, gender=gender)


if __name__ == "__main__":
    app.run(debug=True)
