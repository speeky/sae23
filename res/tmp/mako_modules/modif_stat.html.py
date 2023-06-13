# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686065478.3320684
_enable_loop = True
_template_filename = 'res/templates/modif_stat.html'
_template_uri = 'modif_stat.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Modification d\'une statistique</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n<form action="modifStat" method="POST" class="needs-validation" novalidate>\r\n  <div class="form-group">\r\n    <label for="presence">Présence:</label>\r\n    <input type="number" class="form-control" id="presence" placeholder="Présence ? (1=oui, 0=non)" name="presence" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="position">Position:</label>\r\n    <input type="text" class="form-control" id="position" placeholder="Position du joueur (demi, ailier, contre-pointe, pointe, gardien)" name="position" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="nb_but">Nombre de but:</label>\r\n    <input type="number" class="form-control" id="nb_but" placeholder="Nombre de but" name="nb_but" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="nb_faute">Nombre de fautes:</label>\r\n    <input type="number" class="form-control" id="nb_faute" placeholder="Numéro" name="nb_faute" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="id">Numéro de la statistique:</label>\r\n    <input type="number" class="form-control" id="id" placeholder="Numéro" name="id" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Modifier</button>\r\n</form>\r\n<br>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/modif_stat.html", "uri": "modif_stat.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 5, "36": 5, "37": 5, "38": 5, "44": 38}}
__M_END_METADATA
"""
