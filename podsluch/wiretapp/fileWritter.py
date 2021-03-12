from pydub import AudioSegment


def updateRecordsJS(listOfRecords):
    path = 'wiretapp/static/'
    f = open(path + '\\records.js' ,'w')
    f.write('let track_list=[')
    for record in listOfRecords:
        f.write('{ \n'
                'path: ' + "\"/static/records/" + record + "\",\n"
                'name:' + "\"" + record + "\"" + '},'
        #       'path:' + "\"" + path+ "records" +"\\\\" + record + "\",\n" +
        #        'name:' + "\"" + record + "\"" + '},'
        #        )
                )
    f.write("];")
    f.close()


def cut(start, end, name, dB):
    path = 'wiretapp/static/records/'
    start = start * 1000  # Works in milliseconds
    end = end * 1000
    newAudio = AudioSegment.from_wav(path+name)
    newAudio = newAudio[start:end]
    newAudio = newAudio + dB
    newAudio.export(path+str(start/1000)+"To"+str(end/1000)+name, format="wav")  # Exports to a wav file in the current path.
