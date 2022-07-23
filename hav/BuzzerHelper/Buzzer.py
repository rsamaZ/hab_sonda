import RPi.GPIO as GPIO # pylint: disable=import-error
import time
buzzerPin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)

class Buzzer():
	def initialCheck():
		GPIO.output(buzzerPin,GPIO.HIGH)
		print ("Buzzer Armado - Ready and waiting for GPS signal")
		GPIO.output(buzzerPin,GPIO.LOW)
