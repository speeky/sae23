import cherrypy
from mako.lookup import TemplateLookup
from requetes import *
from BD import *
bd()
table(sql_file)
inserte_joueur(csv_joueur)
inserte_match(csv_match)
inserte_csv(csv_participer)
inserte_stat(csv_stat)
inserte_login(csv_login)
inserte_commentaire(csv_commentaire)



mylookup = TemplateLookup(directories=['res/templates'], input_encoding='utf-8',
                          module_directory='res/tmp/mako_modules')

class InterfaceWebEtudiants(object):
    @cherrypy.expose
    def index(self):
        mytemplate = mylookup.get_template("index.html")
        return mytemplate.render()

    @cherrypy.expose
    def affiche(self):
        mytemplate = mylookup.get_template("affiche.html")
        return mytemplate.render(mesEtud=string_web(get_joueur()))

    @cherrypy.expose
    def aff_matchs(self):
        mytemplate = mylookup.get_template("aff_matchs.html")
        return mytemplate.render(mesEtud=stringm_web(get_matchs()))

    @cherrypy.expose
    def aff_match_victoire(self):
        mytemplate = mylookup.get_template("aff_match_victoire.html")
        return mytemplate.render(mesEtud=stringm_web(getParVictoire()))

    @cherrypy.expose
    def aff_commentaire(self):
        mytemplate = mylookup.get_template("aff_commentaire.html")
        return mytemplate.render(mesEtud=stringc_web(get_commentaire()))


    @cherrypy.expose
    def suppressJoueur(self, num=None):
        if num :
            try:
                deleteEtudiantByNumJoueur(num)
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = mylookup.get_template("supp_joueur.html")
        return mytemplate.render(message=message, type=typ, joueur=string_web(get_joueur()))

    @cherrypy.expose
    def suppressMatch(self, num=None):
        if num:
            try:
                deleteMatchByNum(num)
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = mylookup.get_template("supp_match.html")
        return mytemplate.render(message=message, type=typ, match=stringm_web(get_matchs()))

    @cherrypy.expose
    def suppressStat(self, num=None):
        affiche = stringS_web(getStat())
        if num:
            try:
                deleteStatByNum(num)
                message = "Suppression réussie !"
                typ = "success"
            except ValueError as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Veuillez remplir tous les champs."
            typ = "warning"
        mytemplate = mylookup.get_template("supp_stat.html")
        return mytemplate.render(message=message, type=typ, affiche=affiche)


    @cherrypy.expose
    def insertJoueur(self, prenom=None, nom=None, annee=None, poste=None):
        # le test suivant est rendu inutile par l'utilisation de javascript dans formulaire bootstrap
        if prenom and nom and annee and poste :
            print(annee, " -:- ", type(annee))
            try:
                insertEtudiant(prenom, nom, annee, poste)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert_joueur.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def insertMatch(self, adversaire=None, date=None, lieu=None, score_mon_equipe=None, score_adversaire=None, gagnant=None, saison=None):
        liste = ["0","1"]
        if adversaire and date and lieu and score_mon_equipe and score_adversaire and gagnant and saison :
            if gagnant not in liste:
                return "Veuillez remplir remplir le champ 'gagnant' correctement"
            else:
                try:
                    insertMatch(adversaire, date, lieu, score_mon_equipe, score_adversaire, gagnant, saison)
                    message = "Insertion réussie !"
                    typ = "success"
                except (Exception) as e:
                    message = str(e)
                    typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert_match.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def insertStat(self, num_joueur=None, num_match=None, presence=None, position=None, nb_but=None, nb_faute=None):
        if num_joueur and num_match and presence and position and nb_but and nb_faute:
            try:
                id = get_id_by_match_joueur(getParticiper(), int(num_match), int(num_joueur))
                if id is None:
                    inserte_participer(int(num_match), int(num_joueur))
                    id = get_id_by_match_joueur(getParticiper(), int(num_match), int(num_joueur))
                    if id is None:
                        raise Exception("Échec")
                insertStat(presence, position, nb_but, nb_faute, id)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert_stat.html")
        return mytemplate.render(message=message, type=typ, joueur=string_web(get_joueur()), match=stringm_web(get_matchs()))





    @cherrypy.expose
    def aff_annee(self, annee=None):
        if annee is None:
            mytemplate = mylookup.get_template("aff_annee.html")
            return mytemplate.render()
        else:
            mytemplate = mylookup.get_template("affiche.html")
            joueurs = string_web(getParAge(annee))
            return mytemplate.render(mesEtud=joueurs)

    @cherrypy.expose
    def aff_poste(self, poste=None):
        if poste is None:
            mytemplate = mylookup.get_template("aff_poste.html")
            return mytemplate.render()
        else:
            mytemplate = mylookup.get_template("affiche.html")
            joueurs = string_web(getParPoste(poste))
            return mytemplate.render(mesEtud=joueurs)

    @cherrypy.expose
    def aff_nom(self, nom=None, prenom=None):
        if nom is None:
            mytemplate = mylookup.get_template("aff_nom.html")
            return mytemplate.render()
        else:
            # Afficher la liste des joueurs en fonction de l'année
            mytemplate = mylookup.get_template("affiche.html")
            joueurs = string_web(getParNom(nom, prenom))
            return mytemplate.render(mesEtud=joueurs)

    @cherrypy.expose
    def aff_stat(self, num_match=None, num_joueur=None): # Pour les num match et numjoueur qui doit être les bonnes valeurs
        l_match = id_match()
        l_joueur = id_joueur()
        l_stat = id_stat()
        if num_match is None:
            mytemplate = mylookup.get_template("aff_stat.html")
            return mytemplate.render(joueur=string_web(get_joueur()), match=stringm_web(get_matchs()))
        else:
            if int(num_match) in l_match and int(num_joueur) in l_joueur:
                id = get_id_by_match_joueur(getParticiper(), int(num_match), int(num_joueur))
                print(id)
                if int(id) in l_stat:
                    mytemplate = mylookup.get_template("affiche_les_stats.html")
                    return mytemplate.render(mesEtud=stringS_web(getthestat(id)))
                else:
                    return "Aucune statistique pour les valeurs insérées"
            else:
                return "Veuillez remplir remplir le champ 'num_match' et 'num_joueur' correctement"

    @cherrypy.expose
    def aff_saison(self, saison=None):
        if saison is None:
            mytemplate = mylookup.get_template("aff_saison.html")
            return mytemplate.render()
        else:
            # Afficher la liste des joueurs en fonction de l'année
            mytemplate = mylookup.get_template("aff_matchs.html")
            match = stringm_web(getParSaison(saison))
            return mytemplate.render(mesEtud=match)

    @cherrypy.expose
    def login(self, login_str=None, mdp=None):
        if login_str is None:
            mytemplate = mylookup.get_template("aff_login.html")
            return mytemplate.render()
        else:
            if login(login_str, mdp):
                raise cherrypy.HTTPRedirect("/commentaire")
            else:
                return "Identifiants incorrects."

    @cherrypy.expose
    def commentaire(self, minute=None, commentaire=None, id=None):
        if minute and commentaire and id:
            try:
                inserteCommentaire(minute, commentaire, id)
                message = "Insertion réussie !"
                typ = "success"
            except Exception as e:  # Pas besoin des parenthèses après `Exception`
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("insert_commentaire.html")
        return mytemplate.render(message=message, type=typ, com=stringc_web(get_commentaire()))




    @cherrypy.expose
    def modifJoueur(self, prenom=None, nom=None, annee=None, poste=None, id=None):
        if prenom and nom and annee and poste and id:
            try:
                modifJoueur(prenom, nom, annee, poste, id)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("modif_joueur.html")
        return mytemplate.render(message=message, type=typ)



    @cherrypy.expose
    def modifMatch(self, adversaire=None, date=None, lieu=None, score_mon_equipe=None, score_adversaire=None, gagnant=None, saison=None, id=None):
        liste = ["0", "1"]
        if adversaire and date and lieu and score_mon_equipe and score_adversaire and gagnant and saison and id:
            if gagnant not in liste:
                return "Veuillez remplir remplir le champ 'gagnant' correctement"
            try:
                modifMatch(adversaire, date, lieu, score_mon_equipe, score_adversaire, gagnant, saison, id)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("modif_match.html")
        return mytemplate.render(message=message, type=typ)

    @cherrypy.expose
    def modifStat(self, presence=None, position=None, nb_but=None, nb_faute=None, id=None):
        liste = ["0", "1"]
        if presence and position and nb_but and nb_faute and id:
            if presence not in liste:
                return "Veuillez remplir remplir le champ 'gagnant' correctement"
            try:
                modifStat(presence, position, nb_but, nb_faute, id)
                message = "Insertion réussie !"
                typ = "success"
            except (Exception) as e:
                message = str(e)
                typ = "danger"
        else:
            message = "Tous les champs doivent être remplis !!"
            typ = "warning"
        mytemplate = mylookup.get_template("modif_stat.html")
        return mytemplate.render(message=message, type=typ, joueur=string_web(get_joueur()), match=stringm_web(get_matchs()))
