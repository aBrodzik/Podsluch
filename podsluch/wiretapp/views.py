from os import listdir
from os.path import isfile, join

from podsluch.settings import BASE_DIR
from . import fileWritter
from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponse
import os


# Create your views here.
def home(request):
    if request.POST:
        if 'start' in request.POST:
            print('connecting')
        elif 'on' in request.POST:
            print('turing on')
        elif 'off' in request.POST:
            print('turing off')
        elif 'start' in request.POST:
            print('starting rec')
        elif 'stop' in request.POST:
            print('stopping rec')
        elif 'live' in request.POST:
            print('going live')

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
