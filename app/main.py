from flask import Flask, redirect, url_for, render_template, request
from os import listdir
from os.path import isfile, join

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/records", methods=['GET', 'POST'])
def records():

    #pobierz liste plików z katalogu, przyda się z tego zrobić oddzielną funkcję
    path= "static/records"
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

    records=request.form.getlist('records[]')
    if not records:
        records = onlyfiles;
    print('records to display', records)
    return render_template("records.html", records=records)

@app.route("/settings")
def settings():
    return render_template("settings.html")



if __name__ == "__main__":
    app.run()
