Explication des différents fichiers:
- Les fichiers CSV contiennent les jeux de données.
- Le fichier DB.txt contient les informations de connexion à la base de données.
- Le fichier SQL est utilisé pour créer la structure de la base de données et des tables.
- Le fichier requetes.py contient les requêtes permettant d'effectuer des opérations CRUD sur les tables.
- Le fichier trie_sql.py permet d'extraire les requêtes SQL à partir du fichier SQL pour créer les tables.
- Le fichier BD.py est responsable de la création de la base de données, des tables et de l'insertion des données à partir des fichiers CSV.
- Le fichier config.txt permet le bon fonctionnement de mako.
- Le dossier res contient tous les fichiers necéssaire à l'interface web (template, css, js).
- Le fichier Web.py est le fichier qui permet de créer la table et de lancer l'interface web.


Afin de lancer le programme, il suffit d'exécuter le fichier "Web.py" et de rentrer "http://127.0.0.1:8080" dans son navigateur.
Si vous rencontrez un problème de connexion à la base de données, vous pouvez modifier les identifiants dans le fichier "DB.txt".

Mise à jour : Ajout de la table "commentaire" et la table "login" qui contient l'identifiant du coach qui vas permettre de rajouter un commentaire (admin:admin).