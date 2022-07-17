import RPi.GPIO as GPIO
import time
buzzerPin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)
#import RPi.GPIO as GPIO

def getBuzzerDataFromFile():
        #logger.info(str(round(buzzerStatus,2)) + "|" + str(round(buzzerInitial,4)))
        buzzerData = [str(0), str(0)]
        try:
                with open('/data/hab_sonda/logs/buzzerdata.log') as buzzerdatafile:
                        line = list(buzzerdatafile)[-1]
                bdata = line.split('|')
                buzzerData[0] = str(bdata[1])
                buzzerData[1] = int(bdata[2])
                return buzzerData
        except:
                return buzzerData

def initialCheck():
	GPIO.output(buzzerPin,GPIO.HIGH)
	print ("Buzzer Armado - Ready and waiting for GPS signal")
	time.sleep(1)
	GPIO.output(buzzerPin,GPIO.LOW)
