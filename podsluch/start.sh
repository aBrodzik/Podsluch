data1=$(date --rfc-3339=d)
data2=$(date --rfc-3339=s)
data3=$(echo $data2 | awk '{ print substr( $0, 12 ) }')
dash=-
sciezka=/home/podsluch/siodemka-master4/podsluch/wiretapp/static/records/nagranie
rozszerzenie=.wav
polaczone=$sciezka$data1$dash$data3$rozszerzenie
rtl_fm -f 446.14375M -E dc -s 12.5k 2> /dev/null | sox -t raw -r 12.5k -e s -b 16 -c 1 -V1 - -t wav $polaczone sinc 300-3400 lowpass 1887 > /dev/null &
