# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686067707.3668237
_enable_loop = True
_template_filename = 'res/templates/insert_stat.html'
_template_uri = 'insert_stat.html'
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
        message = context.get('message', UNDEFINED)
        match = context.get('match', UNDEFINED)
        joueur = context.get('joueur', UNDEFINED)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Insertion d\'un d\'une statistique</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n<form action="insertStat" method="POST" class="needs-validation" novalidate>\r\n  <div class="form-group">\r\n    <label for="num_match">Numéro Match:</label>\r\n    <input type="number" class="form-control" id="num_match" placeholder="Entrer le numéro du match" name="num_match" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="num_joueur">Numéro du joueur:</label>\r\n    <input type="number" class="form-control" id="num_joueur" placeholder="Enter le numéro du joueur" name="num_joueur" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="presence">Présence:</label>\r\n    <input type="number" class="form-control" id="presence" placeholder="Présence ? (1=oui, 0=non)" name="presence" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="position">Position:</label>\r\n    <input type="text" class="form-control" id="position" placeholder="Position du joueur (demi, ailier, contre-pointe, pointe, gardien)" name="position" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="nb_but">Nombre de but:</label>\r\n    <input type="number" class="form-control" id="nb_but" placeholder="Nombre de but" name="nb_but" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="nb_faute">Nombre de faute:</label>\r\n    <input type="number" class="form-control" id="nb_faute" placeholder="Nombre de faute" name="nb_faute" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Insérer</button>\r\n</form>\r\n<br>\r\n\r\n<h3>Liste des matchs :</h3>\r\n')
        for a in match :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        __M_writer('\r\n<h3>Liste des joueurs :</h3>\r\n')
        for a in joueur :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insert_stat.html", "uri": "insert_stat.html", "source_encoding": "utf-8", "line_map": {"27": 0, "36": 1, "37": 5, "38": 5, "39": 5, "40": 5, "41": 49, "42": 50, "43": 50, "44": 50, "45": 52, "46": 54, "47": 55, "48": 55, "49": 55, "55": 49}}
__M_END_METADATA
"""
