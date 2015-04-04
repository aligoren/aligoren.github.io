# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428115071.133595
_enable_loop = True
_template_filename = 'C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_js', 'content', 'sourcelink', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def extra_js():
            return render_extra_js(context)
        thumbnail_size = _import_ns.get('thumbnail_size', context.get('thumbnail_size', UNDEFINED))
        photo_array_json = _import_ns.get('photo_array_json', context.get('photo_array_json', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<script src="/assets/js/flowr.plugin.js"></script>\n<script>\njsonContent = ')
        __M_writer(str(photo_array_json))
        __M_writer(';\n$("#gallery_container").flowr({\n        data : jsonContent,\n        height : ')
        __M_writer(str(thumbnail_size))
        __M_writer('*.6,\n        padding: 5,\n        rows: -1,\n        render : function(params) {\n            // Just return a div, string or a dom object, anything works fine\n            img = $("<img />").attr({\n                \'src\': params.itemData.url_thumb,\n                \'width\' : params.width,\n                \'height\' : params.height\n            }).css(\'max-width\', \'100%\');\n            link = $( "<a></a>").attr({\n                \'href\': params.itemData.url,\n                \'class\': \'image-reference\'\n            });\n            div = $("<div />").addClass(\'image-block\').attr({\n                \'title\': params.itemData.title,\n                \'data-toggle\': "tooltip",\n            });\n            link.append(img);\n            div.append(link);\n            div.hover(div.tooltip());\n            return div;\n        },\n        itemWidth : function(data) { return data.size.w; },\n        itemHeight : function(data) { return data.size.h; },\n        complete : function(params) {\n            if( jsonContent.length > params.renderedItems ) {\n                nextRenderList = jsonContent.slice( params.renderedItems );\n            }\n        }\n    });\n$("a.image-reference").colorbox({rel:"gal", maxWidth:"100%",maxHeight:"100%",scalePhotos:true});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context)
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        ui = _mako_get_namespace(context, 'ui')
        comments = _mako_get_namespace(context, 'comments')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i class="glyphicon glyphicon-folder-open"></i>&nbsp;')
                __M_writer(str(ftitle))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        __M_writer('\n<div id="gallery_container"></div>\n')
        if photo_array:
            __M_writer('<noscript>\n<ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('        <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(str(image['title']))
                __M_writer('">\n            <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(str(image['title']))
                __M_writer('" /></a>\n')
            __M_writer('</ul>\n</noscript>\n')
        if site_has_comments and enable_comments:
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
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
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n<link rel="alternate" type="application/rss+xml" title="RSS" href="rss.xml">\n<style type="text/css">\n    .image-block {\n        display: inline-block;\n    }\n    .flowr_row {\n        width: 100%;\n    }\n    </style>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "gallery.tmpl", "filename": "C:\\Python34\\lib\\site-packages\\nikola\\data\\themes\\bootstrap3\\templates/gallery.tmpl", "line_map": {"128": 9, "129": 10, "130": 10, "131": 10, "132": 12, "133": 13, "134": 14, "135": 14, "136": 17, "137": 18, "138": 19, "139": 20, "140": 20, "141": 20, "142": 20, "143": 20, "144": 22, "145": 24, "146": 26, "147": 27, "148": 29, "149": 30, "22": 4, "151": 30, "152": 30, "25": 3, "154": 31, "155": 31, "156": 31, "157": 31, "150": 30, "31": 0, "160": 37, "161": 37, "167": 5, "159": 36, "180": 41, "158": 33, "59": 2, "60": 3, "61": 4, "190": 42, "191": 42, "66": 5, "197": 191, "71": 39, "76": 52, "81": 94, "87": 55, "97": 55, "98": 58, "99": 58, "100": 61, "101": 61, "107": 7, "189": 41, "153": 30, "125": 7, "126": 8, "127": 8}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
