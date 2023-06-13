# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686063801.5858722
_enable_loop = True
_template_filename = 'res/templates/affiche_les_stats.html'
_template_uri = 'affiche_les_stats.html'
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
        mesEtud = context.get('mesEtud', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<link rel="stylesheet" href="../css/style.css" >\r\n\r\n<h2>La statistique :</h2>\r\n<br>\r\n\r\n\r\n')
        for a in mesEtud :
            __M_writer('\t<div class="player"><h3>')
            __M_writer(str(a))
            __M_writer('</h3></div><br>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/affiche_les_stats.html", "uri": "affiche_les_stats.html", "source_encoding": "utf-8", "line_map": {"27": 0, "33": 1, "34": 8, "35": 9, "36": 9, "37": 9, "38": 11, "44": 38}}
__M_END_METADATA
"""
