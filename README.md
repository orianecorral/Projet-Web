# Jobfinder
1. Aperçu du projet :
À travers ce projet web, nous avons créé un job-board, Jobfinder qui permet de visualiser des offres de travail et ainsi pouvoir postuler à celles-ci.
Notre groupe de travail pour ce projet comprend Antoine Ribeyre, Ryan Mzalouat et Oriane Corral.
2. Fonctionnalités

A. Page principale

Jobfinder comprend une page principale où il est possible de rechercher des offres de travail selon des critères, par exemple, le titre du poste. Sur cette même page, un utilisateur peut se connecter à son compte qu'il soit représentant d'une entreprise ou un particulier à la recherche d'un poste.
Également,   un utilisateur qui  visite Jobfinder pour la première fois pourra créer son compte. L'inscription comprend un formulaire différent pour les particuliers et les entreprises.

B. Comptes
Pour les particuliers : 
Lorsqu'un particulier est connecté à son compte particulier, il peut avoir accès à ses informations personnelles en cliquant sur le bouton en haut à droite. Il peut ainsi les modifier ou même supprimer son compte. 
Le particulier peut aussi visualiser les annonces auxquelles il a candidaté.
Nous avons ajouté une fonctionnalité où un particulier peut candidater à une offre sans s'inscrire à Jobfinder. Cependant, ses informations ne seront pas pré remplies contrairement à un particulier qui a déjà son compte Jobfinder.
Pour les entreprises : 
Similaire au compte particulier, une entreprise peut modifier, supprimer, ses informations personnelles sur son profil. Une entreprise est l'unique entité qui peut créer une offre de travail et cela depuis son profil. 
Le professionnel peut accéder à toutes les offres d'emploi qui correspondent à son entreprise ainsi qu'à toutes les candidatures des particuliers à chacune des offres de travail. 

C. Admin
Nous avons implémenté une partie admin où un superuser est capable de créer des utilisateurs, c'est à dire un particulier ou une entreprise. 
Pour les utilisateurs qui sont déjà inscrits, l'admin peut modifier les informations personnelles de ceux-ci, cependant il ne pourra pas modifier l'email(l'identifiant) et son mot de passe. 
Du côté des annonces, le superuser peut créer, modifier et supprimer une offre de travail pour une entreprise.
Concernant les candidatures, l'admin peut modifier et même supprimer une candidature pour une annonce en particulier.
Un admin a accès à des tableaux représentatifs de la base de données et ses différents éléments comme les descriptions,les informations correspondant aux annonces etc. Cependant, l'admin n'a pas accès au tableau "Utilisateurs".

5. Technologies utilisées
Pour ce projet, nous avons fait le choix d'utiliser les technologies suivantes :
- Python comme langage principal 
- Django pour créer un lien entre la base de données et MySQL, ainsi que pour créer des vues. Nous avons utilisé les fonctionnalités intégrées de Django telles que forms, modelForm, AbstractUser, messages, authenticate.
- HTML/CSS pour le front-end
- Javascript pour créer une interactivité dynamique et la "responsivité" de la page web.
- MySQL/PhpMyAdmin pour gérer une base de données avec des primary keys et des foreign keys.

7. Structure du projet
├── jobfinder
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── jobfinder_admin
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   │   ├── connexion_admin.html
│   │   ├── editerannonce.html
│   │   ├── editerentreprise.html
│   │   ├── editer.html
│   │   ├── editeruser.html
│   │   ├── form_annonce.html
│   │   ├── form_entreprise.html
│   │   ├── form_user.html
│   │   ├── liste_candidature.html
│   │   └── Liste_utilisateur.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── jobfinder_app
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   │   ├── __init__.py:Zone.Identifier
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   │   ├── annonce_form.html
│   │   ├── compte_candidature_form.html
│   │   ├── connexion.html
│   │   ├── home_page.html
│   │   ├── inscription.html
│   │   ├── no_compte_candidature_form.html
│   │   └── update_annonce.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── jobfinder_compte
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __pycache__
│   ├── models.py
│   ├── __pycache__
│   ├── templates
│   │   ├── connexion_entreprise.html
│   │   ├── connexion_user.html
│   │   ├── entreprise_form.html
│   │   ├── entreprise_page.html
│   │   ├── remove-annonce.html
│   │   ├── remove-entreprise.html
│   │   ├── remove-particulier.html
│   │   ├── update_entreprise.html
│   │   ├── update_user.html
│   │   ├── user_form.html
│   │   └── user_page.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── static
    ├── css
    │   ├── con-inscr.css
    │   ├── style_form_01.css
    │   ├── style_form.css
    │   ├── style_home.css
    │   ├── style_main.css
    │   ├── style_pages_01.css
    │   └── style_pages.css
    ├── font
    │   ├── Quantify.ttf
    │   └── Quantify.ttf:Zone.Identifier
    ├── img
    │   ├── App-Store-logo.png
    │   ├── App-Store-logo.png:Zone.Identifier
    │   ├── instagram-logo.png
    │   ├── instagram-logo.png:Zone.Identifier
    │   ├── linkedin-logo.png
    │   ├── linkedin-logo.png:Zone.Identifier
    │   ├── Logo_dispo.png
    │   ├── Logo_Insta.png
    │   ├── Logo_LinkedIn.png
    │   ├── Logo_main.png
    │   ├── logo-play-store.png
    │   ├── logo-play-store.png:Zone.Identifier
    │   ├── logo-x.jpg
    │   ├── logo-x.jpg:Zone.Identifier
    │   ├── Logo_X.png
    │   └── Loupe.png
    └── new_css
        ├── style_admin.css
        ├── style_con-inscr.css
        ├── style_form.css
        ├── style_home.css
        ├── style_pages.css
        └── style_pyForm.css
9. Points d'amélioration
- Manque de visibilité sur la complexité du sujet avec un changement de technologies utilisées à partir de la fin de la première semaine de projet (uniquement Python à Python avec Django).
- Implémenter une RestAPI pour la base de données. 
11. Conclusion
