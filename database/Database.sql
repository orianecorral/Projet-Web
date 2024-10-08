-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mar. 08 oct. 2024 à 10:00
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `Database`
--

-- --------------------------------------------------------

--
-- Structure de la table `Annonce`
--

CREATE TABLE `Annonce` (
  `annonces_id` int(11) NOT NULL,
  `titre` text NOT NULL,
  `adresse` text NOT NULL,
  `nom_entreprise` text NOT NULL,
  `salaire` int(11) NOT NULL,
  `contrat` text NOT NULL,
  `date` date NOT NULL,
  `compagny_id` int(11) NOT NULL,
  `long_description` text NOT NULL,
  `short_description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Annonce`
--

INSERT INTO `Annonce` (`annonces_id`, `titre`, `adresse`, `nom_entreprise`, `salaire`, `contrat`, `date`, `compagny_id`, `long_description`, `short_description`) VALUES
(1, 'Développeur Full-Stack', '12 Rue de Rivoli, 75001 Paris', 'TechAdvance', 45000, 'CDI', '2024-08-21', 1, 'TechAdvance est à la recherche d’un Développeur Full-Stack pour rejoindre une équipe dynamique à Paris. Vous participerez au développement de nos solutions SaaS en utilisant React et Node.js, tout en collaborant avec l\'équipe DevOps pour améliorer les performances et la sécurité des systèmes. Nous recherchons quelqu\'un avec une expérience en développement d\'applications web, des compétences solides en JavaScript, ainsi qu\'une bonne maîtrise des bases de données NoSQL (MongoDB). Si vous êtes passionné par les nouvelles technologies et aimez travailler en équipe, ce poste est fait pour vous.', 'Rejoignez notre équipe de développeurs pour construire des applications web modernes et performantes.'),
(2, 'Ingénieur DevOps', '12 Rue de Rivoli, 75001 Paris', 'TechAdvance', 50000, 'CDI', '2024-08-16', 1, 'En tant qu\'Ingénieur DevOps chez TechAdvance, vous serez responsable de la gestion des pipelines d\'intégration et de déploiement continus (CI/CD). Vous travaillerez en étroite collaboration avec les équipes de développement pour améliorer l\'efficacité et la fiabilité des systèmes. Vous maîtrisez Docker, Kubernetes et les environnements cloud (AWS, Azure). Nous recherchons une personne capable de gérer la scalabilité et la sécurité des infrastructures tout en réduisant les temps de déploiement.', 'Nous recherchons un expert DevOps pour automatiser nos processus d’intégration et de déploiement.'),
(3, 'Chef de Projet IT', '12 Rue de Rivoli, 75001 Paris', 'TechAdvance', 55000, 'CDI', '2024-08-16', 1, 'Vous serez chargé de piloter des projets IT complexes dans un environnement agile.', 'Le Chef de Projet IT sera le point de contact principal pour gérer des projets technologiques chez TechAdvance. Vous serez responsable de la planification, du suivi des délais et de la gestion des ressources tout en coordonnant les différentes équipes de développement et d’infrastructure. Une expérience en méthodologies agiles (Scrum) est indispensable, ainsi que la capacité à comprendre les besoins techniques et commerciaux. Vous assurerez également le suivi de la qualité et la gestion des risques.'),
(4, 'Responsable Marketing Digital', '45 Avenue Foch, 69006 Lyon', 'Innov&Boost', 40000, 'CDD 12 mois', '2024-09-17', 2, 'Innov&Boost est à la recherche d’un(e) Responsable Marketing Digital pour développer et exécuter notre stratégie de marketing numérique. Vous serez en charge de la gestion des campagnes publicitaires en ligne, de l’optimisation du référencement naturel (SEO) et de la gestion des réseaux sociaux. Votre rôle inclut également l’analyse des performances marketing à travers les outils d’analyse (Google Analytics, Facebook Ads Manager). Vous devez être créatif(ve), avoir une expérience significative en marketing digital et être à l’aise avec les outils CRM.', 'Rejoignez notre équipe pour piloter la stratégie marketing digital et augmenter notre visibilité en ligne.'),
(5, 'Community Manager', '45 Avenue Foch, 69006 Lyon', 'Innov&Boost', 30000, 'CDD 6 mois', '2024-10-01', 2, 'En tant que Community Manager chez Innov&Boost, vous aurez pour mission de développer notre communauté en ligne, de créer des contenus engageants, et d’interagir avec nos clients sur différentes plateformes (Instagram, Twitter, Facebook). Vous participerez à la mise en place de campagnes de communication digitale, à la gestion des retours clients et à l’amélioration de notre image de marque. Une bonne maîtrise des outils de création graphique (Canva, Photoshop) et des compétences en rédaction sont attendues.', 'Vous serez responsable de la gestion de nos réseaux sociaux et de la création de contenu engageant.'),
(6, 'Chargé(e) de Communication', '45 Avenue Foch, 69006 Lyon', 'Innov&Boost\r\n', 32000, 'CDI', '2024-09-26', 2, 'Le/la Chargé(e) de Communication sera responsable de l\'élaboration et de la mise en œuvre de la stratégie de communication d\'Innov&Boost. Vous travaillerez sur la rédaction de communiqués de presse, la gestion des relations publiques, et la coordination avec les agences de communication. Vous collaborerez étroitement avec l’équipe marketing pour aligner la communication avec les objectifs de l’entreprise et renforcer notre présence sur le marché. Une expérience dans le domaine de la communication d’entreprise est requise.', 'Gérez nos stratégies de communication interne et externe pour renforcer notre marque.'),
(7, 'Assistant(e) Comptable', '23 Rue du Palais Gallien, 33000 Bordeaux', 'Comptabiliz', 24000, 'Stage 6 mois', '2024-09-19', 2, 'Comptabiliz recherche un(e) Assistant(e) Comptable pour renforcer son équipe à Bordeaux. Vous serez responsable de la saisie des pièces comptables, de la gestion des factures clients et fournisseurs, ainsi que de l’aide à la préparation des bilans annuels. Nous recherchons une personne rigoureuse, avec une bonne connaissance des logiciels comptables (Sage, Ciel) et des normes fiscales. Ce stage peut déboucher sur une embauche en CDI.', 'Aidez à la gestion des écritures comptables et des factures dans un environnement dynamique.\r\n'),
(8, 'Comptable Confirmé(e)', '23 Rue du Palais Gallien, 33000 Bordeaux', 'Comptabiliz', 35000, 'CDI', '2024-09-23', 3, 'En tant que Comptable Confirmé(e) chez Comptabiliz, vous serez en charge de superviser les opérations comptables, de préparer les déclarations fiscales, et de veiller à la conformité des documents financiers. Vous serez également responsable de la gestion des audits internes et de l’accompagnement des jeunes comptables de l’équipe. Une expertise dans l’utilisation des outils comptables et une solide connaissance des normes IFRS et françaises sont indispensables.', 'Rejoignez notre équipe en tant que Comptable Confirmé(e) pour superviser l’ensemble des opérations comptables.'),
(9, 'Data Scientist\r\n', '8 Rue des Carmes, 31000 Toulouse', 'AI Minds', 50000, 'CDI', '2024-09-10', 4, 'AI Minds recherche un Data Scientist pour renforcer son équipe d\'intelligence artificielle. Vous travaillerez sur des projets innovants en utilisant des techniques de machine learning pour développer des modèles prédictifs et des systèmes de recommandation. Une expérience dans la manipulation des données avec Python (Pandas, Scikit-learn) ainsi que des compétences en modélisation statistique sont nécessaires. Vous collaborerez avec des équipes de développeurs pour intégrer les solutions dans des applications réelles.', 'Développez des modèles d\'apprentissage automatique pour des projets innovants.'),
(10, 'Ingénieur Machine Learning', '8 Rue des Carmes, 31000 Toulouse', 'AI Minds', 60000, 'CDI', '2024-09-10', 4, 'AI Minds recherche un Ingénieur Machine Learning pour travailler sur des projets d’intelligence artificielle avancés. Vous serez responsable de la conception d\'algorithmes d\'apprentissage automatique, notamment dans les domaines du traitement du langage naturel (NLP) et de la vision par ordinateur. Vous devez être familier avec les frameworks d\'IA tels que TensorFlow et PyTorch, et avoir une solide compréhension des techniques de deep learning. Une expérience pratique avec des jeux de données massifs et des environnements cloud (AWS) est attendue.', 'Mettez en place des algorithmes de machine learning pour améliorer nos solutions IA.');

-- --------------------------------------------------------

--
-- Structure de la table `Condidatures`
--

CREATE TABLE `Condidatures` (
  `candidatures_id` int(11) NOT NULL,
  `annonces_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Entreprise`
--

CREATE TABLE `Entreprise` (
  `compagny_id` int(11) NOT NULL,
  `nom_entreprise` text NOT NULL,
  `adresse` text NOT NULL,
  `pageweb` text NOT NULL,
  `taille` text NOT NULL,
  `description` text NOT NULL,
  `annonce_id` int(11) NOT NULL,
  `email` text NOT NULL,
  `mdp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Entreprise`
--

INSERT INTO `Entreprise` (`compagny_id`, `nom_entreprise`, `adresse`, `pageweb`, `taille`, `description`, `annonce_id`, `email`, `mdp`) VALUES
(1, 'TechAdvance', '12 Rue de Rivoli, 75001 Paris, France', 'www.techadvance.fr', '150', 'TechAdvance est une entreprise spécialisée dans le développement de solutions SaaS et de plateformes numériques pour les entreprises. Fondée en 2014, TechAdvance accompagne ses clients dans leur transformation digitale en offrant des services sur mesure dans les domaines du développement web, du cloud, et de la cybersécurité. Son expertise en technologies de pointe telles que React, Node.js et Kubernetes en fait un acteur incontournable dans l\'écosystème tech français.', 1234, 'contact@techadvance.fr', 'azerty'),
(2, 'Innov&Boost', '45 Avenue Foch, 69006 Lyon, France', 'www.innovboost.com', '75', 'Innov&Boost est une agence de conseil en marketing digital qui aide les entreprises à accroître leur visibilité en ligne et à optimiser leurs performances marketing. Créée en 2016, Innov&Boost propose des services en gestion de campagnes publicitaires, SEO, gestion des réseaux sociaux et stratégie de contenu. Grâce à une équipe d\'experts en marketing digital, l\'agence collabore avec des startups et des PME pour les aider à atteindre leurs objectifs de croissance.', 56, 'info@innovboost.com', 'azerty'),
(3, 'Comptabiliz', '23 Rue du Palais Gallien, 33000 Bordeaux, France', 'www.comptabiliz.fr', '40', 'Comptabiliz est un cabinet d\'expertise comptable basé à Bordeaux, spécialisé dans la comptabilité, la fiscalité, et le conseil financier pour les entreprises. Depuis sa création en 2010, Comptabiliz s\'est forgé une solide réputation grâce à son expertise et à ses services personnalisés pour les PME et les entrepreneurs. Le cabinet accompagne ses clients dans la gestion quotidienne de leurs finances et dans l\'optimisation de leurs processus comptables.', 78, 'service@comptabiliz.fr', 'azerty'),
(4, 'AI Minds', '8 Rue des Carmes, 31000 Toulouse, France', 'www.aiminds.ai', '120', 'AI Minds est une entreprise innovante spécialisée dans l’intelligence artificielle et le machine learning. Fondée en 2017 à Toulouse, AI Minds conçoit des solutions basées sur l\'IA pour les secteurs de la santé, de la finance et du commerce. Grâce à une équipe d’ingénieurs et de chercheurs en intelligence artificielle, l’entreprise développe des modèles prédictifs et des systèmes de recommandation pour aider les entreprises à prendre des décisions plus éclairées et automatiser des processus complexes.', 910, 'hr@aiminds.ai', 'azerty');

-- --------------------------------------------------------

--
-- Structure de la table `Utilisateur`
--

CREATE TABLE `Utilisateur` (
  `user_id` int(11) NOT NULL,
  `prenom` text NOT NULL,
  `nom` text NOT NULL,
  `email` text NOT NULL,
  `telephone` text NOT NULL,
  `candidature` int(11) NOT NULL,
  `mdp` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Utilisateur`
--

INSERT INTO `Utilisateur` (`user_id`, `prenom`, `nom`, `email`, `telephone`, `candidature`, `mdp`) VALUES
(1, 'Julie', 'Martin', 'julie.martin@example.com', '+33 6 12 34 56 78', 0, 'azerty'),
(2, 'Nicolas', 'Lefebvre', 'nicolas.lefebvre@example.com', '+33 6 87 65 43 21', 0, 'azerty'),
(3, 'Claire', 'Durand', 'claire.durand@example.com', '+33 7 22 33 44 55', 0, 'azerty');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Annonce`
--
ALTER TABLE `Annonce`
  ADD PRIMARY KEY (`annonces_id`);

--
-- Index pour la table `Entreprise`
--
ALTER TABLE `Entreprise`
  ADD PRIMARY KEY (`compagny_id`);

--
-- Index pour la table `Utilisateur`
--
ALTER TABLE `Utilisateur`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Annonce`
--
ALTER TABLE `Annonce`
  MODIFY `annonces_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `Entreprise`
--
ALTER TABLE `Entreprise`
  MODIFY `compagny_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `Utilisateur`
--
ALTER TABLE `Utilisateur`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
