
def updateRecordsJS(listOfRecords):
    path = "C:\\\\Users\\\\g5\\\\PycharmProjects\\\\podsluchDjango\\\\podsluch\\\\wiretapp\\\\static\\\\"
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
