#!/usr/bin/python
# Run this on greenroom-pi during autostart script
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time
 
import web

PORT_NUMBER = 8081

urls = (
    '/studios', 'studios'
)

app = web.application(urls, globals())

class studios:
	
	#Handler for the GET requests
	def GET(self):
		GPIO.setup(15, GPIO.IN) 
		GPIO.setup(16, GPIO.IN) 
		GPIO.setup(18, GPIO.IN) 

		astate = 1 - GPIO.input(15)
		bstate = 1 - GPIO.input(16)
		remstate = 1 - GPIO.input(18)
		web.header('Access-Control-Allow-Origin', '*')

		json = '{ "a": ' + str(astate) + ', "b": ' + str(bstate) + ', "remote" :' + str(remstate) + '}'

		return json

if __name__ == '__main__':
    app.run()
