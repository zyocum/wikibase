#!/usr/bin/env python3

"""Query the Wikidata query service for a given entity QID (or property PID)
and get back entity information as JSON.

The returned JSON is equivalent to the JSON data that is available in
Wikidata entity dumps (available from https://dumps.wikimedia.org/wikidatawiki/entities/),
but this may be more convient for accessing individual records.

"""
import json

from functools import lru_cache

from qwikidata.linked_data_interface import get_entity_dict_from_api

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        'id',
        help='Wikidata identifier'
    )
    args = parser.parse_args()
    print(
        json.dumps(
            get_entity_dict_from_api(args.id),
            ensure_ascii=False
        )
    )