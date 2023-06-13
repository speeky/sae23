# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686063566.8385959
_enable_loop = True
_template_filename = 'res/templates/aff_stat.html'
_template_uri = 'aff_stat.html'
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
        joueur = context.get('joueur', UNDEFINED)
        match = context.get('match', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Afficher une statistique</h2>\r\n<br>\r\n<form action="aff_stat" method="GET">\r\n  <div class="form-group">\r\n    <label for="num_match">Numéro match:</label>\r\n    <input type="number" class="form-control" placeholder="Numéro du match" name="num_match" id="num_match" required>\r\n  </div>\r\n  <div class="form-group">\r\n        <label for="num_joueur">Numéro joueur :</label>\r\n        <input type="number" class="form-control" placeholder="Numéro du joueur" name="num_joueur" id="num_joueur" required>\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Afficher</button>\r\n</form>\r\n\r\n\r\n<br>\r\n<h3>Liste des joueurs :</h3>\r\n')
        for a in joueur :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        __M_writer('\r\n\r\n\r\n<h3>Liste des matchs :</h3>\r\n')
        for a in match :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/aff_stat.html", "uri": "aff_stat.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 19, "36": 20, "37": 20, "38": 20, "39": 22, "40": 26, "41": 27, "42": 27, "43": 27, "49": 43}}
__M_END_METADATA
"""
