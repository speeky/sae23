# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686064094.0749068
_enable_loop = True
_template_filename = 'res/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'template.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n<br>\r\n<center><h3 class="center">Règles du Water Polo :</h3></center><br>\r\n<h5>Le water-polo est un sport aquatique qui oppose deux équipes de sept joueurs chacune (six joueurs de champ et un gardien de but) dans une piscine. L\'objectif du jeu est de marquer plus de buts que l\'équipe adverse en lançant un ballon dans le but de l\'équipe adverse.\r\n <br>\r\nVoici les règles principales du water-polo :\r\n    <br> <br>\r\n\r\n<u><b>Buts :</b></u> Chaque équipe a un but de 3 mètres de large et 0,9 mètre de haut. Le but est défendu par le gardien de but qui peut utiliser ses mains pour bloquer les tirs adverses.\r\n<br><br>\r\n<u><b>Durée du match :</b></u> Un match de water-polo est généralement divisé en quatre périodes de 7 à 8 minutes chacune, avec une pause de deux minutes entre chaque période. En cas d\'égalité à la fin du temps réglementaire, des prolongations peuvent être jouées.\r\n<br><br>\r\n<u><b>Possession de la balle :</b></u> Les joueurs utilisent leurs mains pour passer, lancer et attraper le ballon. Ils peuvent se déplacer dans l\'eau en nageant, en utilisant des mouvements de jambes et en effectuant des passes à leurs coéquipiers. Le ballon ne peut pas être tenu avec les deux mains simultanément, à moins que le joueur ne soit immobile.\r\n<br><br>\r\n<u><b>Fautes et sanctions :</b></u> Le water-polo est un sport physique et les contacts sont autorisés, mais il existe des règles strictes sur les types de contact autorisés. Les fautes courantes comprennent la poussée, la retenue, le tirage de maillot, l\'interférence et le jeu brutal. Les fautes sont sanctionnées par des exclusions temporaires (où le joueur fautif doit quitter le jeu pendant 20 à 30 secondes) ou des exclusions permanentes (où le joueur doit quitter le jeu pour le reste de la partie).\r\n<br><br>\r\n<u><b>Coups francs :</b></u> Lorsqu\'une faute est commise, l\'équipe adverse obtient un coup franc. Le coup franc est exécuté à l\'endroit de la faute ou à l\'endroit où le ballon était lorsque la faute a été commise. Les joueurs adverses doivent se trouver à une certaine distance du tireur lors de l\'exécution du coup franc.\r\n<br><br>\r\n<u><b>Hors-jeu :</b></u> Les règles du hors-jeu dans le water-polo sont similaires à celles du football. Un joueur est hors-jeu s\'il est plus près du but adverse que le ballon et n\'est pas en train de nager pour revenir en position de jeu.\r\n<br><br>\r\n<u><b>Temps d\'attaque :</b></u> Chaque équipe dispose d\'un temps limité pour tenter de marquer un but une fois qu\'elle a récupéré la possession de la balle. Ce temps d\'attaque est généralement de 30 secondes, et si une équipe ne parvient pas à tirer au but dans ce laps de temps, elle perd la possession et l\'autre équipe obtient la balle.\r\n<br><br>\r\nCes règles fournissent une base pour comprendre le water-polo, mais il existe également des règles plus spécifiques et des stratégies avancées qui peuvent être mises en œuvre par les équipes. Le water-polo est un sport rapide, physique et exigeant, qui nécessite une grande condition physique, une coordination et une habileté dans l\'eau.\r\n</h5>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "33": 2, "39": 33}}
__M_END_METADATA
"""
