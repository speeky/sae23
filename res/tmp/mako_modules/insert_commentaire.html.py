# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686065917.098056
_enable_loop = True
_template_filename = 'res/templates/insert_commentaire.html'
_template_uri = 'insert_commentaire.html'
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
        type = context.get('type', UNDEFINED)
        message = context.get('message', UNDEFINED)
        com = context.get('com', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Modifier un commentaire</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n<form action="commentaire" method="POST" class="needs-validation" novalidate>\r\n  <div class="form-group">\r\n    <label for="minute">La minute de jeu :</label>\r\n    <input type="number" class="form-control" id="minute" placeholder="Entrez la minute de jeu" name="minute" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="commentaire">Le commentaire:</label>\r\n    <input type="text" class="form-control" id="commentaire" placeholder="Entrez le commentaire" name="commentaire" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="id">ID du match:</label>\r\n    <input type="number" class="form-control" id="id" placeholder="Entrez l\'ID du match" name="id" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Insérer</button>\r\n</form>\r\n<br>\r\n')
        for a in com :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/insert_commentaire.html", "uri": "insert_commentaire.html", "source_encoding": "utf-8", "line_map": {"27": 0, "35": 1, "36": 5, "37": 5, "38": 5, "39": 5, "40": 29, "41": 30, "42": 30, "43": 30, "49": 43}}
__M_END_METADATA
"""
