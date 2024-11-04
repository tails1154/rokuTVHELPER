print("Loading Modules")
import requests
import datetime
import os
import time
print("Starting...")
print(datetime.datetime.now().hour)
hour=input("Enter the hour that you want the TV to be turned off:")
min=input("Enter the minute that you want the TV to be turned off:")
tvip=input("Enter the TV's ip address:")


def loop():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	print(str(datetime.datetime.now()))
	print("Turning off TV at: " + hour + ":" + min)
	print(datetime.datetime.now().min)
	if str(datetime.datetime.now().hour) == str(hour) and str(datetime.datetime.now().minute) == str(min):
		print("It's time to turn off the tv!")
		requests.post("http://" + tvip + ":8060/keypress/Power")
		print("Good Night!")
	else:
		time.sleep(1)
		loop()
loop()
print("Exiting...")
