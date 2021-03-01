
import audio
from flask import Flask,   render_template, request
from os import listdir
from os.path import isfile, join

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get("off"):
            print("turning off")
        elif request.form.get("on"):
            print("turning on")
        elif request.form.get("connect"):
            print("connecting...")
        elif request.form.get("start"):
            print("starting recoring")
        elif request.form.get("stop"):
            print("stopping recording")
        elif request.form.get("standby"):
            print("turning on standby")
        elif request.form.get("standaway"):
            print("shutting down standby")
        elif request.form.get("live"):
            print("starting live")

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


    if request.method == 'POST':
        i=0;
        for record in records:
            i=i+1
            print(request.form.get(str(i)))
            if request.form.get(str(i)):
                print("playing");
                audio.play("static/records/"+records[i-1])
                break

    return render_template("records.html", records=records)





@app.route("/settings")
def settings():
    return render_template("settings.html")


if __name__ == "__main__":
    app.run()
