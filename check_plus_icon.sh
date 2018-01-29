#/bin/bash
COLOR=$(adb shell 'screencap /sdcard/screen.dump;stringZ=$(dd if=/sdcard/screen.dump bs=4 count=1 skip=130260 2>/dev/null | hd); red=$(echo $stringZ | cut -d" " -f2); green=$(echo $stringZ | cut -d" " -f3); blue=$(echo $stringZ | cut -d" " -f4); rgb="#$red$green$blue"; printf $rgb;')

if [ $COLOR == '#385274' ]
then
	RECONNECT=$(adb shell input tap 647 186)
	echo FALSE
elif [ $COLOR == '#5df619' ]
then
	echo TRUE
#	echo Connected $COLOR
else
	echo TRUE
#	echo Screen off $COLOR
fi
