# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686063540.772024
_enable_loop = True
_template_filename = 'res/templates/supp_stat.html'
_template_uri = 'supp_stat.html'
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
        affiche = context.get('affiche', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Suppression d\'une statistique par son numéro</h3>\r\n\r\n</pre>\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n\r\n <form action="suppressStat" method="POST">\r\n  <div class="form-group">\r\n    <label for="num">Numéro:</label>\r\n    <input type="number" class="form-control" placeholder="Numéro de la statistique" name="num" id="num">\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Supprimer</button>\r\n</form>\r\n\r\n<br>\r\n<h3>Liste des statistiques :</h3>\r\n')
        for a in affiche :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/supp_stat.html", "uri": "supp_stat.html", "source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 6, "37": 6, "38": 6, "39": 6, "40": 19, "41": 20, "42": 20, "43": 20, "44": 22, "50": 44}}
__M_END_METADATA
"""
