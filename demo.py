#!/usr/bin/env python3

import json

from wrapper import wbgetentities
from wrapper import wbsearchentities

query = 'discovery'

results = wbsearchentities(query)
print(json.dumps(results, indent=2, ensure_ascii=False))

qids = [result['id'] for result in results['search']]

entities = wbgetentities(*qids)
print(json.dumps(entities, indent=2, ensure_ascii=False))
