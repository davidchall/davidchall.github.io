#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'David Hall'
SITENAME = 'David C Hall'
AVATAR = 'images/profile.png'
ABOUT_ME = 'Postdoc in Radiation Oncology Physics'

# Theming
THEME = 'themes/pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
PYGMENTS_STYLE = 'emacs'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
SIDEBAR_ON_LEFT = True

TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', 'https://github.com/davidchall'),
          ('linkedin', 'https://www.linkedin.com/in/davidchristopherhall'))

DISPLAY_CATEGORIES_ON_MENU = False
DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives', 'search']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins', 'plugins']
PLUGINS = [
    'liquid_tags.notebook',
    'ipynb.liquid',
    'i18n_subsites',
    'tipue_search',
    'tag_cloud',
    'render_math',
]

PATH = 'content'
STATIC_PATHS = ['images', 'notebooks']
ARCHIVES_SAVE_AS = 'archives.html'
