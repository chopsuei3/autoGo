import serial
import os
import datetime
import time
import threading

pokemon_caught = 0
pokemon_missed = 0
reconnects = 0
script_starttime = datetime.datetime.now()
timekeeper = int(round(time.time() * 1000))

def check_screen():
#	print "\nChecking screen color...",
#	screen_status = str(os.system("bash /home/user/goplus/check_plus.sh")).replace("\n","")
#	screen_status = os.system("bash /home/user/goplus/check_plus.sh")
	global reconnects
	global check_screen_thread
	try:
		screen_status = os.popen('bash /home/user/goplus/check_plus.sh').read()
	except:
		print "Check screen failed...device connected?"
	time.sleep(1)
	if str(screen_status).replace("\r","").replace("\n","") == "FALSE":
		print "GoPlus icon FAIL"
#		print "Re-connecting...",
		timekeeper_now = int(round(time.time() * 1000))
		if timekeeper_now - timekeeper > 10000:
			reconnects += 1
		ser.write("#")
		response = ser.readline()
		time.sleep(1)
	check_screen_thread = threading.Timer(240,check_screen)
	check_screen_thread.start()
#	if str(response).replace("\n","").rstrip() == "Initialization":
#			print "\nGoPlus CONNECTED!\n"
#		else:
#			print response
#	else:
#		print "GoPlus icon OK\n"
#

def print_status():
	current_datetime = datetime.datetime.now()
	print "\n" + str(current_datetime.strftime("%m-%d-%Y %I:%M:%S %p"))
	timediff = current_datetime - script_starttime
	runtime = divmod(timediff.days * 86400 + timediff.seconds, 60)
	print "Time running = " + str(timediff) + " (H:MM:SS)"
	print "Reconnects = " + str(reconnects)
	print "Pokemon caught = " + str(pokemon_caught)
	print "Pokemon fled = " + str(pokemon_missed) + "\n"
	global print_status_thread
	print_status_thread = threading.Timer(600,print_status)
	print_status_thread.start()


ser = serial.Serial('/dev/ttyUSB0', 9600)

check_screen()
print_status()

try:
	while True:
		output = ser.readline()
		if str(output).replace("\n","").rstrip() != "Initialization":
			print str(output).replace("\n","")
			if int(str(output).split(",")[0]) > 6000:
				if str(output).find('Pokemon Caught') != -1:
					pokemon_caught += 1
				elif str(output).find('Pokemon Not Caught') != -1:
					pokemon_missed += 1
		time.sleep(0.5)
except KeyboardInterrupt:
    print('interrupted!')
    check_screen_thread.cancel()
