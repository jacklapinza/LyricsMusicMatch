import requests
from time import sleep
import sys

def delay(testo):
    for x in testo:
        print(x, end="")
        sys.stdout.flush()
        sleep(0.01)
    print("")
    return delay

delay('''Script realizzato da Federico Di Lembo.
Questo semplice script permette di ottenere il testo
di una data canzone. 
Per ovvi motivi l'apikey è stata rimosso. Per far funzionare lo script
basta registrarsi sul sito: https://developer.musixmatch.com e utilizzare
la propria API. 
Il piano free concede diversi metodi, che posso essere implementati in questo
programma, per creare un unica app da cui poter scegliere le diverse opzioni.
In questo caso, con un apikey free, sarà possibile ottenere il 30/% di una data
canzone. 
Potete digitare quit per uscire in qualsiasi momento.''')
print("")
print("")
delay("#######")
print("")
print("")

while True:

    

    # URL DI BASE + APIKEY
    base_url = "https://api.musixmatch.com/ws/1.1/matcher.lyrics.get?format=jsonp&callback=callback&q_"

    # INSERIRE LA PROPIA API-KEY -----------------
    apikey = ""

    # TRACCIA
    traccia = input("Nome canzone: ").strip()
    if traccia == "quit":
        exit()

    # ARTISTA
    artista = input("Nome autore: ").strip()
    if artista == "quit":
        exit()

    # RICHIESTA API -- RESTITUISCE UN RESPONSE BODY CHE VA SUCCESSIVAMENTO MANIPOLATO PER PULIRLO DAI CARATTERI SUPERLI
    response = base_url + "track=" + traccia + "&q_" + \
        "artist=" + artista + "&apikey=" + apikey

    # TRASFORMO LA STRINGA (TYPE BYTES) IN STRINGA (TYPE STR)
    data = requests.get(response)
    string = data.content
    string = string.decode("utf-8")

    # ESTRAGGO LA CHIAMATA DELL'ERRORE PER COMPARARLA AL MIO DIZIONARIO
    error = ''',"execute_time"'''
    errore = string[:string.find(error)]
    # print(stringa_2)

    # GESTIONE ERRORI

    error_code = {
        "400": "Cattiva sintassi",
        "401": "Autenticazione fallita. Controlla apikey",
        "402": "Limite richieste raggiunto",
        "403": "Non sei autorizzato a compiere quest'azione",
        "404": "La canzone non è stata trovata",
        "405": "Il metodo della richiesta non è valido",
        "500": "Qualcosa è andato male",
        "503": "Il nostro sistema è sovraccarico, riprova più tardi"
    }

    test = False

    for x in error_code:
        if str(x) in errore:
            print(error_code[x])
            test = True

    while test:
        riprova = input("Vuoi riprovare?: (s/n)").strip()
        if riprova == "s":
            break
        else:
            exit()

    # FUNZIONE DI SCREMATURA TESTO CANZONE

    def scrematura(stringa):
        print("")
        print("")
        print("Testo canzone: ")
        ext = '''body":"'''
        ext_2 = "*******"
        output = stringa[stringa.find(ext):]
        output_2 = output[:output.find(ext_2)]
        output_3 = output_2.replace('''body":''', "")
        output_4 = output_3.replace("\\n", " ")
        output_5 = output_4.replace("\\u00e9", "é")
        output_6 = output_5.replace("\\u00e8", "è")
        output_7 = output_6.replace("\\u00c8", "è")
        output_8 = output_7.replace('''\\"''', "")
        output_9 = output_8.replace("\\u00e0", "à")
        output_10 = output_9.replace("\\u00f9", "ù")
        output_11 = output_10.replace("\\u00f2", "ò")
        output_12 = output_11.replace("\\u00ec", "ì")
        print("")
        print("")
        print("")
        return output_12

    # CONDIZIONE FINALE
    if test == False:
        print(scrematura(string))
        print("")
        print("")
        print("")
    else:
        pass
