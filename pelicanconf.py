#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matt Fortier'
SITENAME = 'Matt Fortier'
SITEURL = 'http://mattfortier.me'

THEME = 'void/'
PATH = 'content'

TITLE = 'Matt Fortier'
DESCRIPTION = 'Big Data & ML | Travel | Photography | Misc.'

TIMEZONE = 'Asia/Shanghai'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Static Pages
PAGE_PATHS = ['pages']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ABOUT_PAGE_HEADER = 'Hello.'

# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%b %d, %Y'
DEFAULT_PAGINATION = False

# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"

# PLUGINS
PLUGIN_PATHS = ['pelican-plugins', 'pelican_dynamic']
PLUGINS = ['assets', 'liquid_tags.notebook', 'pelican_dynamic', 'render_math']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

#STATIC_PATHS = ['images', 'code', 'notebooks', 'extra', 'data']
#EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}

NAVIGATION = [
    # You probably want to fill these in so they point to your user pages
    {'site': 'twitter', 'user': '', 'url': 'https://twitter.com/mattfortier'},
    {'site': 'github', 'user': '', 'url': 'https://github.com/fortiema'},
    {'site': 'linkedin', 'user': '', 'url': 'http://linkedin.com/in/mattfortier-patsnap'},
]

TWITTER_NAME = ""
TWITTER_CARDS = True
FACEBOOK_SHARE = True

# Other
MAILCHIMP = False
CACHE_CONTENT = False

