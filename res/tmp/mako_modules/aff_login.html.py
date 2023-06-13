# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686064955.0228183
_enable_loop = True
_template_filename = 'res/templates/aff_login.html'
_template_uri = 'aff_login.html'
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
        __M_writer('\r\n<h2>Insérer ses identifiants de coach pour pouvoir insérer</h2>\r\n<br>\r\n<form action="login" method="GET">\r\n  <div class="form-group">\r\n    <label for="login_str">Utilisateur :</label>\r\n    <input type="text" class="form-control" placeholder="Utilisateur" name="login_str" id="login_str" required>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="mdp">Mot de passe :</label>\r\n    <input type="text" class="form-control" placeholder="Mot de passe" name="mdp" id="mdp" required>\r\n  </div>\r\n\r\n  <button type="submit" class="btn btn-primary">Se connecter</button>\r\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/aff_login.html", "uri": "aff_login.html", "source_encoding": "utf-8", "line_map": {"27": 0, "32": 1, "38": 32}}
__M_END_METADATA
"""
