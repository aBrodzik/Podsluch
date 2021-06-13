rtl_fm_pid=$(pidof rtl_fm) && kill $rtl_fm_pid
nc_pid=$(pidof nc) && kill $nc_pid
ffmpeg_pid=$(pidof ffmpeg) && kill $ffmpeg_pid
icecast2_pid=$(pidof icecast2) && kill $icecast2_pid
