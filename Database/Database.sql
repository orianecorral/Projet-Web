-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : dim. 20 oct. 2024 à 20:09
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
-- Structure de la table `Annonces`
--

CREATE TABLE `Annonces` (
  `id` int(11) NOT NULL,
  `titre` varchar(400) NOT NULL,
  `adresse` varchar(500) NOT NULL,
  `nom_entreprise` varchar(300) NOT NULL,
  `salaire` varchar(300) NOT NULL,
  `contrat` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `short_description` varchar(255) NOT NULL,
  `long_description` longtext NOT NULL,
  `entreprise_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Annonces`
--

INSERT INTO `Annonces` (`id`, `titre`, `adresse`, `nom_entreprise`, `salaire`, `contrat`, `date`, `short_description`, `long_description`, `entreprise_id`) VALUES
(1, 'Développeur Full-Stack', '12 Rue de Rivoli, 75001 Paris, France', 'Techadvance', '45,000 - 65,000 €', 'CDI', '2024-10-14', 'Nous recherchons un Développeur Full-Stack pour participer au développement de nos solutions SaaS. Vous travaillerez sur des technologies modernes telles que React et Node.js au sein d\'une équipe dynamique et passionnée.', 'Description du poste  \r\nDans un contexte de forte évolution de l’offre de service, TechAdvance recherche un développeur Full Stack (H/F) en CDI.\r\n\r\nAu sein du département des systèmes d’information, vous développerez des solutions logicielles full web en respectant les délais et la qualité.\r\n\r\nVous serez chargé de :\r\n- Rédiger les spécifications techniques\r\n- Concevoir et développer des solutions techniques\r\n- Collaborer avec les autres équipes dans un environnement Agile\r\n- Participer aux tests et à la mise en production\r\n\r\nProfil recherché : Développeur expérimenté avec maîtrise de React, Node.js, SQL et NoSQL. Environnement stimulant et télétravail partiel possible.', 1),
(2, 'Ingénieur DevOps', '12 Rue de Rivoli, 75001 Paris, France ', 'Techadvance', '50,000 - 70,000 €', 'CDI', '2024-10-14', 'Nous recherchons un Ingénieur DevOps pour automatiser nos processus de CI/CD. Vous participerez à la gestion des pipelines et à l\'amélioration continue des systèmes. Rejoignez une équipe technique avancée et ambitieuse.', 'Description du poste  \r\nTechAdvance recherche un Ingénieur DevOps (H/F) en CDI pour renforcer son équipe d\'infrastructure.\r\n\r\nVos missions :\r\n- Automatiser les pipelines CI/CD\r\n- Maintenir et améliorer les systèmes de production\r\n- Collaborer avec les équipes de développement\r\n\r\nProfil : Expérience en Docker, Kubernetes, et scripting Bash/PowerShell.\r\n\r\nAvantages : Télétravail, mutuelle, environnement technique avancé.', 1),
(3, 'Responsable Marketing Digital', '45 Avenue Foch, 69006 Lyon, France', 'Innov&Boost', '40,000 - 55,000 €', 'CDD 12 mois', '2024-10-07', 'En tant que Responsable Marketing Digital, vous piloterez la stratégie de marketing en ligne d\'Innov&Boost pour accroître la visibilité des clients et développer des campagnes de publicité performantes.', 'Description du poste  \r\nInnov&Boost recrute un Responsable Marketing Digital (H/F) en CDD de 12 mois pour piloter la stratégie numérique de ses clients.\r\n\r\nVos missions :\r\n- Définir et mettre en œuvre la stratégie digitale\r\n- Analyser les performances des campagnes\r\n- Gérer les budgets publicitaires\r\n\r\nProfil : Expérience en gestion de campagnes Google Ads et Facebook.\r\n\r\nAvantages : Participation à des projets de transformation digitale passionnants.', 2),
(4, 'Community Manager', '45 Avenue Foch, 69006 Lyon, France', 'Innov&Boost', '30,000 - 35,000 €', 'CDD 6 mois', '2024-10-07', 'Nous recherchons un Community Manager pour gérer nos réseaux sociaux et créer des contenus engageants. Vous développerez notre communauté en ligne et participerez à la stratégie de communication digitale d\'Innov&Boost.', 'Description du poste  \r\nInnov&Boost recrute un Community Manager (H/F) en CDD de 6 mois pour renforcer son équipe de communication.\r\n\r\nVos missions :\r\n- Gérer les réseaux sociaux de l\'agence et des clients\r\n- Créer des contenus engageants\r\n- Analyser les performances des campagnes sociales\r\n\r\nProfil : Dynamique et créatif, avec une passion pour les réseaux sociaux et la création de contenu.\r\n\r\nAvantages : Environnement créatif, participation à des projets variés.', 2),
(5, 'Assistant(e) Comptable', '23 Rue du Palais Gallien, 33000 Bordeaux', 'Comptabiliz', '24,000 - 30,000 €', 'Stage 6 mois', '2024-10-07', 'Nous recherchons un(e) Assistant(e) Comptable pour assister nos équipes dans la gestion quotidienne des écritures comptables, des factures et des comptes clients/fournisseurs. Stage de 6 mois avec possibilité de CDI.\r\n', 'Description du poste  \r\nComptabiliz recherche un Assistant(e) Comptable (H/F) pour un stage de 6 mois, basé à Bordeaux.\r\n\r\nVos missions :\r\n- Saisie des écritures comptables\r\n- Gestion des factures clients et fournisseurs\r\n- Participation aux clôtures mensuelles\r\n\r\nProfil : Étudiant en comptabilité, rigoureux, avec une bonne maîtrise d\'Excel.\r\n\r\nAvantages : Stage rémunéré, possibilité d\'évolution vers un CDI.', 3),
(6, 'Responsable Fiscalité', '23 Rue du Palais Gallien, 33000 Bordeaux', 'Comptabiliz', '45,000 - 55,000 €', 'CDI', '2024-10-07', 'En tant que Responsable Fiscalité chez Comptabiliz, vous serez en charge des déclarations fiscales et de la conformité des entreprises. Vous accompagnerez les clients dans leurs obligations fiscales et optimiserez leur stratégie fiscale.\r\n', 'Description du poste  \r\nComptabiliz recrute un Responsable Fiscalité (H/F) en CDI pour gérer les aspects fiscaux des clients.\r\n\r\nVos missions :\r\n- Préparer et soumettre les déclarations fiscales\r\n- Optimiser la stratégie fiscale des clients\r\n- Assurer la conformité fiscale\r\n\r\nProfil : Expert en fiscalité avec 5 ans d\'expérience en cabinet.\r\n\r\nAvantages : Environnement stimulant et possibilités de développement personnel.', 3),
(7, 'Chef de Projet Informatique', '78 Rue de Belleville, 75020 Paris', 'Okayo', '50,000 - 65,000 €', 'CDI', '2024-10-04', 'Okayo recherche un Chef de Projet Informatique pour gérer des projets d\'intégration logiciels dans le domaine de l\'assurance. Vous assurerez la coordination entre les équipes techniques et fonctionnelles pour mener à bien les projets.', 'Description du poste  \r\nOkayo recrute un Chef de Projet Informatique (H/F) pour coordonner l’intégration de projets logiciels.\r\n\r\nVos missions :\r\n- Planifier et coordonner les projets\r\n- Collaborer avec les équipes techniques et fonctionnelles\r\n- Assurer la satisfaction client\r\n\r\nProfil : Expérience en gestion de projet informatique, idéalement dans le secteur des assurances.\r\n\r\nAvantages : Poste évolutif, télétravail partiel, environnement jeune et innovant.', 4),
(8, 'Consultant MOA', '78 Rue de Belleville, 75020 Paris', 'Okayo', '40,000 - 50,000 €', 'CDI', '2024-10-04', 'Nous recherchons un Consultant MOA pour analyser les besoins clients et coordonner les solutions logicielles adaptées. Vous participerez à la mise en œuvre de projets complexes et collaborerez étroitement avec les équipes techniques.', 'Description du poste  \r\nOkayo recrute un Consultant MOA (H/F) en CDI pour accompagner ses clients dans l’implémentation de solutions logicielles.\r\n\r\nVos missions :\r\n- Analyser les besoins clients\r\n- Proposer des solutions adaptées\r\n- Assurer le suivi de la mise en œuvre\r\n\r\nProfil : Formation Bac +5 avec expérience en maîtrise d’ouvrage et gestion de projet.\r\n\r\nAvantages : Poste à responsabilités, télétravail possible.', 4),
(9, 'Analyste Financier Junior', '100 Rue de la Paix, 75008 Paris', 'FinTechOne', '35,000 - 45,000 €', 'CDI', '2024-10-17', 'Nous recherchons un Analyste Financier Junior pour analyser les performances financières des actifs et produire des rapports détaillés à destination des investisseurs. Poste évolutif avec un environnement technique avancé.', 'Description du poste  \r\nFinTechOne recrute un Analyste Financier Junior (H/F) en CDI pour renforcer son équipe d’analystes.\r\n\r\nVos missions :\r\n- Analyser les performances des actifs financiers\r\n- Rédiger des rapports d’investissement\r\n- Collaborer avec les équipes techniques pour automatiser les processus\r\n\r\nProfil : Diplômé en finance, rigoureux et avec une bonne maîtrise d\'Excel.\r\n\r\nAvantages : Environnement technologique, télétravail, évolution rapide possible.', 5),
(10, 'Développeur Backend Java', '100 Rue de la Paix, 75008 Paris', 'FinTechOne', '50,000 - 70,000 €', 'CDI', '2024-10-18', 'Nous recrutons un Développeur Backend Java pour participer à la création de solutions logicielles pour le secteur financier. Vous travaillerez sur des projets complexes à fort impact au sein d\'une équipe d\'experts techniques.', 'Description du poste  \r\nFinTechOne recherche un Développeur Backend Java (H/F) pour un CDI.\r\n\r\nVos missions :\r\n- Développer des solutions backend pour la gestion d’actifs\r\n- Collaborer avec les équipes de développement frontend\r\n- Optimiser les performances des systèmes\r\n\r\nProfil : Maîtrise de Java, expérience dans les services financiers souhaitée.\r\n\r\nAvantages : Environnement technologique, projets complexes, rémunération attractive.', 5),
(11, 'Data Scientist', '8 Rue de la République, 69001 Lyon', 'DataGenius', '55,000 - 75,000 €', 'CDI', '2024-10-01', 'En tant que Data Scientist, vous analyserez de vastes ensembles de données pour proposer des modèles prédictifs avancés. Vous travaillerez avec des experts techniques pour transformer les données en valeur ajoutée pour les clients.', 'Description du poste  \r\nDataGenius recrute un Data Scientist (H/F) en CDI.\r\n\r\nVos missions :\r\n- Analyser les données des clients\r\n- Proposer des modèles de machine learning\r\n- Optimiser les systèmes de prédiction\r\n\r\nProfil : Expérience en data science, maîtrise de Python et R, et compétences en modélisation.\r\n\r\nAvantages : Environnement innovant, projets passionnants, télétravail partiel.', 6),
(12, 'Data Analyst', '8 Rue de la République, 69001 Lyon', 'DataGenius', '40,000 - 50,000 €', 'CDI', '2024-10-01', 'Nous recherchons un Data Analyst pour analyser les données commerciales et opérationnelles de nos clients. Vous participerez à la création de rapports et de tableaux de bord pour améliorer les performances des entreprises.', 'Description du poste  \r\nDataGenius recrute un Data Analyst (H/F) en CDI.\r\n\r\nVos missions :\r\n- Analyser les données commerciales et opérationnelles\r\n- Créer des rapports de performance\r\n- Collaborer avec les équipes de data science\r\n\r\nProfil : Bac+5 en statistique, bonne maîtrise d\'Excel et SQL.\r\n\r\nAvantages : Projets variés, équipe dynamique, télétravail partiel possible.', 6),
(13, 'Ingénieur Big Data', '8 Rue de la République, 69001 Lyon', 'DataGenius', '60,000 - 80,000 €', 'CDI', '2024-10-01', 'Nous recherchons un Ingénieur Big Data pour participer à l’implémentation de solutions de traitement de grandes quantités de données. Vous travaillerez avec des technologies comme Hadoop et Spark dans un environnement stimulant.', 'Description du poste  \r\nDataGenius recrute un Ingénieur Big Data (H/F) en CDI.\r\n\r\nVos missions :\r\n- Implémenter des solutions Big Data\r\n- Optimiser les processus de traitement des données\r\n- Collaborer avec les équipes d’analyse et de développement\r\n\r\nProfil : Expérience avec Hadoop, Spark, et gestion des flux de données massifs.\r\n\r\nAvantages : Rémunération attractive, projets stimulants, télétravail partiel.', 6),
(14, 'Analyste Business Intelligence', '8 Rue de la République, 69001 Lyon', 'DataGenius', '45,000 - 55,000 €', 'CDI', '2024-10-02', 'Nous recherchons un Analyste Business Intelligence pour développer et optimiser des tableaux de bord et des rapports afin d’améliorer la prise de décision chez nos clients. Vous travaillerez avec des outils BI tels que Power BI et Tableau.', 'Description du poste  \r\nDataGenius recrute un Analyste BI (H/F) en CDI.\r\n\r\nVos missions :\r\n- Développer et optimiser des tableaux de bord BI\r\n- Collaborer avec les équipes de data science\r\n- Améliorer la performance des systèmes décisionnels\r\n\r\nProfil : Bac+5, bonne maîtrise des outils BI (Power BI, Tableau).\r\n\r\nAvantages : Environnement innovant, équipe jeune et dynamique.', 6),
(15, 'Architecte Data', '8 Rue de la République, 69001 Lyon', 'DataGenius', '70,000 - 90,000 €', 'CDI', '2024-10-02', 'DataGenius recherche un Architecte Data pour concevoir des architectures de données robustes et scalables. Vous serez responsable de l’architecture globale des systèmes de données et travaillerez avec les équipes de développement et d\'analyse.', 'Description du poste  \r\nDataGenius recrute un Architecte Data (H/F) en CDI.\r\n\r\nVos missions :\r\n- Concevoir des architectures de données scalables\r\n- Gérer les infrastructures de données\r\n- Collaborer avec les équipes techniques pour garantir la robustesse des systèmes\r\n\r\nProfil : Expérience en architecture de données, maîtrise des outils Big Data.\r\n\r\nAvantages : Poste à responsabilités, télétravail possible.', 6);

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add annonces', 6, 'add_annonces'),
(22, 'Can change annonces', 6, 'change_annonces'),
(23, 'Can delete annonces', 6, 'delete_annonces'),
(24, 'Can view annonces', 6, 'view_annonces'),
(25, 'Can add candidatures', 7, 'add_candidatures'),
(26, 'Can change candidatures', 7, 'change_candidatures'),
(27, 'Can delete candidatures', 7, 'delete_candidatures'),
(28, 'Can view candidatures', 7, 'view_candidatures'),
(29, 'Can add utilisateurs', 8, 'add_utilisateurs'),
(30, 'Can change utilisateurs', 8, 'change_utilisateurs'),
(31, 'Can delete utilisateurs', 8, 'delete_utilisateurs'),
(32, 'Can view utilisateurs', 8, 'view_utilisateurs'),
(33, 'Can add particuliers', 9, 'add_particuliers'),
(34, 'Can change particuliers', 9, 'change_particuliers'),
(35, 'Can delete particuliers', 9, 'delete_particuliers'),
(36, 'Can view particuliers', 9, 'view_particuliers'),
(37, 'Can add entreprises', 10, 'add_entreprises'),
(38, 'Can change entreprises', 10, 'change_entreprises'),
(39, 'Can delete entreprises', 10, 'delete_entreprises'),
(40, 'Can view entreprises', 10, 'view_entreprises');

-- --------------------------------------------------------

--
-- Structure de la table `Candidatures`
--

CREATE TABLE `Candidatures` (
  `id` int(11) NOT NULL,
  `prenom` varchar(100) NOT NULL,
  `nom` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `telephone` varchar(15) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `annonce_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Candidatures`
--

INSERT INTO `Candidatures` (`id`, `prenom`, `nom`, `email`, `telephone`, `user_id`, `annonce_id`) VALUES
(1, 'Antoine', 'Ribeyre', 'ribeyre@epitech.eu', '0607080910', 7, 1),
(2, 'Antoine', 'Ribeyre', 'ribeyre@epitech.eu', '0607080910', 7, 4),
(3, 'Antoine', 'Ribeyre', 'ribeyre@epitech.eu', '0607080910', 7, 8),
(4, 'Antoine', 'Ribeyre', 'ribeyre@epitech.eu', '0607080910', 7, 11),
(5, 'Antoine', 'Ribeyre', 'ribeyre@epitech.eu', '0607080910', 7, 14),
(6, 'Oriane', 'Coral', 'coral@epitech.eu', '0607080910', 9, 10),
(7, 'Oriane', 'Coral', 'coral@epitech.eu', '0607080910', 9, 15),
(8, 'Oriane', 'Coral', 'coral@epitech.eu', '0607080910', 9, 1),
(9, 'Oriane', 'Coral', 'coral@epitech.eu', '0607080910', 9, 5),
(10, 'Amandine', 'Leduc', 'leduc@epitech.eu', '0607080910', 8, 6),
(11, 'Amandine', 'Leduc', 'leduc@epitech.eu', '0607080910', 8, 7),
(12, 'Amandine', 'Leduc', 'leduc@epitech.eu', '0607080910', 8, 12),
(13, 'Amandine', 'Leduc', 'leduc@epitech.eu', '0607080910', 8, 2),
(14, 'Pierre', 'Dupont', 'Dupont@epitech.eu', '0607080910', NULL, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'jobfinder_app', 'annonces'),
(7, 'jobfinder_app', 'candidatures'),
(10, 'jobfinder_compte', 'entreprises'),
(9, 'jobfinder_compte', 'particuliers'),
(8, 'jobfinder_compte', 'utilisateurs'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'jobfinder_app', '0001_initial', '2024-10-20 15:52:51.872883'),
(2, 'contenttypes', '0001_initial', '2024-10-20 15:52:51.921059'),
(3, 'contenttypes', '0002_remove_content_type_name', '2024-10-20 15:52:51.997088'),
(4, 'auth', '0001_initial', '2024-10-20 15:52:52.072812'),
(5, 'auth', '0002_alter_permission_name_max_length', '2024-10-20 15:52:52.382270'),
(6, 'auth', '0003_alter_user_email_max_length', '2024-10-20 15:52:52.392955'),
(7, 'auth', '0004_alter_user_username_opts', '2024-10-20 15:52:52.402710'),
(8, 'auth', '0005_alter_user_last_login_null', '2024-10-20 15:52:52.411334'),
(9, 'auth', '0006_require_contenttypes_0002', '2024-10-20 15:52:52.416290'),
(10, 'auth', '0007_alter_validators_add_error_messages', '2024-10-20 15:52:52.422862'),
(11, 'auth', '0008_alter_user_username_max_length', '2024-10-20 15:52:52.433483'),
(12, 'auth', '0009_alter_user_last_name_max_length', '2024-10-20 15:52:52.442731'),
(13, 'auth', '0010_alter_group_name_max_length', '2024-10-20 15:52:52.461625'),
(14, 'auth', '0011_update_proxy_permissions', '2024-10-20 15:52:52.472109'),
(15, 'jobfinder_compte', '0001_initial', '2024-10-20 15:52:52.621939'),
(16, 'admin', '0001_initial', '2024-10-20 15:52:53.114132'),
(17, 'admin', '0002_logentry_remove_auto_add', '2024-10-20 15:52:53.228791'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-20 15:52:53.244044'),
(19, 'jobfinder_compte', '0002_auto_20241016_1338', '2024-10-20 15:52:53.329678'),
(20, 'jobfinder_app', '0002_auto_20241016_1236', '2024-10-20 15:52:53.548935'),
(21, 'jobfinder_app', '0003_auto_20241016_1338', '2024-10-20 15:52:53.710611'),
(22, 'jobfinder_app', '0004_auto_20241016_2027', '2024-10-20 15:52:53.797564'),
(23, 'jobfinder_app', '0005_auto_20241017_0745', '2024-10-20 15:52:53.880222'),
(24, 'jobfinder_app', '0006_auto_20241017_0837', '2024-10-20 15:52:53.998744'),
(25, 'jobfinder_app', '0007_auto_20241018_1418', '2024-10-20 15:52:54.023756'),
(26, 'jobfinder_app', '0008_alter_annonces_id_alter_candidatures_id', '2024-10-20 15:52:54.297885'),
(27, 'jobfinder_app', '0009_auto_20241019_1756', '2024-10-20 15:52:54.638172'),
(28, 'jobfinder_compte', '0003_alter_entreprises_id_alter_particuliers_id_and_more', '2024-10-20 15:52:55.672010'),
(29, 'jobfinder_compte', '0004_auto_20241019_1756', '2024-10-20 15:52:56.702116'),
(30, 'sessions', '0001_initial', '2024-10-20 15:52:56.734598');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('mg5u2nja7i9spttmv5azgaj80ojw7e92', 'ODQ3NjJlN2ZmNWZhZTk4NDZiM2RhMmI0OTE2ODg0NDE2MTYwYWE4ZTp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNDJmN2RmZDBmZWQ2OWY0YmVkNDg5YjFiMGZmODgzODkzNTcyMWRjIn0=', '2024-11-03 17:48:33.262979');

-- --------------------------------------------------------

--
-- Structure de la table `Entreprises`
--

CREATE TABLE `Entreprises` (
  `id` int(11) NOT NULL,
  `nom_entreprise` varchar(200) DEFAULT NULL,
  `pageweb` varchar(500) DEFAULT NULL,
  `adresse` varchar(300) DEFAULT NULL,
  `taille` varchar(100) DEFAULT NULL,
  `description` longtext NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Entreprises`
--

INSERT INTO `Entreprises` (`id`, `nom_entreprise`, `pageweb`, `adresse`, `taille`, `description`, `user_id`) VALUES
(1, 'TechAdvance', 'http://techadvance.com', '12 Rue de Rivoli, 75001 Paris', '0-10', 'TechAdvance est spécialisée dans le développement de solutions SaaS innovantes pour les entreprises.', 1),
(2, 'Innov&Boost', 'http://www.innovboost.com', '45 Avenue Foch, 69006 Lyon', '250-5000', 'Innov&Boost est une agence de conseil en marketing digital qui accompagne les entreprises dans leur transformation numérique.', 2),
(3, 'Comptabiliz', 'http://www.comptabiliz.fr', '23 Rue du Palais Gallien, 33000 Bordeaux', '10-250', 'Comptabiliz est un cabinet d\'expertise comptable spécialisé dans la gestion des finances et la fiscalité des entreprises.', 3),
(4, 'Okayo', 'http://www.okayo.fr', '78 Rue de Belleville, 75020 Paris', '0-10', 'Okayo est une entreprise spécialisée dans l\'édition de logiciels pour le secteur de l\'assurance, avec une approche innovante et humaine.', 4),
(5, 'FinTechOne', 'http://www.fintechone.fr', '100 Rue de la Paix, 75008 Paris', '250-5000', 'FinTechOne est un acteur majeur du secteur des services financiers numériques, proposant des solutions innovantes pour la gestion d’actifs.', 5),
(6, 'DataGenius', 'http://www.datagenius.com', '8 Rue de la République, 69001 Lyon', '+5000', 'DataGenius est une société spécialisée dans l\'analyse de données pour aider les entreprises à prendre des décisions éclairées grâce à la data science.', 6);

-- --------------------------------------------------------

--
-- Structure de la table `Particuliers`
--

CREATE TABLE `Particuliers` (
  `id` int(11) NOT NULL,
  `prenom` varchar(200) DEFAULT NULL,
  `nom` varchar(300) DEFAULT NULL,
  `telephone` varchar(300) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Particuliers`
--

INSERT INTO `Particuliers` (`id`, `prenom`, `nom`, `telephone`, `user_id`) VALUES
(1, 'Antoine', 'Ribeyre', '0607080910', 7),
(2, 'Amandine', 'Leduc', '0607080910', 8),
(3, 'Oriane', 'Coral', '0607080910', 9),
(6, 'Pierre', 'Dupont', '', 12),
(7, 'Admin', 'Admin', '0000000000', 13);

-- --------------------------------------------------------

--
-- Structure de la table `Utilisateurs`
--

CREATE TABLE `Utilisateurs` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_particulier` tinyint(1) NOT NULL,
  `is_entreprise` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `Utilisateurs`
--

INSERT INTO `Utilisateurs` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_particulier`, `is_entreprise`) VALUES
(1, 'pbkdf2_sha256$180000$jrqHaCP7caGS$TYdPunV3fQQsa8CWKpHMyMhZNT83sfK7LMqcgmuGPaM=', '2024-10-20 16:53:18.737825', 0, 'contact@techadvance.fr', '', '', 'contact@techadvance.fr', 0, 1, '2024-10-20 15:55:05.817941', 0, 1),
(2, 'pbkdf2_sha256$180000$flN538hIbmHL$pXzYXTuodXKwMhOmY0htU5/WTxSqF8116dPmrdemx1k=', '2024-10-20 16:05:03.343415', 0, 'contact@innovboost.fr', '', '', 'contact@innovboost.fr', 0, 1, '2024-10-20 16:04:51.188922', 0, 1),
(3, 'pbkdf2_sha256$180000$Cr9oeCSlfhrW$k7Ie5agNU1AxvcCmj5VQE+GD/z3b+vs7WMeHXGr3N1s=', '2024-10-20 16:08:00.375954', 0, 'contact@comptabiliz.fr', '', '', 'contact@comptabiliz.fr', 0, 1, '2024-10-20 16:07:49.566700', 0, 1),
(4, 'pbkdf2_sha256$180000$IFm1CYF2YVGe$qL9OZyana13Novm8TRhArnMe58gbFNHH4CXeLQcwVVg=', '2024-10-20 16:12:47.713387', 0, 'contact@okayo.fr', '', '', 'contact@okayo.fr', 0, 1, '2024-10-20 16:10:31.128222', 0, 1),
(5, 'pbkdf2_sha256$180000$Xse1cDVCoyZ1$v+HDTVc3711monkoVn+tMm6k4NA2bgfuW14w54xkQug=', '2024-10-20 16:15:27.853307', 0, 'contact@fintechone.fr', '', '', 'contact@fintechone.fr', 0, 1, '2024-10-20 16:15:17.828869', 0, 1),
(6, 'pbkdf2_sha256$180000$Jj9kod7uQ5N2$bfOTmOkFEnYVZlYvCHebch1TUSuoh7cMu3/EzEsKUhk=', '2024-10-20 16:17:47.205503', 0, 'contact@datagenius.fr', '', '', 'contact@datagenius.fr', 0, 1, '2024-10-20 16:17:29.614366', 0, 1),
(7, 'pbkdf2_sha256$180000$NSQ7baz372HV$yphvMOY61AtaA2qkVDMWr/6sX7J4Zt/ppLGhvY7MgcM=', '2024-10-20 17:48:33.257998', 0, 'ribeyre@epitech.eu', '', '', 'ribeyre@epitech.eu', 0, 1, '2024-10-20 16:32:05.076983', 1, 0),
(8, 'pbkdf2_sha256$180000$yvyu7VaLNhpT$OOTNnsQlKOfUFe0oUg1lFAI4ITa/B2Pz3l/FzGkTbTc=', '2024-10-20 16:36:34.490955', 0, 'leduc@epitech.eu', '', '', 'leduc@epitech.eu', 0, 1, '2024-10-20 16:32:34.374111', 1, 0),
(9, 'pbkdf2_sha256$180000$9WCcSRhS38CL$YvEXRQctwFltjrbDbVbABFoiEYnBRl0PPImTwrbD9ow=', '2024-10-20 16:35:45.554547', 0, 'coral@epitech.eu', '', '', 'coral@epitech.eu', 0, 1, '2024-10-20 16:33:27.367419', 1, 0),
(12, 'pbkdf2_sha256$180000$qb6JTLpwSB0P$oJFyzkVfAC4IPmAgGxiPliONUVQt3Si8WpE9DJ0tt68=', NULL, 0, 'pierre@gmail.com', '', '', 'pierre@gmail.com', 0, 1, '2024-10-20 17:38:27.945559', 1, 0),
(13, 'pbkdf2_sha256$180000$DPCuv593JRrB$C7p1y03f2XC6JJ9IebmkPDvZ39X37SoUMjypWB1Dotg=', NULL, 0, 'admin@gmail.com', '', '', 'admin@gmail.com', 0, 1, '2024-10-20 17:42:55.706065', 1, 0);

-- --------------------------------------------------------

--
-- Structure de la table `Utilisateurs_groups`
--

CREATE TABLE `Utilisateurs_groups` (
  `id` int(11) NOT NULL,
  `utilisateurs_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `Utilisateurs_user_permissions`
--

CREATE TABLE `Utilisateurs_user_permissions` (
  `id` int(11) NOT NULL,
  `utilisateurs_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Annonces`
--
ALTER TABLE `Annonces`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Annonces_entreprise_id_a68f8f20_fk` (`entreprise_id`);

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `Candidatures`
--
ALTER TABLE `Candidatures`
  ADD PRIMARY KEY (`id`),
  ADD KEY `Candidatures_annonce_id_40196dd5_fk` (`annonce_id`),
  ADD KEY `Candidatures_user_id_bcc0182f_fk` (`user_id`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Index pour la table `Entreprises`
--
ALTER TABLE `Entreprises`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `Particuliers`
--
ALTER TABLE `Particuliers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Index pour la table `Utilisateurs`
--
ALTER TABLE `Utilisateurs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Index pour la table `Utilisateurs_groups`
--
ALTER TABLE `Utilisateurs_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Utilisateurs_groups_utilisateurs_id_group_id_b640462c_uniq` (`utilisateurs_id`,`group_id`),
  ADD KEY `Utilisateurs_groups_group_id_8f414974_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `Utilisateurs_user_permissions`
--
ALTER TABLE `Utilisateurs_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Utilisateurs_user_permis_utilisateurs_id_permissi_a549d186_uniq` (`utilisateurs_id`,`permission_id`),
  ADD KEY `Utilisateurs_user_pe_permission_id_56367f31_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Annonces`
--
ALTER TABLE `Annonces`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT pour la table `Candidatures`
--
ALTER TABLE `Candidatures`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT pour la table `Entreprises`
--
ALTER TABLE `Entreprises`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `Particuliers`
--
ALTER TABLE `Particuliers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `Utilisateurs`
--
ALTER TABLE `Utilisateurs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `Utilisateurs_groups`
--
ALTER TABLE `Utilisateurs_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Utilisateurs_user_permissions`
--
ALTER TABLE `Utilisateurs_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Annonces`
--
ALTER TABLE `Annonces`
  ADD CONSTRAINT `Annonces_entreprise_id_a68f8f20_fk` FOREIGN KEY (`entreprise_id`) REFERENCES `Utilisateurs` (`id`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `Candidatures`
--
ALTER TABLE `Candidatures`
  ADD CONSTRAINT `Candidatures_annonce_id_40196dd5_fk` FOREIGN KEY (`annonce_id`) REFERENCES `Annonces` (`id`),
  ADD CONSTRAINT `Candidatures_user_id_bcc0182f_fk` FOREIGN KEY (`user_id`) REFERENCES `Utilisateurs` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `Utilisateurs` (`id`);

--
-- Contraintes pour la table `Entreprises`
--
ALTER TABLE `Entreprises`
  ADD CONSTRAINT `Entreprises_user_id_c4da7690_fk` FOREIGN KEY (`user_id`) REFERENCES `Utilisateurs` (`id`);

--
-- Contraintes pour la table `Particuliers`
--
ALTER TABLE `Particuliers`
  ADD CONSTRAINT `Particuliers_user_id_ec662bda_fk` FOREIGN KEY (`user_id`) REFERENCES `Utilisateurs` (`id`);

--
-- Contraintes pour la table `Utilisateurs_groups`
--
ALTER TABLE `Utilisateurs_groups`
  ADD CONSTRAINT `Utilisateurs_groups_group_id_8f414974_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `Utilisateurs_user_permissions`
--
ALTER TABLE `Utilisateurs_user_permissions`
  ADD CONSTRAINT `Utilisateurs_user_pe_permission_id_56367f31_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
