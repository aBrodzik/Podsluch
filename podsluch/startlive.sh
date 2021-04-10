#rtl_fm -f 446.14375M -E dc -s 12.5k 2> /dev/null | sox -t raw -r 12.5k -e s -b 16 -c 1 -V1 - -t wav /home/podsluch/siodemka-master/podsluch/wiretapp/static/live/trueLiveTest.wav sinc 300-3400 lowpass 1887> /dev/null &
rtl_fm -f 446.14375M -E dc -g 0 -s 12.5k 2> /dev/null|play -r 12.5k -t raw -e s -b 16 -c 1 -V0 - sinc 300-3400 lowpass 1887 2> /dev/null&
