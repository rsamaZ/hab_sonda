#################################################################################
#               Proyecto:   buzzerService                                          #
#               Autor: Oscar Loras Delgado                                      #
#                                                                               #
#################################################################################

import time
import logging
import ConfigHelper
import RPi.GPIO as GPIO
import ruleService
buzzerPin = 26

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT, initial=GPIO.LOW)

#Creacion del loger para los datos cientificos
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('/data/hab_sonda/logs/buzzerdata.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

#Creacion del logger para los logs de aplicacion
loggerLog = logging.getLogger('server_logger1')
loggerLog.setLevel(logging.INFO)
inf = logging.FileHandler('/data/hab_sonda/logs/buzzerService.log')
inf.setLevel(logging.INFO)
formatterInformer = logging.Formatter('[%(asctime)s][%(levelname)s][%(message)s]', datefmt='%Y-%m-%d %H:%M:%S')
inf.setFormatter(formatterInformer)
loggerLog.addHandler(inf)


act = ConfigHelper.isBuzzerActivo()
tiempoMuestreoBuzzer = ConfigHelper.getTiempoMuestreoBuzzer()

loggerLog.info("[buzzerService] tiempoMuestreoBuzzer: " + str(tiempoMuestreoBuzzer))

if act == 1:

	while True:

		try:
			tiempoMuestreoBuzzer = ConfigHelper.getToken("Buzzer", "tiempoMuestreoBuzzer", tiempoMuestreoBuzzer)

			def on():
				GPIO.output(buzzerPin,GPIO.HIGH)
				print ("Buzzer ON - Emitiendo sonido...")
				time.sleep(1) # Delay in seconds
			
			#ruleService.thresholdOp:GPS.0.lt.10000:buzzer.on
			def off():
				GPIO.output(buzzerPin,GPIO.LOW)
				print ("Buzzer OFF - No sound")
				

			def timeOn():
				time.perf_counter(buzzerPin,GPIO.HIGH)
				print("Tiempo que lleva sonando la sonda: ")
			

            #INICIO: Espacio para recuperar los datos del sensor a partir de la libreria
			buzzerTimer = timeOn()
			buzzerOn = on()
			buzzerOff = off()
			
            #Escritura de datos en el archivo de datos del sensor. Todo lo que se escriba aqui sera lo que potencialmente se acabe enviando por telemetria.
			logger.info(time(buzzerTimer))

                        #FINAL: Espacio para recuperar los datos del sensor a partir de la libreria
			time.sleep(tiempoMuestreoBuzzer)

		except Exception as e:
			loggerLog.error("[buzzerService] Exception: " + str(e))
			loggerLog.error("[buzzerService] Se ha producido un error, se sigue iterando...")
			time.sleep(5)
else:
	loggerLog.warn("[buzzerService] El sensor no ha sido activado!")