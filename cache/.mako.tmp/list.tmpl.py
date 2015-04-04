# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115071.008795
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


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
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n')
        if items:
            __M_writer('    <ul class="postlist">\n')
            for text, link in items:
                __M_writer('        <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("Nothing found.")))
            __M_writer('</p>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "list.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/list.tmpl", "line_map": {"64": 12, "65": 12, "66": 12, "67": 14, "68": 15, "69": 16, "70": 16, "71": 16, "72": 18, "78": 72, "26": 0, "36": 2, "41": 19, "47": 4, "56": 4, "57": 7, "58": 7, "59": 9, "60": 10, "61": 11, "62": 12, "63": 12}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
