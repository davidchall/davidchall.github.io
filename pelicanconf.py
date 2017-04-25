#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Hall'
SITENAME = 'David Hall'
SITEURL = 'https://davidchall.github.io'
DISQUS_SITENAME = 'davidchall'

# Theming
THEME = 'themes/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'emacs'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PATH = 'content'

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', 'https://github.com/davidchall'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = [
    'liquid_tags.notebook',
    'ipynb.liquid',
    'i18n_subsites'
]

STATIC_PATHS = ['notebooks']
