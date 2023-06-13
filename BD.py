import pymysqlimport csvfrom trie_sql import trie_create, trie_altersql_file = "sae.sql"csv_joueur = "joueur.csv"csv_match = "match.csv"csv_participer = "participer.csv"csv_stat = "stat.csv"csv_login = "login.csv"csv_commentaire = "commentaire.csv"def getParamsConnexion() -> tuple:    base = 'etudiants'    serveur = "localhost"    utilisateur = "root"    mdp = ""    numPort = 3306     # port MySQL standard (par défaut)    try :        with open("DB.txt") as f :            for ligne in f :                if len(ligne)<5 or ligne[0] == '#' :                    continue                champs = ligne.split(':')                if 'nombase' in champs[0] :                    base = champs[1].strip()                elif 'host' in champs[0] :                    serveur = champs[1].strip()                elif 'user' in champs[0] :                    utilisateur = champs[1].strip()                elif 'pass' in champs[0] :                    mdp = champs[1].strip()                elif 'port' in champs[0] and len(champs[1].strip()) < 3 :          # pas obligatoire!                    numPort = int(champs[1].strip())    except FileNotFoundError as e :        print("'configDB.txt' absent, utilisation des valeurs par défaut")    return (serveur,utilisateur,mdp,base,numPort)def dbConnect():    s, u, m, b, p = getParamsConnexion()    db = pymysql.connect(host=s, charset="utf8", user=u, passwd=m, db=b, port=p)    return (db, db.cursor())def serveurConnect():    s,u,m,b,p = getParamsConnexion()    db = pymysql.connect(host=s, charset="utf8", user=u, passwd=m, port=p)    return (db,db.cursor())def bd():    __db, __cursor = serveurConnect()    __cursor.execute("CREATE DATABASE IF NOT EXISTS sae")    __db.commit()    __cursor.close()    __db.close()def table(sql_file):    create = trie_create(sql_file)    alter = trie_alter(sql_file)    try:        _db, _cursor = dbConnect()        for i in create:            _cursor.execute(i)        for y in alter:            _cursor.execute(y)        _db.commit()        _cursor.close()        _db.close()    except pymysql.err.OperationalError as e:        if '1826' in str(e):            passdef inserte_joueur(csv_joueur):    with open(csv_joueur, mode='r', encoding='utf-8') as fichier_csv:        lecteur_csv = csv.reader(fichier_csv, delimiter=',')        _db, _cursor = dbConnect()        for ligne in lecteur_csv:            id, nom, prénom, annee, poste = ligne            s = f"INSERT INTO joueur (`id_joueur`, `nom`, `prénom`, `année_naissance`, `poste`) VALUES ({id},'{nom}','{prénom}',{annee},'{poste}')"            try:                _cursor.execute(s)                _db.commit()            except pymysql.IntegrityError:                _db.rollback()def inserte_match(csv_match):    with open(csv_match, mode='r', encoding='utf-8') as fichier_csv:        lecteur_csv = csv.reader(fichier_csv, delimiter=',')        _db, _cursor = dbConnect()        for ligne in lecteur_csv:            id, adversaire, date, lieu, score_mon_equipe, score_adversaire, gagnant, saison = ligne            s = f"INSERT INTO matchs (`id_match`, `adversaire`, `date`, `lieu`, `score_mon_equipe`, `score_adversaire`, `gagnant`, `saison`) VALUES ({id},'{adversaire}','{date}','{lieu}',{score_mon_equipe},{score_adversaire}, {gagnant}, '{saison}' )"            try:                _cursor.execute(s)                _db.commit()            except pymysql.IntegrityError:                _db.rollback()def inserte_csv(csv_participer):    with open(csv_participer, mode='r', encoding='utf-8') as fichier_csv:        lecteur_csv = csv.reader(fichier_csv, delimiter=',')        _db, _cursor = dbConnect()        for ligne in lecteur_csv:            id, idm, idj = ligne            s = f"INSERT INTO participer (`id_participer`, `id_match`, `id_joueur`) VALUES ({id},{idm},{idj})"            try:                _cursor.execute(s)                _db.commit()            except pymysql.IntegrityError:                _db.rollback()def inserte_stat(csv_stat):    with open(csv_stat, mode='r', encoding='utf-8') as fichier_csv:        lecteur_csv = csv.reader(fichier_csv, delimiter=',')        _db, _cursor = dbConnect()        for ligne in lecteur_csv:            id, présence, position, nb_but, nb_faute, idp = ligne            if position == 'NULL':                s = f"INSERT INTO statistique_joueur (`id_stat`, `présence`, `position`, `nb_but`, `nb_faute`, `id_participer`) VALUES ({id},{présence},{position},{nb_but},{nb_faute}, {idp})"            else:                s = f"INSERT INTO statistique_joueur (`id_stat`, `présence`, `position`, `nb_but`, `nb_faute`, `id_participer`) VALUES ({id},{présence},'{position}',{nb_but},{nb_faute}, {idp})"            try:                _cursor.execute(s)                _db.commit()            except pymysql.IntegrityError:                _db.rollback()def inserte_login(csv_login):    with open(csv_login, mode='r', encoding='utf-8') as fichier_csv:        lecteur_csv = csv.reader(fichier_csv, delimiter=',')        _db, _cursor = dbConnect()        for ligne in lecteur_csv:            id, login, mdp = ligne            s = f"INSERT INTO `login` (`id_login`, `login`, `mdp`) VALUES ({id},'{login}','{mdp}')"            try:                _cursor.execute(s)                _db.commit()            except pymysql.IntegrityError:                _db.rollback()def inserte_commentaire(csv_commentaire):    with open(csv_commentaire, mode='r', encoding='utf-8') as fichier_csv:        lecteur_csv = csv.reader(fichier_csv, delimiter=',')        _db, _cursor = dbConnect()        for ligne in lecteur_csv:            id, minute, commentaire, id_match = ligne            s = f"INSERT INTO `commentaire` (`id_commentaire`, `minute`, `commentaire`, `id_match`) VALUES ({id},'{minute}','{commentaire}','{id_match}')"            try:                _cursor.execute(s)                _db.commit()            except pymysql.IntegrityError:                _db.rollback()