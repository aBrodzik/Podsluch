from array import array

from flask import Flask, redirect, url_for, render_template, request
from os import listdir
from os.path import isfile, join

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/records", methods=['GET', 'POST'])
def records():
    # pobierz liste plików z katalogu, przyda się z tego zrobić oddzielną funkcję
    path = "static/records"
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    records = request.form.getlist('records[]')
    if not records:
        records = onlyfiles;
    print('records to display', records)
    return render_template("records.html", records=records)


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/connect", methods=["GET", "POST"])
def connect():
    if request.method == "POST":
        print("connecting...")

    return render_template("index.html")


@app.route("/onoff", methods=["GET", "POST"])
def onoff():
    if request.method == 'POST':
        if request.form["off"] == "off":
            print("turning off")
        elif request.form["on"] == "on":
            print("turning on")

    return render_template("index.html")


@app.route("/rec", methods=["GET", "POST"])
def rec():
    if request.method == "POST":
        print("recording")

    return render_template("index.html")


@app.route("/sb", methods=["GET", "POST"])
def standby():
    if request.method == "POST":
        print("staring standby")

    return render_template("index.html")


@app.route("/live", methods=["GET", "POST"])
def live():
    if request.method == "POST":
        print("live")

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
