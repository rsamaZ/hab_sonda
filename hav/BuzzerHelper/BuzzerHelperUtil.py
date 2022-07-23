import time
import sys
import os


def getBuzzerDataFromFile():
    buzzerData = [str(0), str(0)]
    try:
        with open('/data/hab_sonda/logs/buzzerdata.log') as buzzerdatafile:
            line = list(buzzerdatafile)[-1]
        bdata = line.split('|')
        buzzerData[0] = str(bdata[1])
        buzzerData[1] = str(bdata[2])
        return buzzerData
    except:
        return buzzerData
