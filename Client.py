import socket

# crea il socket del client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specifica l'indirizzo del server e la porta a cui connettersi
server_address = ('localhost', 13456)

# connettiti al server
client_socket.connect(server_address)

# invia la richiesta al server
while True:
    
    identificazione = input('Inserisci 0 se sei un cliente, 10 se sei un fornitore: ')
    
    


    if identificazione == '0':
        client_socket.send(identificazione.encode())
        print('Inserisci la tua richiesta:')
        print('1: Se vuoi visualizzare tutti i prodotti')
        print('2: Se vuoi visualizzare i nostri clienti')
        print('3: Se vuoi visualizzare i nostri fornitori')
        print('4: Se sei un fornitore e vuoi fornire un prodotto')
        print('5: Se sei un cliente e vuoi effettuare un ordine')
        print('100: Se vuoi uscire dal programma')
        request = input()
        try:
            if request == '1':
                client_socket.send(request.encode())
                response = client_socket.recv(1024).decode()
                print(response)
       
            elif request == '2':
                client_socket.send(request.encode())
                responsea = client_socket.recv(1024).decode()
                print(responsea)
       
            elif request == '3':
                client_socket.send(request.encode())
                responseb = client_socket.recv(1024).decode()
                print(responseb)
       
            elif request == '4':
                client_socket.send(request.encode())
                print ('Non sei un fornitore, non hai i permessi necessari per aggiungere un prodotto!')
        
            elif request == '5':
                client_socket.send(request.encode())
                cod= input('Codice: ')
                client_socket.send(str(cod).encode())
        
            elif request == '100':
                print('Arresto del programma in corso!!!')
                break
        except ConnectionAbortedError:
            print('Connessione interrotta dal server. Riconnessione in corso...')
            client_socket.close()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(server_address)
        finally:
            identificazione = ""
            request = ""
    
    elif identificazione == '10':
        client_socket.send(identificazione.encode())
        print('Inserisci la tua richiesta:')
        print('1: Se vuoi visualizzare tutti i prodotti')
        print('2: Se vuoi visualizzare i nostri clienti')
        print('3: Se vuoi visualizzare i nostri fornitori')
        print('4: Se sei un fornitore e vuoi fornire un prodotto')
        print('5: Se sei un cliente e vuoi effettuare un ordine')
        print('100: Se vuoi uscire dal programma')
        request = input()
        try:
            if request == '1':
                client_socket.send(request.encode())
                response = client_socket.recv(1024).decode()
                print(response)
        
            elif request == '2':
                client_socket.send(request.encode())
                responsec = client_socket.recv(1024).decode()
                print(responsec)
       
            elif request == '3':
                client_socket.send(request.encode())
                responsed = client_socket.recv(1024).decode()
                print(responsed)
        
        
            elif request == '4':
                client_socket.send(request.encode())
                codprod = input ('Codice: ')
                client_socket.send(str(codprod).encode())
                tip = input ('Tipologia: ')
                client_socket.send(str(tip).encode())
                col = input ('Colore: ')
                client_socket.send(str(col).encode())
                cost = input ('Costo: ')
                client_socket.send(str(cost).encode())
                pes = input('Peso: ')
                client_socket.send(str(pes).encode())
                mat = input ('Materiale: ')
                client_socket.send(str(mat).encode())
        
        
            elif request == '5':
                client_socket.send(request.encode())
                print('Non sei un cliente, per poter effettuare un ordine accedi come cliente!')
        
            elif request == '100':
                print('Arresto del programma in corso!!!')
                break
        except ConnectionAbortedError:
            print('Connessione interrotta dal server. Riconnessione in corso...')
            client_socket.close()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(server_address)
        finally:
            identificazione = ""
            request = ""
       
    else:
        print('Valore inserito non valido!')






# chiudi la connessione con il server
client_socket.close()
