# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115070.805995
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'belowtitle', 'content', 'sourcelink', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        def content():
            return render_content(context._locals(__M_locals))
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        show_blog_title = _import_ns.get('show_blog_title', context.get('show_blog_title', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context._locals(__M_locals))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        show_sourcelink = _import_ns.get('show_sourcelink', context.get('show_sourcelink', UNDEFINED))
        abs_link = _import_ns.get('abs_link', context.get('abs_link', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<a href="#content" class="sr-only sr-only-focusable">')
        __M_writer(str(messages("Skip to main content")))
        __M_writer('</a>\n\n<!-- Menubar -->\n\n<nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n    <div class="container"><!-- This keeps the margins nice -->\n        <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" href="')
        __M_writer(str(abs_link(_link("root", None, lang))))
        __M_writer('">\n')
        if logo_url:
            __M_writer('                <img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(str(blog_title))
            __M_writer('" id="logo">\n')
        __M_writer('\n')
        if show_blog_title:
            __M_writer('                <span id="blog-title">')
            __M_writer(str(blog_title))
            __M_writer('</span>\n')
        __M_writer('            </a>\n        </div><!-- /.navbar-header -->\n        <div class="collapse navbar-collapse navbar-ex1-collapse">\n            <ul class="nav navbar-nav">\n                ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n                ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n            </ul>\n')
        if search_form:
            __M_writer('                ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('\n            <ul class="nav navbar-nav navbar-right">\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'belowtitle'):
            context['self'].belowtitle(**pageargs)
        

        __M_writer('\n')
        if show_sourcelink:
            __M_writer('                    ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
                context['self'].sourcelink(**pageargs)
            

            __M_writer('\n')
        __M_writer('                ')
        __M_writer(str(template_hooks['menu_alt']()))
        __M_writer('\n            </ul>\n        </div><!-- /.navbar-collapse -->\n    </div><!-- /.container -->\n</nav>\n\n<!-- End of Menubar -->\n\n<div class="container" id="content" role="main">\n    <div class="body-content">\n        <!--Body content-->\n        <div class="row">\n            ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </div>\n        <!--End of body content-->\n\n        <footer>\n            ')
        __M_writer(str(content_footer))
        __M_writer('\n            ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n        </footer>\n    </div>\n</div>\n\n')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script>$(\'a.image-reference:not(.islink)\').colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.code()))
            __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_belowtitle(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        translations = _import_ns.get('translations', context.get('translations', UNDEFINED))
        def belowtitle():
            return render_belowtitle(context)
        base = _mako_get_namespace(context, 'base')
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            __M_writer('                    <li>')
            __M_writer(str(base.html_translations()))
            __M_writer('</li>\n')
        __M_writer('                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/base.tmpl", "line_map": {"128": 71, "129": 71, "130": 72, "131": 72, "132": 77, "133": 77, "134": 81, "135": 81, "136": 82, "137": 82, "138": 82, "139": 82, "190": 47, "144": 85, "145": 86, "146": 87, "147": 87, "148": 87, "149": 88, "22": 2, "151": 89, "152": 89, "25": 3, "154": 91, "155": 92, "28": 0, "150": 89, "162": 85, "227": 6, "156": 92, "199": 66, "176": 45, "213": 51, "188": 45, "189": 46, "153": 91, "191": 47, "192": 47, "193": 49, "68": 2, "69": 3, "70": 4, "71": 4, "72": 5, "73": 5, "78": 8, "79": 9, "80": 9, "81": 12, "82": 12, "83": 25, "84": 25, "85": 26, "86": 27, "87": 27, "88": 27, "89": 27, "90": 27, "91": 29, "92": 30, "93": 31, "94": 31, "95": 31, "96": 33, "97": 37, "98": 37, "99": 38, "100": 38, "101": 40, "102": 41, "103": 41, "104": 41, "105": 43, "236": 6, "110": 49, "111": 50, "112": 51, "242": 236, "117": 51, "118": 53, "119": 53, "120": 53, "121": 65, "122": 65, "127": 66}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
