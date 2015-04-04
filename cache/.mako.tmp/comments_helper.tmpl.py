# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115071.180395
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/comments_helper.tmpl'
_template_uri = 'comments_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['comment_link', 'comment_link_script', 'comment_form']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('isso', context._clean_inheritance_tokens(), templateuri='comments_helper_isso.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'isso')] = ns

    ns = runtime.TemplateNamespace('muut', context._clean_inheritance_tokens(), templateuri='comments_helper_muut.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'muut')] = ns

    ns = runtime.TemplateNamespace('googleplus', context._clean_inheritance_tokens(), templateuri='comments_helper_googleplus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'googleplus')] = ns

    ns = runtime.TemplateNamespace('intensedebate', context._clean_inheritance_tokens(), templateuri='comments_helper_intensedebate.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'intensedebate')] = ns

    ns = runtime.TemplateNamespace('facebook', context._clean_inheritance_tokens(), templateuri='comments_helper_facebook.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'facebook')] = ns

    ns = runtime.TemplateNamespace('livefyre', context._clean_inheritance_tokens(), templateuri='comments_helper_livefyre.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'livefyre')] = ns

    ns = runtime.TemplateNamespace('disqus', context._clean_inheritance_tokens(), templateuri='comments_helper_disqus.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'disqus')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link(context,link,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link(link, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link(link, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_link_script(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_link_script()))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_link_script()))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_comment_form(context,url,title,identifier):
    __M_caller = context.caller_stack._push_frame()
    try:
        comment_system = context.get('comment_system', UNDEFINED)
        isso = _mako_get_namespace(context, 'isso')
        muut = _mako_get_namespace(context, 'muut')
        disqus = _mako_get_namespace(context, 'disqus')
        facebook = _mako_get_namespace(context, 'facebook')
        googleplus = _mako_get_namespace(context, 'googleplus')
        intensedebate = _mako_get_namespace(context, 'intensedebate')
        livefyre = _mako_get_namespace(context, 'livefyre')
        __M_writer = context.writer()
        __M_writer('\n')
        if comment_system == 'disqus':
            __M_writer('        ')
            __M_writer(str(disqus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'livefyre':
            __M_writer('        ')
            __M_writer(str(livefyre.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'intensedebate':
            __M_writer('        ')
            __M_writer(str(intensedebate.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'muut':
            __M_writer('        ')
            __M_writer(str(muut.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'googleplus':
            __M_writer('        ')
            __M_writer(str(googleplus.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'facebook':
            __M_writer('        ')
            __M_writer(str(facebook.comment_form(url, title, identifier)))
            __M_writer('\n')
        elif comment_system == 'isso':
            __M_writer('        ')
            __M_writer(str(isso.comment_form(url, title, identifier)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "comments_helper.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\base\\templates/comments_helper.tmpl", "line_map": {"22": 9, "25": 6, "28": 7, "31": 5, "34": 8, "37": 4, "40": 3, "43": 0, "48": 2, "49": 3, "50": 4, "51": 5, "52": 6, "53": 7, "54": 8, "55": 9, "56": 27, "57": 45, "58": 63, "64": 29, "76": 29, "77": 30, "78": 31, "79": 31, "80": 31, "81": 32, "82": 33, "83": 33, "84": 33, "85": 34, "86": 35, "87": 35, "88": 35, "89": 36, "90": 37, "91": 37, "92": 37, "93": 38, "94": 39, "95": 39, "96": 39, "97": 40, "98": 41, "99": 41, "100": 41, "101": 42, "102": 43, "103": 43, "104": 43, "110": 47, "122": 47, "123": 48, "124": 49, "125": 49, "126": 49, "127": 50, "128": 51, "129": 51, "130": 51, "131": 52, "132": 53, "133": 53, "134": 53, "135": 54, "136": 55, "137": 55, "138": 55, "139": 56, "140": 57, "141": 57, "142": 57, "143": 58, "144": 59, "145": 59, "146": 59, "147": 60, "148": 61, "149": 61, "150": 61, "156": 11, "168": 11, "169": 12, "170": 13, "171": 13, "172": 13, "173": 14, "174": 15, "175": 15, "176": 15, "177": 16, "178": 17, "179": 17, "180": 17, "181": 18, "182": 19, "183": 19, "184": 19, "185": 20, "186": 21, "187": 21, "188": 21, "189": 22, "190": 23, "191": 23, "192": 23, "193": 24, "194": 25, "195": 25, "196": 25, "202": 196}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
