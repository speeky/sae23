-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mar. 09 mai 2023 à 19:44
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `sae`
--

-- --------------------------------------------------------

--
-- Structure de la table `commentaire`
--

DROP TABLE IF EXISTS `commentaire`;
CREATE TABLE IF NOT EXISTS `commentaire` (
  `id_commentaire` int NOT NULL AUTO_INCREMENT,
  `minute` int NOT NULL,
  `commentaire` text NOT NULL,
  `id_match` int NOT NULL,
  PRIMARY KEY (`id_commentaire`),
  KEY `id_match` (`id_match`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `joueur`
--

DROP TABLE IF EXISTS `joueur`;
CREATE TABLE IF NOT EXISTS `joueur` (
  `id_joueur` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(20) NOT NULL,
  `prénom` varchar(20) NOT NULL,
  `année_naissance` int NOT NULL,
  `poste` enum('demi','ailier','contre-pointe','pointe','gardien') CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id_joueur`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `joueur`
--

-- --------------------------------------------------------

--
-- Structure de la table `matchs`
--

DROP TABLE IF EXISTS `matchs`;
CREATE TABLE IF NOT EXISTS `matchs` (
  `id_match` int NOT NULL AUTO_INCREMENT,
  `adversaire` varchar(20) NOT NULL,
  `date` date NOT NULL,
  `lieu` varchar(20) NOT NULL,
  `score_mon_equipe` int NOT NULL,
  `score_adversaire` int NOT NULL,
  `gagnant` tinyint(1) NOT NULL,
  `saison` varchar(20) NOT NULL,
  PRIMARY KEY (`id_match`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `matchs`
--

-- --------------------------------------------------------

--
-- Structure de la table `participer`
--

DROP TABLE IF EXISTS `participer`;
CREATE TABLE IF NOT EXISTS `participer` (
  `id_participer` int NOT NULL AUTO_INCREMENT,
  `id_match` int NOT NULL,
  `id_joueur` int NOT NULL,
  PRIMARY KEY (`id_participer`),
  KEY `id_match` (`id_match`),
  KEY `id_joueur` (`id_joueur`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `participer`
--

-- --------------------------------------------------------

--
-- Structure de la table `statistique_joueur`
--

DROP TABLE IF EXISTS `statistique_joueur`;
CREATE TABLE IF NOT EXISTS `statistique_joueur` (
  `id_stat` int NOT NULL AUTO_INCREMENT,
  `présence` tinyint(1) NOT NULL,
  `position` enum('demi','ailier','contre-pointe','pointe','gardien') NOT NULL,
  `nb_but` int NOT NULL,
  `nb_faute` int NOT NULL,
  `id_participer` int NOT NULL,
  PRIMARY KEY (`id_stat`),
  KEY `id_participer` (`id_participer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Contraintes pour les tables déchargées
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE IF NOT EXISTS `login` (
  `id_login` int NOT NULL AUTO_INCREMENT,
  `login` varchar(20) NOT NULL,
  `mdp` varchar(20) NOT NULL,
  PRIMARY KEY (`id_login`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;



--
-- Contraintes pour la table `commentaire`
--
ALTER TABLE `commentaire`
  ADD CONSTRAINT `match` FOREIGN KEY (`id_match`) REFERENCES `matchs` (`id_match`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `participer`
--
ALTER TABLE `participer`
  ADD CONSTRAINT `joueur` FOREIGN KEY (`id_joueur`) REFERENCES `joueur` (`id_joueur`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `matchs` FOREIGN KEY (`id_match`) REFERENCES `matchs` (`id_match`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Contraintes pour la table `statistique_joueur`
--
ALTER TABLE `statistique_joueur`
  ADD CONSTRAINT `participer` FOREIGN KEY (`id_participer`) REFERENCES `participer` (`id_participer`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
