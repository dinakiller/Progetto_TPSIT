import socket

# crea la funzione per inviare una query al server
def send_query(query):
    # crea il socket del client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    # invia la query al server
    client_socket.sendall(query.encode('utf-8'))
    # riceve la risposta dal server
    data = client_socket.recv(1024)
    # decodifica la risposta
    result = data.decode('utf-8')
    # chiude la connessione
    client_socket.close()
    return result

if __name__ == '__main__':
    # invia una query al server e stampa il risultato
    result = send_query('SELECT * FROM table')
    print(result)
