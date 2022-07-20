import time
import sys
import os

#Metodo que recupera los datos del UV del archivo de datos del servicio
def getBuzzerDataFromFile():
        buzzerData = ["ERROR"]
        try:
                with open('/data/hab_sonda/logs/buzzerdata.log') as buzzerdatafile:
                        line = list(buzzerdatafile)[-1]
                bdata = line.split('|')
                buzzerData[0] = str(bdata[1])
                return buzzerData
        except:
                return buzzerData

