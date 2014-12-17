# -*- coding: utf-8 -*-
"""
Ignore the unused imports, this file's purpose is to make visible
anything which a user might need to import from newspaper.
View newspaper/__init__.py for its usage.
"""
__title__ = 'newspaper'
__author__ = 'Lucas Ou-Yang'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014, Lucas Ou-Yang'

import feedparser

from .article import Article
from .configuration import Configuration
from .mthreading import NewsPool
from .settings import POPULAR_URLS, TRENDING_URL
from .source import Source
from .utils import extend_config, print_available_languages


def build(url='', dry=False, config=None, **kwargs):
    """Returns a constructed source object without
    downloading or parsing the articles
    """
    config = config or Configuration()
    config = extend_config(config, kwargs)
    url = url or ''
    s = Source(url, config=config)
    if not dry:
        s.build()
    return s


def build_article(url='', config=None, **kwargs):
    """Returns a constructed article object without downloading
    or parsing
    """
    config = config or Configuration()
    config = extend_config(config, kwargs)
    url = url or ''
    a = Article(url, config=config)
    return a


def languages():
    """Returns a list of the supported languages
    """
    print_available_languages()


def popular_urls():
    """Returns a list of pre-extracted popular source urls
    """
    with open(POPULAR_URLS) as f:
        urls = ['http://' + u.strip() for u in f.readlines()]
        return urls


def hot():
    """Returns a list of hit terms via google trends
    """
    try:
        listing = feedparser.parse(TRENDING_URL)['entries']
        trends = [item['title'] for item in listing]
        return trends
    except Exception as e:
        print('ERR hot terms failed!', str(e))
        return None
