import pymysql


def get_joueur():
    requete = _requetes_joueur["getAll"]
    joueur = []
    for t in execute(requete):
        joueur.append(t)
    return joueur

def getParAge(annee) -> list :
    req = mkGetParAge(annee)
    return execute(req)

def getParPoste(poste) -> list :
    req = mkGetParPoste(poste)
    return execute(req)

def getParNom(nom, prenom):
    req = mkGetParNom(nom, prenom)
    return execute(req)


def insertEtudiant(prenom, nom, dateNaissance, poste) -> None :
    """ Insertion d'un étudiant dans la collection"""
    req = mkInsertRequestJoueur(prenom.capitalize(),nom.capitalize(),dateNaissance,poste)
    execute(req)


def deleteEtudiant(prenom : str, nom : str) -> None :
    """ Suppression d'un étudiant dans la collection
    On en supprime potentiellement plusieurs si le couple(prenom,nom) n'est pas unique!"""
    p = prenom.capitalize()
    n = nom.capitalize()
    req = mkDeleteRequest(p, n)
    execute(req)


def deleteEtudiantByNumJoueur(num : int) -> None :
    """ Suppression d'un étudiant dans la collection"""
    req = mkDeleteByNumRequestJoueur(num)
    execute(req)



def string_web(get):
    s= ''
    liste = []
    for etud in get:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 5:
            continue
        num = infos[0]
        nom = infos[1]
        prenom = infos[2]
        annee = infos[3]
        poste = infos[4]
        liste.append(f"Numéro: {num}, Nom: {nom}, Prénom: {prenom}, Année: {annee}, Poste: {poste}")
    return liste

def string(get):
    s= ''
    for etud in get:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 5:
            continue
        num = infos[0]
        nom = infos[1]
        prenom = infos[2]
        annee = infos[3]
        poste = infos[4]
        print(f"Numéro: {num}, Nom: {nom}, Prénom: {prenom}, Année: {annee}, Poste: {poste}")



def mkGetParAge(annee):
    s = _requetes_joueur["getAllParAge"].format(annee)
    return s

def mkGetParPoste(poste):
    s = _requetes_joueur["getAllParPoste"].format(poste)
    return s

def mkGetParNom(nom, prenom):
    s = _requetes_joueur["getByNom"].format(nom.capitalize(), prenom.capitalize())
    return s

def mkInsertRequestJoueur(prenom, nom, annee, poste):
    s = _requetes_joueur["insert"].format(prenom.capitalize(), nom.capitalize(), annee, poste)
    return s


def mkDeleteRequest(prenom, nom):
    s = _requetes_joueur["delete"].format(nom.upper(), prenom.capitalize())
    return s


def mkDeleteByNumRequestJoueur(num):
    s = _requetes_joueur["deleteByNum"].format(num)
    return s

_requetes_joueur = {
    "getAll" : "select * from joueur order by id_joueur;",
    "getAllParAge" : "select * from joueur where année_naissance = {};",
    "getAllParPoste" : "select * from joueur where poste = '{}';",
    "getByNom" : "select * from joueur where nom = '{}' and prénom = '{}';",
    "insert" : "insert into joueur (prénom,nom,année_naissance,poste) values ('{}','{}','{}','{}');",
    "delete" : "delete from joueur where nom = '{}' and prénom = '{}';" ,
    "deleteByNum" : "delete from joueur where id_joueur = {};" }



from BD import dbConnect

def execute(req : str) :    # type de valeur rendu variable :-(
    _dbEtudiant, _cursorEtudiant = dbConnect()
    res = _cursorEtudiant.execute(req)
    if "select" in req :
        res = _cursorEtudiant.fetchall()
    else :
        _dbEtudiant.commit()
    return res

def date(req):
    matchs = []
    for t in execute(req):
        matchs.append(t)
    new_data = []
    for row in matchs:
        new_row = list(row)
        new_row[2] = new_row[2].strftime('%d-%m-%y')
        new_data.append(new_row)
    return new_data

def stringm_web(get):
    A = tuple(tuple(x) for x in get)
    s = ''
    liste = []
    for etud in A:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 8:
            continue
        num = infos[0]
        adversaire = infos[1]
        date_match = infos[2]
        lieu = infos[3]
        score_cna = infos[4]
        score_adverse = infos[5]
        cna_gagnant = infos[6]
        if cna_gagnant == '1':
            cna_gagnant = "CNA"
        elif cna_gagnant == '0':
            cna_gagnant = adversaire
        saison = infos[7]
        liste.append(f"Numéro: {num}, Adversaire: {adversaire}, Date: {date_match}, Lieu: {lieu}, Score CNA: {score_cna}, Score {adversaire}: {score_adverse}, Vainqueur: {cna_gagnant}, Saison: {saison}")
    return liste

def stringm(get):
    A = tuple(tuple(x) for x in get)
    s = ''
    for etud in A:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 8:
            continue
        num = infos[0]
        adversaire = infos[1]
        date_match = infos[2]
        lieu = infos[3]
        score_cna = infos[4]
        score_adverse = infos[5]
        cna_gagnant = infos[6]
        if cna_gagnant == '1':
            cna_gagnant = "CNA"
        elif cna_gagnant == '0':
            cna_gagnant = adversaire
        saison = infos[7]
        print(f"Numéro: {num}, Adversaire: {adversaire}, Date: {date_match}, Lieu: {lieu}, Score CNA: {score_cna}, Score {adversaire}: {score_adverse}, Vainqueur: {cna_gagnant}, Saison: {saison}")

def stringc_web(get):
    A = tuple(tuple(x) for x in get)
    s = ''
    liste = []
    for etud in A:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 3:
            continue
        num = infos[0]
        minute = infos[1]
        comment = infos[2]
        liste.append(f"Numéro: {num}, Minute: {minute}, Commentaire: {comment}")
    return liste

def com(req):
    matchs = []
    for t in execute(req):
        matchs.append(t)
    return matchs

def get_matchs():
    requete = _requetes_match["getAll"]
    return date(requete)

def get_commentaire():
    requete = _requetes_match["getCommentaire"]
    return com(requete)

def getParVictoire() -> list :
    req = _requetes_match["getVictoire"]
    return date(req)

def getParSaison(saison) -> list :
    req = mkGetSaison(saison)
    return date(req)



def insertMatch(adversaire,date,lieu,score_mon_equipe,score_adversaire,gagnant,saison) -> None :
    req = mkInsertRequestMatch(adversaire.capitalize(),date,lieu.capitalize(),score_mon_equipe,score_adversaire,gagnant,saison)
    execute(req)


def deleteMatchByNum(num : int) -> None :
    req = mkDeleteByNumRequestMatch(num)
    execute(req)


def mkInsertRequestMatch(adversaire,date,lieu,score_mon_equipe,score_adversaire,gagnant,saison):
    s = _requetes_match["insert"].format(adversaire.capitalize(), date, lieu.capitalize(), score_mon_equipe, score_adversaire, gagnant, saison)
    return s

def mkGetSaison(saison):
    s = _requetes_match["getSaison"].format(saison)
    return s

def mkDeleteByNumRequestMatch(num):
    s = _requetes_match["deleteByNum"].format(num)
    return s



_requetes_match = {
    "getAll" : "select * from matchs;",
    "getCommentaire" : "select * from commentaire;",
    "getVictoire" : "select * from matchs where gagnant = 1;",
    "getSaison" : "select * from matchs where saison = '{}'",
    "insert" : "insert into matchs (adversaire,date,lieu,score_mon_equipe,score_adversaire,gagnant,saison) values ('{}','{}','{}','{}','{}','{}','{}');",
    "deleteByNum" : "delete from matchs where id_match = {};" }



from BD import dbConnect

def stringS_web(get):
    s= ''
    liste = []
    for etud in get:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 5:
            continue
        num = infos [0]
        presence = infos[1]
        if presence == '1':
            presence = "Présent"
        elif presence == '0':
            presence = "Absent"
        position = infos[2]
        nb_but = infos[3]
        nb_faute = infos[4]
        liste.append(f"Numéro: {num}, {presence}, Position: {position}, Nombre de buts: {nb_but}, Nombre de fautes: {nb_faute}")
    return liste

def stringS(get):
    s= ''
    for etud in get:
        s = s + str(etud) + "\n"
    s = s.replace("(", "").replace(")", "").replace("'", "")
    personnes = s.split("\n")
    for personne in personnes:
        infos = personne.split(", ")
        if len(infos) < 5:
            continue
        num = infos [0]
        presence = infos[1]
        if presence == '1':
            presence = "Présent"
        elif presence == '0':
            presence = "Absent"
        position = infos[2]
        nb_but = infos[3]
        nb_faute = infos[4]
        print(f"Numéro: {num}, {presence}, Position: {position}, Nombre de buts: {nb_but}, Nombre de fautes: {nb_faute}")



def execute(req : str) :    # type de valeur rendu variable :-(
    _dbEtudiant, _cursorEtudiant = dbConnect()
    res = _cursorEtudiant.execute(req)
    if "select" in req :
        res = _cursorEtudiant.fetchall()
    else :
        _dbEtudiant.commit()
    return res


def getParticiper():
    requete = _requetes_global["getParticiper"]
    participation = []
    for t in execute(requete):
        participation.append(t)
    return participation

def inserte_participer(match, joueur):
    req = mkInserteParticiper(match, joueur)
    execute(req)

def mkInserteParticiper(match, joueur):
    s = _requetes_global["inserteParticiper"].format(match, joueur)
    return s


def getStat():
    requete = _requetes_global["getStat"]
    stat =  []
    for t in execute(requete):
        stat.append(t)
    return stat

def insertStat(presence,position, nb_but, nb_faute, id_participer):
    req = mkInserteStat(presence,position, nb_but, nb_faute, id_participer)
    execute(req)

def deleteStatByNum(num : int) -> None :
    req = mkDeleteStat(num)
    execute(req)

def getthestat(num : int) -> None :
    requete = mkgetstat(num)
    return execute(requete)


def deleteParticiperByNum(num : int) -> None :
    req = mkDeleteParticiper(num)
    execute(req)

def mkInserteStat(presence,position, nb_but, nb_faute, id_participer):
    s = _requetes_global["inserteStat"].format(presence, position, nb_but, nb_faute, id_participer)
    return s

def mkDeleteStat(num):
    s = _requetes_global["deleteStat"].format(num)
    return s

def mkgetstat(num):
    s = _requetes_global["gettheStat"].format(num)
    return s

def mkDeleteParticiper(num):
    s = _requetes_global["deleteParticiper"].format(num)
    return s

def get_id_by_match_joueur(A, match, joueur):
    for tup in A:
        if tup[1] == match and tup[2] == joueur:
            return tup[0]
    return None



def login(login_str, mdp):
    req = mklogin(login_str, mdp)
    if execute(req) == 1:
        return True
    else:
        return False


def mklogin(login_str, mdp):
    s = _requetes_global["login"].format(login_str, mdp)
    return s



def inserteCommentaire(minute, commentaire, id_match):
    req = mkcommentaire(minute, commentaire, id_match)
    execute(req)

def mkcommentaire(minute, commentaire, id_match):
    s = _requetes_global["inserteCommentaire"].format(minute, commentaire, id_match)
    return s






_requetes_global = {
    "getParticiper" : "select * from participer order by id_participer;",
    "inserteParticiper" : "insert into participer (id_match, id_joueur) values ({},{});",
    "inserteCommentaire" : "INSERT INTO `commentaire` (`id_commentaire`, `minute`, `commentaire`, `id_match`) VALUES (NULL, '{}', '{}', '{}');",
    "getStat" : "select * from statistique_joueur order by id_stat",
    "gettheStat" : "select * from statistique_joueur where id_participer = {}",
    "inserteStat" : "insert into statistique_joueur (présence,position, nb_but, nb_faute, id_participer) values ('{}', '{}', '{}', '{}', '{}');",
    "deleteStat" : "delete from statistique_joueur where id_stat = {};",
    "login" : "SELECT * FROM `login` WHERE `login` LIKE '{}' AND `mdp` LIKE '{}'",
    "deleteParticiper" : "delete from participer where id_participer = {};"}








def modifMatch(adversaire,date,lieu,score_mon_equipe,score_adversaire,gagnant,saison,id_match) -> None :
    req = mkModifMatch(adversaire.capitalize(),date,lieu.capitalize(),score_mon_equipe,score_adversaire,gagnant,saison,id_match)
    execute(req)
def mkModifMatch(adversaire,date,lieu,score_mon_equipe,score_adversaire,gagnant,saison, id_match):
    s = _requetes_modif["match"].format(adversaire.capitalize(), date, lieu.capitalize(), score_mon_equipe, score_adversaire, gagnant, saison, id_match)
    return s



def modifJoueur(nom, prenom, annee, poste, id_joueur) -> None :
    req = mkModifJoueur(nom.capitalize(),prenom.capitalize(),annee,poste, id_joueur)
    execute(req)
def mkModifJoueur(nom, prenom, annee, poste, id_joueur):
    s = _requetes_modif["joueur"].format(nom.capitalize(), prenom.capitalize(), annee, poste, id_joueur)
    return s






def modifStat(presence,position, nb_but, nb_faute, id_stat):
    req = mkModifStat(presence,position, nb_but, nb_faute, id_stat)
    execute(req)
def mkModifStat(presence,position, nb_but, nb_faute, id_stat):
    s = _requetes_modif["stat"].format(presence, position, nb_but, nb_faute, id_stat)
    return s




_requetes_modif = {
    "match" : "UPDATE `matchs` SET `adversaire` = '{}', `date` = '{}', `lieu` = '{}', `score_mon_equipe` = '{}', `score_adversaire` = '{}', `gagnant` = '{}', `saison` = '{}' WHERE `matchs`.`id_match` = {};",
    "joueur" : "UPDATE `joueur` SET `nom` = '{}', `prénom` = '{}', `année_naissance` = '{}', `poste` = '{}' WHERE `joueur`.`id_joueur` = {};",
    "stat" : "UPDATE `statistique_joueur` SET `présence` = '{}', `position` = '{}', `nb_but` = '{}', `nb_faute` = '{}' WHERE `statistique_joueur`.`id_stat` = {};"}


def execute(req : str) :    # type de valeur rendu variable :-(
    _dbEtudiant, _cursorEtudiant = dbConnect()
    res = _cursorEtudiant.execute(req)
    if "select" in req :
        res = _cursorEtudiant.fetchall()
    else :
        _dbEtudiant.commit()
    return res



def id_match():
    liste = []
    for i in get_matchs():
        liste.append(i[0])
    return liste

def id_joueur():
    liste = []
    for i in get_joueur():
        liste.append(i[0])
    return liste

def id_stat():
    liste = []
    for i in getStat():
        liste.append(i[5])
    return liste