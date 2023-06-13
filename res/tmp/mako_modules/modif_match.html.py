# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1686067584.2731776
_enable_loop = True
_template_filename = 'res/templates/modif_match.html'
_template_uri = 'modif_match.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<h3>Insertion d\'un match</h3>\r\n\r\n<p class="message alert alert-')
        __M_writer(str(type))
        __M_writer('">')
        __M_writer(str(message))
        __M_writer('</p>\r\n\r\n<form action="modifMatch" method="POST" class="needs-validation" novalidate>\r\n  <div class="form-group">\r\n    <label for="adversaire">Adversaire:</label>\r\n    <input type="text" class="form-control" id="adversaire" placeholder="Entrer le club adverse" name="adversaire" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="date">Date:</label>\r\n    <input type="date" class="form-control" id="date" placeholder="Enter la date (année-mois-jour)" name="date" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="lieu">Lieu:</label>\r\n    <input type="text" class="form-control" id="lieu" placeholder="Lieu de la rencontre" name="lieu" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="score_mon_equipe">Score CNA:</label>\r\n    <input type="number" class="form-control" id="score_mon_equipe" placeholder="Score CNA" name="score_mon_equipe" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="score_adversaire">Score Adverse:</label>\r\n    <input type="number" class="form-control" id="score_adversaire" placeholder="Adverse" name="score_adversaire" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <div class="form-group">\r\n    <label for="gagnant">CNA gagnant ?:</label>\r\n    <input type="number" class="form-control" id="gagnant" placeholder="CNA gagnant (1=oui, 0=non)" name="gagnant" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n\r\n  <div class="form-group">\r\n    <label for="saison">Saison:</label>\r\n    <input type="text" class="form-control" id="saison" placeholder="Saison" name="saison" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n\r\n    <div class="form-group">\r\n    <label for="id">Numéro du match:</label>\r\n    <input type="number" class="form-control" id="id" placeholder="Numéro du match" name="id" required>\r\n    <div class="valid-feedback">Valid.</div>\r\n    <div class="invalid-feedback">Remplir ce champ, SVP!</div>\r\n  </div>\r\n  <button type="submit" class="btn btn-primary">Modifier</button>\r\n</form>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "res/templates/modif_match.html", "uri": "modif_match.html", "source_encoding": "utf-8", "line_map": {"27": 0, "34": 1, "35": 5, "36": 5, "37": 5, "38": 5, "44": 38}}
__M_END_METADATA
"""
