import socket

# Creazione socket
sock = socket.socket()
sock.connect(('localhost', 8000))

# Lettura query dall'utente
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
