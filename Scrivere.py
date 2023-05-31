def solo_lettere(text):#funzione per inserire solo lettere nell'inserimento dati
    if text.isalpha():
        return True
    else:
        return False
    
def solo_numeri(text):#funzione per inserire solo nuemri nell'inserimento dati
    if text.isdigit():
        return True
    else:
        return False 