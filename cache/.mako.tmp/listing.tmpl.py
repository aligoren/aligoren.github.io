# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115071.539196
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/listing.tmpl'
_template_uri = 'listing.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'sourcelink']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        code = _import_ns.get('code', context.get('code', UNDEFINED))
        files = _import_ns.get('files', context.get('files', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def content():
            return render_content(context)
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if folders or files:
            __M_writer('<ul class="list-unstyled">\n')
            for name in folders:
                __M_writer('    <li><a href="')
                __M_writer(str(name))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i> ')
                __M_writer(str(name))
                __M_writer('</a>\n')
            for name in files:
                __M_writer('    <li><a href="')
                __M_writer(str(name))
                __M_writer('.html"><i class="glyphicon glyphicon-file"></i> ')
                __M_writer(str(name))
                __M_writer('</a>\n')
            __M_writer('</ul>\n')
        if code:
            __M_writer('    ')
            __M_writer(str(code))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        source_link = _import_ns.get('source_link', context.get('source_link', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if source_link:
            __M_writer('    <li>\n    <a href="')
            __M_writer(str(source_link))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\n    </li>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "listing.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/listing.tmpl", "line_map": {"22": 3, "76": 5, "77": 6, "78": 6, "79": 7, "80": 8, "81": 9, "82": 10, "83": 10, "84": 10, "85": 10, "86": 10, "87": 12, "88": 13, "89": 13, "90": 13, "91": 13, "28": 0, "93": 15, "94": 17, "95": 18, "96": 18, "97": 18, "116": 25, "103": 22, "92": 13, "46": 2, "47": 3, "113": 22, "114": 23, "115": 24, "52": 20, "117": 25, "118": 25, "119": 25, "57": 28, "125": 119, "63": 5}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
