from datetime import datetime

def oraCorrente():
# Ottenere l'ora corrente
 ora = datetime.now()

 ora_Oggi = ora.strftime("%d/%m/%Y %H:%M:%S")
 return ora_Oggi
