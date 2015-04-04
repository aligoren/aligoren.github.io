# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115070.993195
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/annotation_helper.tmpl'
_template_uri = 'annotation_helper.tmpl'
_source_encoding = 'ascii'
_exports = ['css', 'code']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <link rel="stylesheet" href="http://assets.annotateit.org/annotator/v1.2.5/annotator.min.css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_code(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n    <script src="http://code.jquery.com/jquery-migrate-1.2.1.js"></script>\n    <script src="http://assets.annotateit.org/annotator/v1.2.7/annotator-full.js"></script>\n    <script>\n    jQuery(function ($) {\n        $(\'body\').annotator().annotator(\'setupPlugins\', {}, {\n            // Disable filter bar\n            Filter: false\n        });\n    });\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "annotation_helper.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/annotation_helper.tmpl", "line_map": {"20": 3, "21": 16, "15": 0, "41": 5, "27": 1, "37": 5, "47": 41, "31": 1}, "source_encoding": "ascii"}
__M_END_METADATA
"""
