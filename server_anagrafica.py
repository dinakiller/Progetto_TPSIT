import socket
import sqlite3

# crea la funzione per eseguire una query sul database
def run_query(query):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result

# crea la funzione per gestire le richieste del client
def handle_request(conn):
    while True:
        # riceve la richiesta dal client
        data = conn.recv(1024)
        if not data:
            break
        # decodifica la richiesta
        request = data.decode('utf-8')
        # esegue la query sul database
        result = run_query(request)
        # invia il risultato al client
        conn.sendall(str(result).encode('utf-8'))

# crea la funzione per avviare il server
def start_server():
    # crea il socket del server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print('Server in ascolto su localhost:12345...')
    # accetta le connessioni dei client e gestisci le richieste
    while True:
        conn, addr = server_socket.accept()
        print('Connessione accettata da', addr)
        handle_request(conn)
        conn.close()

if __name__ == '__main__':
    start_server()
