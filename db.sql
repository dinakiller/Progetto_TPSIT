CREATE DATABASE db;


CREATE TABLE Prodotti(
  cod-prodotto int(20) NOT NULL UNIQUE,
  tipologia varchar(20)
  colore varchar(15),
  costo float NOT NULL, 
  peso float NOT NULL,
  materiale varchar(15),
 PRIMARY KEY(cod-prodotto)
);


CREATE TABLE Aziende(
  nome-azienda varchar(20) NOT NULL UNIQUE,
  partita-iva varchar(15),
 indirizzo varchar(30),
 nazione varchar(30),
 forma-giuridica varchar(20),
PRIMARY KEY (nome-azienda)
);


CREATE TABLE Vendite(
n-azienda varchar(20) NOT NULL,
codice-prodotto int(20) NOT NULL,
quantita int NOT NULL,
data date(),

FOREIGN KEY (codice-prodotto) REFERENCES Prodotti(cod-prodotto),
FOREIGN KEY (n-azienda) REFERENCES Aziende(nome-azienda),
CONSTRAINT cod-vendita PRIMARY KEY (n-azienda,codice-prodotto)
);


INSERT INTO Prodotti(cod-prodotto,tipologia,colore,costo,peso,materiale)
VALUES (1, 'divano', 'rosso', 300, 300, 'pelle');

INSERT INTO Prodotti
VALUES (2, 'divano', 'verde', 450,250,'pelle');
INSERT INTO Prodotti
VALUES (3, 'bicchiere','rosso',0.30, 0.15, 'plastica');
INSERT INTO Prodotti
VALUES (4, 'set-tovaglioli','bianco',1, 1.50, 'carta');
INSERT INTO Prodotti
VALUES (5, 'sedia','marrone',40, 5, 'legno');
INSERT INTO Prodotti
VALUES (6, 'lampadina','trasparente',6.50, 1, 'vetro');

INSERT INTO Aziende(nome-azienda,partita-iva,indirizzo,nazione,forma-giuridica)
VALUES ('ikea',86334519757,'via roma 11','italia','SPA');
INSERT INTO Aziende
VALUES ('dalmonego',5416461001,'Unter den Linden 14','germania','SAPA');
INSERT INTO Aziende
VALUES ('A.G._INFORMATICA',4641681004,'Rue de Rivoli','francia','SRL');
INSERT INTO Aziende
VALUES ('Prudential',13022491008,'Kings Road 89','inghilterra','SPA');


INSERT INTO Vendite(n-azienda,codice-prodotto,quantita,data)
VALUES ('ikea',1,2,2004-06-26)
INSERT INTO Vendite
VALUES ('ikea',2,4,1971-09-7);
INSERT INTO Vendite
VALUES ('dalmonego',5,10,1492-06-16);
INSERT INTO Vendite,
VALUES ('A.G._INFORMATICA',4,6,2005-11-23);
INSERT INTO Vendite
VALUES ('Prudential',3,5,2016,11,10);









