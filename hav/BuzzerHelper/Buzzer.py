import RPi.GPIO as GPIO
import time

buzzerPin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)


def initialCheck():
    GPIO.output(buzzerPin, GPIO.HIGH)
    time.sleep(0.25)
    print("Buzzer Armado - Ready and waiting for GPS signal")
    GPIO.output(buzzerPin, GPIO.LOW)


def on():
    GPIO.output(buzzerPin, GPIO.HIGH)
    print("Buzzer ON - HAB altitude is under 10000m")