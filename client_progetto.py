import socket
import sys

# Creazione socket
sock = socket.socket()
sock.connect(('localhost', 8000))

# Lettura query dall'utente
try:
    query = input("Inserisci la query: ")

    # Invio query al server
    sock.send(query.encode('utf-8'))

    # Ricezione dei risultati dal server
    results = sock.recv(1024).decode('utf-8')

    # Stampa dei risultati
    print("Risultati:")
    print(results)

    # Chiusura connessione
    sock.close()

except:
    print("Attenzione, errore:", sys.exc_info() [0])