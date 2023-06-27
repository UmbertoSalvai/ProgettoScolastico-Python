from datetime import datetime

def oraCorrente():
# Ottenere l'ora corrente
 ora = datetime.now()

# Formatta la data e l'ora secondo il tuo desiderio
 ora_Oggi = ora.strftime("%d/%m/%Y %H:%M:%S")
 return ora_Oggi
