import socket
import mysql.connector

# crea la connessione al database
db = mysql.connector.connect(
  host="localhost",
  user="aledina",
  password="aledina07",
  database="test"
)

# crea il cursore per eseguire le query sul database
cursor = db.cursor()

# crea il socket del server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specifica la porta e l'indirizzo del server
server_address = ('localhost', 13456)

# binda il socket all'indirizzo del server
server_socket.bind(server_address)

# ascolta le richieste in ingresso
server_socket.listen(1)

print('Server in ascolto...')

while True:
    # accetta la connessione dal client
    client_socket, client_address = server_socket.accept()
    print(f"Connessione da {client_address} accettata.")

    # riceve la richiesta del client
    identificazione = client_socket.recv(1024).decode()
    request = client_socket.recv(1024).decode()
    if identificazione == '0':
        
        if request == '1':
            cursor.execute("SELECT * FROM Prodotti")
            results = cursor.fetchall()
            # invia i risultati al client
            client_socket.send(str(results).encode())
        elif request == '2':
            cursor.execute("SELECT * FROM Clienti")
            resultsa = cursor.fetchall()
            # invia i risultati al client
            client_socket.send(str(resultsa).encode())
        elif request == '3':
            cursor.execute("SELECT * FROM Fornitori")
            resultsb = cursor.fetchall()
            # invia i risultati al client
            client_socket.send(str(resultsb).encode())
    
        elif request == '4':
            client_socket.send('Non hai i permessi necessari, il tuo tentativo è stato segnalato!!!'.encode())
            print('Tentativo di accesso del cliente ad una funzionalità riservata ai fornitori!!!')
        elif request == '5':
            try:
                client_socket.send('Inserisci il codice del prodotto che vuoi ordinare: ')
                cod =  client_socket.recv(1024).decode()
                cursor.execute(f"DELETE FROM Prodotti WHERE Cod_Prodotto='{cod}'")
                db.commit()
                # invia un messaggio di conferma al client
                client_socket.send('Il tuo ordine è stato effettuato'.encode())
            except:
                client_socket.send('Sono stati riscontrati problemi durante la transazione')
      
    elif identificazione == '10':
       
        if request == '1':
            cursor.execute("SELECT * FROM Prodotti")
            resultsc = cursor.fetchall()
            # invia i risultati al client
            client_socket.send(str(resultsc).encode())
        elif request == '2':
            cursor.execute("SELECT * FROM Clienti")
            resultsd = cursor.fetchall()
            # invia i risultati al client
            client_socket.send(str(resultsd).encode())
        elif request == '3':
            cursor.execute("SELECT * FROM Fornitori")
            resultsf = cursor.fetchall()
            # invia i risultati al client
            client_socket.send(str(resultsf).encode())
    
        elif request == '4':
            try:
                client_socket.send('Inserisci il codice prodotto'.encode())
                codprod = client_socket.recv(1024).decode()
                client_socket.send('Inserisci la tipologia : '.encode())
                tip = client_socket.recv(1024).decode()
                client_socket.send('Inserisci il colore del prodotto: '.encode())
                col = client_socket.recv(1024).decode()
                client_socket.send('Inserisci il costo del prodotto: '.encode())
                cost = client_socket.recv(1024).decode()
                client_socket.send('Inserisci il peso del prodotto: ')
                pes =  client_socket.recv(1024).decode()
                client_socket.send('Inserisci il materiale del prodotto')
                mat =  client_socket.recv(1024).decode()
                cursor.execute(f"INSERT INTO 'Prodotti' ('Cod_Prodotto', 'tipologia', 'colore', 'costo', 'peso', 'materiale') VALUES ('{codprod}', '{tip}', '{col}', '{cost}', '{pes}', '{mat}')) ")
                db.commit()
                # invia un messaggio di conferma al client
                client_socket.send('Il prodotto è stato aggiunto con successo'.encode())
            except:
                client_socket.send('Problema riscontrato durante la fornitura del prodotto')
        elif request == '5':
            client_socket.send('I fornitori non possono eseguire ordini!!!')
       
    else:
        print('Errore durante la scelta!!!')
        

    # chiude la connessione con il client
    client_socket.close()
