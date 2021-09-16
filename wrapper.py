#!/usr/bin/env python3

"""Simple wrapper of a couple of the Wikibase API modules

C.f. https://www.mediawiki.org/wiki/Wikibase/API#API_modules
"""

import sys
import requests

from urllib import parse

def sep_join(values):
    """Prepare parameters that take multiple values
    See https://www.wikidata.org/w/api.php?action=help&modules=main#main/datatypes
    """
    if any((('|' in set(v)) for v in values)):
        # we need to use an INFORMATION SEPARATOR ONE (U+001F) character as delimiter
        SEPARATOR = '\u001F'
        return SEPARATOR + SEPARATOR.join(values)
    else:
        return '|'.join(values)

def wbgetentities(
    *ids,
    sites=['wikidatawiki'],
    titles=[],
    redirects='no',
    props=[
        'info',
        'sitelinks',
        'aliases',
        'labels',
        'descriptions',
        'claims',
        'datatype'
    ],
    languages=['en'],
    languagefallback=True,
    normalize=True,
    sitefilter=[]
):
    """Wrap Wikibase API wbgetentities module: https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities"""
    if not any(ids):
        raise ValueError('expected at least one ID')
    query = {
        'action': 'wbgetentities',
        'ids': sep_join(ids),
        'redirects': redirects,
        'format': 'json'
    }
    if any(sites):
        query['sites'] = sep_join(sites)
    if any(props):
        query['props'] = sep_join(props)
    if any(languages):
        query['languages'] = sep_join(languages)
    if languagefallback:
        query['languagefallback'] = True
    if normalize:
        query['normalize'] = True
    if any(sitefilter):
        query['sitefilter'] = sep_join(sitefilter)
    url = parse.urlunparse(
        parse.ParseResult(
            scheme='https',
            netloc='www.wikidata.org',
            path='/w/api.php',
            params='',
            query=parse.urlencode(query),
            fragment=''
        )
    )
    response = requests.get(url)
    print(
        f'[Status {response.status_code}]: {parse.unquote(response.url)}',
        file=sys.stderr
    )
    if response.status_code == 200:
        return response.json()

def wbsearchentities(
    search,
    language='en',
    strictlanguage=False,
    type_='item',
    limit=7,
    continue_=0,
    props=[],
):
    """Wrap Wikibase API wbsearchentities module: https://www.wikidata.org/w/api.php?action=help&modules=wbsearchentities"""
    query = {
        'action': 'wbsearchentities',
        'search': search,
        'language': language,
        'type': type_,
        'limit': limit,
        'continue': continue_,
        'format': 'json'
    }
    if strictlanguage:
        query['strictlanguage'] = True
    if any(props):
        query['props'] = sep_join(props)
    url = parse.urlunparse(
        parse.ParseResult(
            scheme='https',
            netloc='www.wikidata.org',
            path='/w/api.php',
            params='',
            query=parse.urlencode(query),
            fragment=''
        )
    )
    response = requests.get(url)
    print(
        f'[Status {response.status_code}]: {parse.unquote(response.url)}',
        file=sys.stderr
    )
    if response.status_code == 200:
        return response.json()
