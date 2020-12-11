
picam = False

if picam:
	from picamera import PiCamera
else:
	import cv2

import time
import telepot
import RPi.GPIO as GPIO
import subprocess



if picam:
	camera = PiCamera()
	camera.rotation = 180

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)
intruder = False
enabled = False

def handle(msg):
	global enabled
	global intruder

	command = msg['text']
	from_id = msg['from']['id']
	#chat_id = msg['chat']['id']
	#print 'Got command: %s' % command
	if from_id == 0000000: # your id from Telegram
		if command.lower() == 'show':
			if picam:
				camera.start_preview()
				time.sleep(5)
				camera.capture('/home/pi/image.jpg')
				camera.stop_preview()
			else:
				camera = cv2.VideoCapture(0)
				return_value, image = camera.read()
				cv2.imwrite('/home/pi/image.jpg', image)
				del(camera)
			inf = open('/home/pi/image.jpg', 'rb')
			#bot.sendMessage(chat_id,text="Done!")
			bot.sendPhoto(chat_id,inf)
		if command.lower() == "enable pir":
			enabled = True
			bot.sendMessage(chat_id,text="PIR enabled")
		if command.lower() == "disable pir":
			enabled = False
			bot.sendMessage(chat_id,text="PIR disabled")
		if command.lower().split(' ')[0]=='say':
		# not using the espeak python module due to raspberry pi and alsa compatibility problems
			command = "espeak -ves \""+command[3:]+"\" --stdout|aplay" # remove or change -ves (spanish text) option to change the language
			process = subprocess.Popen(command,shell=True, executable='/bin/bash')
	else:
		bot.sendMessage(from_id,text="I'm not allowed to talk with you, sorry")
		bot.sendMessage(chat_id,text="Somebody is trying to use the chatbot")

chat_id = xxxxxxx
bot = telepot.Bot('xxxxxxxxx')
bot.message_loop(handle)
#print 'I am listening...'

while 1:
	pirvalue = GPIO.input(11)
	if pirvalue == 1 and intruder == False and enabled == True:
		intruder = True
		if picam:
			camera.start_preview()
			time.sleep(5)
			camera.capture('/home/pi/image.jpg')
			camera.stop_preview()
		else:
			camera = cv2.VideoCapture(0)
			return_value, image = camera.read()
			cv2.imwrite('/home/pi/image.jpg', image)
			del(camera)
		inf = open('/home/pi/image.jpg')
		bot.sendPhoto(chat_id,inf)
	if pirvalue == 0:
		intruder = False
	time.sleep(1)
