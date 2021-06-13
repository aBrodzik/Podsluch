from os import listdir
from os.path import isfile, join, getsize
from time import sleep

from podsluch.settings import BASE_DIR
from . import fileWritter
from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponse
import os


# Create your views here.
def home(request):

    path = ('wiretapp/static/records')
    recordsList = [f for f in listdir(path) if isfile(join(path, f))]
    fileWritter.updateRecordsJS(recordsList)

    if request.POST:
        if 'start' in request.POST: #zacznij nagrywanie
            print('Starting recording')
            os.system("exec ~/siodemka-master/podsluch/wiretapp/stop.sh")
            os.system("exec ~/siodemka-master/podsluch/wiretapp/start.sh")
        elif 'on' in request.POST: #zacznij odbieranie (do transmisji)
            print('Receiving')
            os.system("exec ~/siodemka-master/podsluch/wiretapp/stop.sh")
            os.system("exec ~/siodemka-master/podsluch/wiretapp/startlive.sh")
        elif 'off' in request.POST: #przestań odbierać (do transmisji)
            print('Stop receiving')
            os.system("exec ~/siodemka-master/podsluch/wiretapp/stop.sh")
            os.system("exec ~/siodemka-master/podsluch/wiretapp/konwlive.sh")
    return render(request, 'wiretapp/index.html')


def records(request):
    args = {}
    path = ('wiretapp/static/records')
    recordsList = [f for f in listdir(path) if isfile(join(path, f))]
    fileWritter.updateRecordsJS(recordsList)

    if request.POST:
        print(request.POST)
        if 'delete' in request.POST:
            delIndex = int(request.POST.get('delete'))
            delName = recordsList[delIndex - 1]
            if os.path.exists("wiretapp/static/records/" + delName):
                os.remove("wiretapp/static/records/" + delName)
                recordsList.remove(delName)

            else:
                print("The file does not exist")

            print('deleting ' + recordsList[delIndex])
            return render(request, 'wiretapp/records.html', {'records': recordsList})

        if 'cut' in request.POST:
            # wyodrębnij minuty i sekundy początku
            startTime = str(request.POST.get('start')).split(":")
            startTimeInSeconds = int(startTime[0]) * 60 + int(startTime[1])
            # wyodrębnij minuty i sekundy końca
            endTime = str(request.POST.get('end')).split(":")
            endTimeInSeconds = int(endTime[0]) * 60 + int(endTime[1])
            # pobierz index pliku i znajdź na jego nazwę
            cutIndex = int(request.POST.get('cut'))
            filename = recordsList[cutIndex]
            ampFactor = int(request.POST.get('amp'))
            # zamień jeśtli start>końca
            if startTimeInSeconds > endTimeInSeconds:
                temp = startTimeInSeconds
                startTimeInSeconds = endTimeInSeconds
                endTimeInSeconds = temp

            print("I need to cut " + filename + " from " + str(startTimeInSeconds) + "s to " + str(
                endTimeInSeconds) + "s and increase amplidute by: " + str(ampFactor) + "dB")
            # wytnij
            fileWritter.cut(startTimeInSeconds, endTimeInSeconds, filename, ampFactor)
            recordsList = [f for f in listdir(path) if isfile(join(path, f))]
            fileWritter.updateRecordsJS(recordsList)
        i = 0
        for record in recordsList:
            i = i + 1
            if str(i) in request.POST:
                print("playing")
                # audio.play(path + '/'+ recordsList[i - 1])
                currentName = recordsList[i - 1]
                index = i - 1
                args['index'] = index
                return render(request, 'wiretapp/player.html', args)

    return render(request, 'wiretapp/records.html', {'records': recordsList})


def settings(request):
    return render(request, 'wiretapp/settings.html')


def player(request):
    return render(request, 'wiretapp/player.html')


def help1(request):
    return render(request, 'wiretapp/help.html')


def about(request):
    return render(request, 'wiretapp/about.html')


### DJANGO VIEW

MAX_CHUNK_SIZE = 32000
MAX_WAV_LENGTH = 4294967303
BYTES_PER_SECOND = 32000

def get_audio(request):
    # get offset
    pos = 0;
    offset = pos * BYTES_PER_SECOND
    file_name = "ImperialMarch60.wav"
    # get range
    r = request.META["HTTP_RANGE"]
    start = int(r.replace("bytes=", "").split("-")[0])
    start_o = start + offset
    path = 'wiretapp/static/records/'

    # in case this is the first request, a wave header is added
    if start == 0:
        with open(path + file_name, "rb") as f:
            data = f.read()
        length = 44
    else:
        data = ""
        length = 0
        start_o -= 44

    file_path = path + file_name

    # wait up to 10 seconds if the end of the file is reached
    # (in case it grows more)
    for _ in range(10):
        size = getsize(file_path)
        if size - start_o > 0:
            break
        else:
            sleep(1)

    length += min(MAX_CHUNK_SIZE, size - start_o)

    # if the length is zero (if end of file is reached and there is
    # nothing more to server), set the total length to the actual
    # served length
    if length == 0:
        total = size - offset + 44
    # else, set the total length to the maximum possible wav length
    # so that the browsers know that it has to send subsequent requests
    else:
        total = MAX_WAV_LENGTH

    # get the actual data from the raw audio file
    with open(file_path, "rb") as f:
        f.seek(start_o)
        data += f.read(length).decode("utf-8")

    # send response with use of Content-Range
    resp = HttpResponse(data, content_type="audio/x-wav", status=206)
    resp["Content-Range"] = "bytes " + str(start) + "-" + str(start + length) + "/" + str(total)
    return resp


@register.filter
def get_item(dictionary, key):
    print(dictionary.get(key))
    return HttpResponse(str(dictionary[key]))

# def home(request):
#    if request.POST:
#        if 'connect' in request.POST:
#            print('connecting')
#        elif 'on' in request.POST:
#            print('turing on')
#        elif 'off' in request.POST:
#            print('turing off')
#        elif 'start' in request.POST:
#            print('starting rec')
#            os.system("exec /home/podsluch/stop.sh")
#            os.system("exec /home/podsluch/start.sh")
#        elif 'stop' in request.POST:
#            print('stopping rec')
#            os.system("exec /home/podsluch/stop.sh")
#        elif 'standby' in request.POST:
#            print('switching to standby')
#        elif 'standaway' in request.POST:
#            print('shuting down standby')
#        elif 'live' in request.POST:
#            print('going live')
#            os.system("exec /home/podsluch/stop.sh")
#            os.system("exec /home/podsluch/startlive.sh")
#            os.system("exec /home/podsluch/sluchajlive.sh")
