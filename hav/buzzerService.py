#################################################################################
#               Proyecto:   buzzerService                                       #
#               Autor: Oscar Loras Delgado				                        #
#                                                                               #
#################################################################################

import time
import logging
import ConfigHelper
from BuzzerHelper import Buzzer
#from RuleHelper import ruleService

# Creacion del loger para los datos cientificos
logger = logging.getLogger('server_logger')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('/data/hab_sonda/logs/buzzerdata.log')
fh.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s|%(message)s|', datefmt='%Y-%m-%d %H:%M:%S')
fh.setFormatter(formatter)
logger.addHandler(fh)

# Creacion del logger para los logs de aplicacion
loggerLog = logging.getLogger('server_logger1')
loggerLog.setLevel(logging.INFO)
inf = logging.FileHandler('/data/hab_sonda/logs/buzzerService.log')
inf.setLevel(logging.INFO)
formatterInformer = logging.Formatter(
    '[%(asctime)s][%(levelname)s][%(message)s]', datefmt='%Y-%m-%d %H:%M:%S')
inf.setFormatter(formatterInformer)
loggerLog.addHandler(inf)

act = ConfigHelper.isBuzzerActivo()
tiempoMuestreoBuzzer = ConfigHelper.getTiempoMuestreoBuzzer()

loggerLog.info("[buzzerService] tiempoMuestreoBuzzer: " +
               str(tiempoMuestreoBuzzer))

if act == 1:

    try:
        tiempoMuestreoBuzzer = ConfigHelper.getToken(
            "Buzzer", "tiempoMuestreoBuzzer", tiempoMuestreoBuzzer)

        Buzzer.initialCheck()
        # thresholdOp:GPS.0.lt.10000:buzzer.on

    except Exception as e:
        loggerLog.error("[buzzerService] Exception: " + str(e))
        loggerLog.error(
            "[buzzerService] Se ha producido un error, se sigue iterando...")
        time.sleep(5)
else:
    loggerLog.warning("[buzzerService] El sensor no ha sido activado!")
