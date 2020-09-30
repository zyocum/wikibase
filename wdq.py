#!/usr/bin/env python3

"""Query the Wikidata query service for a given entity QID (or property PID)
and get back label information (in available languages).

You can also get properties of queried entities, and even get the labels of the 
values of the properties.

Examples:

$ ./wdq.py Q42 -H
Q42	Douglas Adams				

$ ./wdq.py Q42 -p P31 | csvlook -It
| entity | entity:en     | property | property:en | value | value:data |
| ------ | ------------- | -------- | ----------- | ----- | ---------- |
| Q42    | Douglas Adams | P31      | instance of | Q5    | human      |

$ ./wdq.py Q42 -p P31 -l de | csvlook -It
| entity | entity:de     | property | property:de | value | value:data |
| ------ | ------------- | -------- | ----------- | ----- | ---------- |
| Q42    | Douglas Adams | P31      | ist ein(e)  | Q5    | Mensch     |

$ ./wdq.py Q42 -p '*' | csvlook -It
| entity | entity:en     | property | property:en   | value     | value:data             |
| ------ | ------------- | -------- | ------------- | --------- | ---------------------- |
| Q42    | Douglas Adams | P31      | instance of   | Q5        | human                  |
| Q42    | Douglas Adams | P21      | sex or gender | Q6581097  | male                   |
| Q42    | Douglas Adams | P106     | occupation    | Q214917   | playwright             |
| Q42    | Douglas Adams | P106     | occupation    | Q28389    | screenwriter           |
| Q42    | Douglas Adams | P106     | occupation    | Q6625963  | novelist               |
| Q42    | Douglas Adams | P106     | occupation    | Q4853732  | children's writer      |
| Q42    | Douglas Adams | P106     | occupation    | Q18844224 | science fiction writer |
| Q42    | Douglas Adams | P106     | occupation    | Q245068   | comedian               |
| Q42    | Douglas Adams | P106     | occupation    | Q36180    | writer                 |
...

"""
import csv
import sys
import datetime

from datetime import datetime
from functools import lru_cache

from qwikidata.linked_data_interface import get_entity_dict_from_api
from qwikidata.entity import WikidataItem, WikidataProperty, WikidataLexeme

@lru_cache(maxsize=1024)
def get_wikidata_item(id_):
    d = get_entity_dict_from_api(id_)
    entity = {
        'item': WikidataItem,
        'property': WikidataProperty,
        'lexeme': WikidataLexeme
    }
    return entity[d['type']](d)

def get_time(value):
    try:
        dt = datetime.fromisoformat(value['time'].lstrip('+').rstrip('Z'))
        return dt.isoformat()
    except:
        return value

def get_properties(item, pids=None, language='en'):
    item_label = item.get_label(language)
    claim_groups = item.get_truthy_claim_groups()
    if pids is None or not any(pids):
        yield {
            'entity': [item.entity_id, item_label],
            'property': [None, None],
            'value': [None, None]
        }
    for pid, claim_group in claim_groups.items():
        if ('*' in pids) or (pid in pids):
            prop = get_wikidata_item(pid)
            prop_label = prop.get_label(language)
            for claim in claim_group:
                try:
                    value = claim.mainsnak.datavalue.value
                    if isinstance(value, dict):
                        record = {
                            'entity': [item.entity_id, item_label],
                            'property': [prop.entity_id, prop_label]
                        }
                        if value.get('id', '').startswith('Q'):
                            value_entity = get_wikidata_item(value['id'])
                            value_label = value_entity.get_label(language)
                            record['value'] = [value_entity.entity_id, value_label]
                        elif 'time' in value:
                            record['value'] = [None, get_time(value)]
                        elif 'text' in value:
                            record['value'] = [None, value['text']]
                        else:
                            record['value'] = [None, value]
                        yield record
                    elif isinstance(value, str):
                        record = {
                            'entity': [item.entity_id, item_label],
                            'property': [prop.entity_id, prop_label],
                            'value': [None, value]
                        }
                        yield record
                except AttributeError:
                    continue

def main(id_, pids, language, aliases=False, header=False):
    item = get_wikidata_item(id_)
    if aliases:
        writer = csv.writer(
            sys.stdout,
            dialect=csv.excel_tab
        )
        eid = item.entity_id
        el = item.get_label(language)
        aliases = item.get_aliases(language)
        writer.writerow([eid, el] + aliases)
    else:
        fieldnames = [
            'entity',
            f'entity:{language}',
            'property',
            f'property:{language}',
            'value',
            f'value:data'
        ]
        writer = csv.DictWriter(
            sys.stdout,
            fieldnames=fieldnames,
            dialect=csv.excel_tab
        )
        if header:
            writer.writeheader()
        for record in get_properties(item, pids=pids, language=language):
            eid, el = record['entity']
            pid, pl = record['property']
            vid, vl = record['value']
            writer.writerow({
                'entity': eid,
                f'entity:{language}': el,
                'property': pid,
                f'property:{language}': pl,
                'value': vid,
                'value:data': vl
            })

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
    parser.add_argument(
        '-p', '--pids',
        nargs='*',
        default=[],
        help=(
            'list of Wikidata property identifiers (PIDs) to include '
            '(all PIDs are listed by default)'
        ),
    )
    parser.add_argument(
        '-a', '--aliases',
        action='store_true',
        help='show aliases (instead of properties)',
    )
    parser.add_argument(
        '-l', '--language',
        default='en',
        help='Wikidata ISO-639-3 language code for labeling results',
    )
    parser.add_argument(
        '-H', '--no-header',
        action='store_false',
        help='suppress the header'
    )
    args = parser.parse_args()
    main(
        args.id,
        args.pids,
        args.language,
        aliases=args.aliases,
        header=args.no_header
    )
