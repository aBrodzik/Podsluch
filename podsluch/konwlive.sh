plik=/home/podsluch/siodemka-master/podsluch/wiretapp/static/records/nagraniezlive*mp3
sciezka=/home/podsluch/siodemka-master/podsluch/wiretapp/static/records/
nazwa=$(echo $plik | awk '{ print substr( $0, 65 ) }')
nazwa2=$(echo $nazwa| awk '{ print substr( $0, 1, length($0)-4 ) }')
ext=.wav
nazwa3=$nazwa2$ext
nazwa4=$(echo $nazwa3 | sed -r 's/:/-/g')
nazwa5=$sciezka$nazwa4
ffmpeg -y -i $plik $nazwa5 2> /dev/null
rm /home/podsluch/siodemka-master/podsluch/wiretapp/static/records/*mp3 2>/dev/null
