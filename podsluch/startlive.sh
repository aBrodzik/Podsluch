#rtl_fm -f 446.14375M -E dc -s 12.5k 2> /dev/null | sox -t raw -r 12.5k -e s -b 16 -c 1 -V1 - -t wav /home/podsluch/siodemka-master2/podsluch/wiretapp/static/live/trueLiveTest.wav sinc 300-3400 lowpass 1887> /dev/null &


#to bylo do kamienia milowego
#rtl_fm -f 446.14375M -E dc -g 0 -s 12.5k 2> /dev/null|play -r 12.5k -t raw -e s -b 16 -c 1 -V0 - sinc 300-3400 lowpass 1887 2> /dev/null&

#czasem trzeba wylaczyc firewall na serwerze zeby dzialalo, np "sudo ufw disable"

#netcat
#rtl_fm -f 446.14375M -E dc -g 0 -s 12.5k 2> /dev/null|sox -r 12.5k -t raw -e s -b 16 -c 1 -V0 - -t wav - sinc 300-3400 lowpass 1887 2> /dev/null | nc -l 8001&

#okreslenie nazwy pliku
data1=$(date --rfc-3339=d)
data2=$(date --rfc-3339=s)
data3=$(echo $data2 | awk '{ print substr( $0, 12 ) }')
data4=$(echo $data3 | awk '{ print substr( $0, 1, length($0)-6 ) }')
dash=-
sciezka=/home/podsluch/siodemka-master/podsluch/wiretapp/static/records/nagraniezlive
rozszerzenie=.mp3
polaczone=$sciezka$data1$dash$data4$rozszerzenie

rtl_fm -f 446.14375M -E dc -s 12.5k 2> /dev/null | sox -t raw -r 12.5k -e s -b 16 -c 1 -V1 - -t mp3 -C 320 $polaczone sinc 300-3400 lowpass 1887 2> /dev/null&
icecast2 -c /home/podsluch/icecast.xml 2>/dev/null&
sleep 4
ffmpeg -ac 1 -re -i $polaczone -acodec libmp3lame -ab 160k -ac 1 -content_type audio/mpeg -f mp3 icecast://source:siodemka@127.0.0.1:8001/transmisja 2>/dev/null&
sleep 1
