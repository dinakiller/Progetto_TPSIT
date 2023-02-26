import mysql.connector
import socket

# Configurazione database MySQL
db_config = {
    'user': 'dinakiller',
    'password': 'superquark/05',
    'host': 'localhost',
    'database': 'db.sql'
}

# Creazione socket
sock = socket.socket()
sock.bind(('localhost', 8000))
sock.listen(1)
print("Server in ascolto sulla porta 8000...")

# Accettazione connessioni client
while True:
    conn, addr = sock.accept()
    print("Connessione accettata da", addr)

    # Connessione al database MySQL
    db = mysql.connector.connect(**db_config)

    # Lettura query dal client
    query = conn.recv(1024).decode('utf-8')
    print("Query ricevuta dal client:", query)

    # Esecuzione query sul database
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # Invio dei risultati al client
    for result in results:
        conn.send(str(result).encode('utf-8'))

    # Chiusura connessione
    conn.close()
    db.close()
