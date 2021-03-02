from os import listdir
from os.path import isfile, join
from . import audio, fileWritter
from django.shortcuts import render
from django.template.defaulttags import register
from django.http import HttpResponse
import os


# Create your views here.


def home(request):
    if request.POST:
        if 'connect' in request.POST:
            print('connecting')
        elif 'on' in request.POST:
            print('turing on')
        elif 'off' in request.POST:
            print('turing off')
        elif 'start' in request.POST:
            print('starting rec')
        elif 'stop' in request.POST:
            print('stopping rec')
        elif 'standby' in request.POST:
            print('switching to standby')
        elif 'standaway' in request.POST:
            print('shuting down standby')
        elif 'live' in request.POST:
            print('going live')

    return render(request, 'wiretapp/index.html')


def records(request):
    args={}

    currentName = ''
    """tutaj powinna być użyta zmienna systemowa połączona z zmienną lokalną ścieżki
    środowiska do nagrań, ale na razie zostawiam tak, bo po prostu nie działało inaczej"""
    path = ('C:/Users/g5/PycharmProjects/podsluchDjango/podsluch/wiretapp/static/records')
    recordsList = [f for f in listdir(path) if isfile(join(path, f))]
    fileWritter.updateRecordsJS(recordsList)
    if request.POST:
        i = 0
        for record in recordsList:
            i = i + 1
            if str(i) in request.POST:
                print("playing")
                # audio.play(path + '/'+ recordsList[i - 1])
                currentName = recordsList[i - 1]
                index = i-1
                args['index']=index
                return render(request, 'wiretapp/player.html', args)

    return render(request, 'wiretapp/records.html', {'records': recordsList})


def settings(request):
    return render(request, 'wiretapp/settings.html')


def player(request):
    return render(request, 'wiretapp/player.html')


@register.filter
def get_item(dictionary, key):
    print(dictionary.get(key))
    return HttpResponse(str(dictionary[key]))
