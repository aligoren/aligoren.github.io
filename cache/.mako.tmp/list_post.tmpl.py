# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115070.759195
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/list_post.tmpl'
_template_uri = 'list_post.tmpl'
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
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
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
        posts = context.get('posts', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        date_format = context.get('date_format', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<article class="listpage">\n    <header>\n        <h1>')
        __M_writer(str(title))
        __M_writer('</h1>\n    </header>\n')
        if posts:
            __M_writer('    <ul class="postlist">\n')
            for post in posts:
                __M_writer('        <li><a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a> <time class="listdate" datetime="')
                __M_writer(str(post.date.isoformat()))
                __M_writer('" title="')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('">')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('</time></li>\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("No posts found.")))
            __M_writer('</p>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "list_post.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/list_post.tmpl", "line_map": {"64": 12, "65": 12, "66": 12, "67": 12, "68": 12, "69": 12, "70": 12, "71": 12, "72": 12, "73": 12, "74": 12, "75": 14, "76": 15, "77": 16, "78": 16, "79": 16, "80": 18, "86": 80, "26": 0, "37": 2, "42": 19, "48": 4, "58": 4, "59": 7, "60": 7, "61": 9, "62": 10, "63": 11}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
