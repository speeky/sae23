# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686064974.7944782
_enable_loop = True
_template_filename = 'res/templates/supp_joueur.html'
_template_uri = 'supp_joueur.html'
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
        type = context.get('type', UNDEFINED)
        joueur = context.get('joueur', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<link rel="stylesheet" href="../css/style.css" >\r\n<h3>Suppression d\'un joueur par son numéro</h3>\r\n\r\n</pre>\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n\r\n<form action="suppressJoueur" method="POST">\r\n  <div class="form-group">\r\n    <label for="num">Numéro:</label>\r\n    <input type="number" class="form-control" placeholder="Numéro du joueur" name="num" id="num">\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Supprimer</button>\r\n</form>\r\n\r\n<br>\r\n\r\n<h3>Liste des joueurs :</h3>\r\n')
        for a in joueur :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/supp_joueur.html", "uri": "supp_joueur.html", "source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 6, "37": 6, "38": 6, "39": 6, "40": 20, "41": 21, "42": 21, "43": 21, "49": 43}}
__M_END_METADATA
"""
