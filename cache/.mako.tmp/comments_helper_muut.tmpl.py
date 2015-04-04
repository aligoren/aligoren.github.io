# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115071.320795
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/comments_helper_muut.tmpl'
_template_uri = 'comments_helper_muut.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_link_script', 'comment_form']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\n<script src="//cdn.muut.com/1/moot.min.js"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <a class="muut" href="https://muut.com/i/')
        __M_writer(str(comment_system_id))
        __M_writer('/')
        __M_writer(str(identifier))
        __M_writer('">')
        __M_writer(str(comment_system_id))
        __M_writer(' forums</a>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper_muut.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/comments_helper_muut.tmpl", "line_map": {"33": 7, "66": 60, "54": 3, "39": 11, "57": 4, "43": 11, "15": 0, "49": 3, "20": 2, "21": 5, "22": 8, "23": 13, "56": 4, "55": 4, "58": 4, "59": 4, "60": 4, "29": 7}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
