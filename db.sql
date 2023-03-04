-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Creato il: Mar 04, 2023 alle 12:53
-- Versione del server: 10.1.48-MariaDB-0ubuntu0.18.04.1
-- Versione PHP: 7.2.24-0ubuntu0.18.04.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `Aziende`
--

CREATE TABLE `Aziende` (
  `Nome_Azienda` varchar(20) NOT NULL,
  `partita_iva` varchar(15) DEFAULT NULL,
  `indirizzo` varchar(30) DEFAULT NULL,
  `nazione` varchar(30) DEFAULT NULL,
  `forma_giuridica` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `Aziende`
--

INSERT INTO `Aziende` (`Nome_Azienda`, `partita_iva`, `indirizzo`, `nazione`, `forma_giuridica`) VALUES
('A.G._INFORMATICA', '4641681004', 'Rue de Rivoli', 'francia', 'SRL'),
('dalmonego', '5416461001', 'Unter den Linden 14', 'germania', 'SAPA'),
('ikea', '86334519757', 'via roma 11', 'italia', 'SPA'),
('Prudential', '13022491008', 'Kings Road 89', 'inghilterra', 'SPA');

-- --------------------------------------------------------

--
-- Struttura della tabella `Prodotti`
--

CREATE TABLE `Prodotti` (
  `Cod_Prodotto` int(20) NOT NULL,
  `tipologia` varchar(20) DEFAULT NULL,
  `colore` varchar(15) DEFAULT NULL,
  `costo` float NOT NULL,
  `peso` float NOT NULL,
  `materiale` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `Prodotti`
--

INSERT INTO `Prodotti` (`Cod_Prodotto`, `tipologia`, `colore`, `costo`, `peso`, `materiale`) VALUES
(1, 'divano', 'rosso', 300, 300, 'pelle'),
(2, 'divano', 'verde', 450, 250, 'pelle'),
(3, 'bicchiere', 'rosso', 0.3, 0.15, 'plastica'),
(4, 'set-tovaglioli', 'bianco', 1, 1.5, 'carta'),
(5, 'sedia', 'marrone', 40, 5, 'legno'),
(6, 'lampadina', 'trasparente', 6.5, 1, 'vetro');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `Aziende`
--
ALTER TABLE `Aziende`
  ADD PRIMARY KEY (`Nome_Azienda`);

--
-- Indici per le tabelle `Prodotti`
--
ALTER TABLE `Prodotti`
  ADD PRIMARY KEY (`Cod_Prodotto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
