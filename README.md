# wikibase
Python wrapper of Wikibase API: https://www.mediawiki.org/wiki/Wikibase/API#API_modules

Currently only the following API modules are implemented:

* [`wbgetentities`](https://www.wikidata.org/w/api.php?action=help&modules=wbgetentities)
* [`wbsearchentities`](https://www.wikidata.org/w/api.php?action=help&modules=wbsearchentities)

## Wikidata/Wikipedia Resources
* [`qwikidata`](https://pypi.org/project/qwikidata/)
* [`wptools`](https://pypi.org/project/wptools/)
* [Wikidata SPARQL Query Service](https://query.wikidata.org/)

## Setup
```bash
# create and activate a virtual environment
$ python3 -m venv wikibase
$ source wikibase/bin/activate
# install dependencies
$ pip3 install -r requirements.txt
...
```

## Run Demo
```bash
$ ./demo.py 
```
```
[Status 200]: https://www.wikidata.org/w/api.php?action=wbsearchentities&search=discovery&language=en&type=item&limit=7&continue=0&format=json
```
```json
{
  "searchinfo": {
    "search": "discovery"
  },
  "search": [
    {
      "id": "Q43404",
      "title": "Q43404",
      "pageid": 45612,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q43404",
      "concepturi": "http://www.wikidata.org/entity/Q43404",
      "label": "Discovery Channel",
      "description": "American basic cable and satellite television channel",
      "match": {
        "type": "label",
        "language": "en",
        "text": "Discovery Channel"
      }
    },
    {
      "id": "Q12772819",
      "title": "Q12772819",
      "pageid": 14157593,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q12772819",
      "concepturi": "http://www.wikidata.org/entity/Q12772819",
      "label": "discovery",
      "description": "act of detecting something new",
      "match": {
        "type": "label",
        "language": "en",
        "text": "discovery"
      }
    },
    {
      "id": "Q21296543",
      "title": "Q21296543",
      "pageid": 23343348,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q21296543",
      "concepturi": "http://www.wikidata.org/entity/Q21296543",
      "label": "Star Trek: Discovery",
      "description": "American television series based on Star Trek",
      "match": {
        "type": "alias",
        "language": "en",
        "text": "Discovery"
      },
      "aliases": [
        "Discovery"
      ]
    },
    {
      "id": "Q54384",
      "title": "Q54384",
      "pageid": 56962,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q54384",
      "concepturi": "http://www.wikidata.org/entity/Q54384",
      "label": "Discovery",
      "description": "space shuttle orbiter",
      "match": {
        "type": "label",
        "language": "en",
        "text": "Discovery"
      }
    },
    {
      "id": "Q211051",
      "title": "Q211051",
      "pageid": 206770,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q211051",
      "concepturi": "http://www.wikidata.org/entity/Q211051",
      "label": "Discovery",
      "description": "Wikimedia disambiguation page",
      "match": {
        "type": "label",
        "language": "en",
        "text": "Discovery"
      }
    },
    {
      "id": "Q1901313",
      "title": "Q1901313",
      "pageid": 1831357,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q1901313",
      "concepturi": "http://www.wikidata.org/entity/Q1901313",
      "label": "Discovery",
      "description": "2001 album by Daft Punk",
      "match": {
        "type": "label",
        "language": "en",
        "text": "Discovery"
      }
    },
    {
      "id": "Q483998",
      "title": "Q483998",
      "pageid": 455563,
      "repository": "wikidata",
      "url": "//www.wikidata.org/wiki/Q483998",
      "concepturi": "http://www.wikidata.org/entity/Q483998",
      "label": "anagnorisis",
      "description": "moment in a play or other work when a character makes a critical discovery",
      "match": {
        "type": "alias",
        "language": "en",
        "text": "discovery"
      },
      "aliases": [
        "discovery"
      ]
    }
  ],
  "search-continue": 7,
  "success": 1
}
```
```
[Status 200]: https://www.wikidata.org/w/api.php?action=wbgetentities&ids=Q43404|Q12772819|Q21296543|Q54384|Q211051|Q1901313|Q483998&redirects=no&format=json&sites=wikidatawiki&props=info|sitelinks|aliases|labels|descriptions|claims|datatype&languages=en&languagefallback=True&normalize=True
```
```json
{
  "entities": {
    "Q43404": {
      "pageid": 45612,
      "ns": 0,
      "title": "Q43404",
      "lastrevid": 1283545542,
      "modified": "2020-09-28T10:09:56Z",
      "type": "item",
      "id": "Q43404",
      "labels": {
        "en": {
          "language": "en",
          "value": "Discovery Channel"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "American basic cable and satellite television channel"
        }
      },
      "aliases": {
        "en": [
          {
            "language": "en",
            "value": "The Discovery Channel"
          },
          {
            "language": "en",
            "value": "Discovery"
          },
          {
            "language": "en",
            "value": "Discovery.com"
          }
        ]
      },
      "claims": {
        "P373": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P373",
              "hash": "82afca5b9e1827ddbd3232e78a4495c047f9bd11",
              "datavalue": {
                "value": "Discovery Channel",
                "type": "string"
              },
              "datatype": "string"
            },
            "type": "statement",
            "id": "q43404$17B7B660-A724-421B-81E3-E691CB193721",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P910": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P910",
              "hash": "815b3d7e9794d6794095a911ab691e651fa76ee9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 8380220,
                  "id": "Q8380220"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$08A53F35-2EF6-42CF-95F8-FF3B8003386D",
            "rank": "normal"
          }
        ],
        "P856": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P856",
              "hash": "f79b429c5f1da93018d085a5fc37c57cecce4e0e",
              "datavalue": {
                "value": "http://dsc.discovery.com",
                "type": "string"
              },
              "datatype": "url"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P407"
            ],
            "id": "Q43404$720F5BDF-8DDE-47AB-A47D-7C2189987E42",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P646": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P646",
              "hash": "e3537f61c96b4ce2931994616bbd859c529d4c75",
              "datavalue": {
                "value": "/m/0kc8y",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$07A161EB-5B8E-4C05-A88A-2AAB3290DDEB",
            "rank": "normal",
            "references": [
              {
                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 15241312,
                          "id": "Q15241312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                      "datavalue": {
                        "value": {
                          "time": "+2013-10-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P577"
                ]
              }
            ]
          }
        ],
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "a805808f2c1d49132e2c4b824e5ee97b7eb47ce7",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1616075,
                  "id": "Q1616075"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$9F6C62B8-A30E-4A8B-AE7B-8D351EACF24F",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "b868cb7869fd5c2e6ac4b9a1b2088ea75cf0e4a4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2001305,
                  "id": "Q2001305"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$0b5dbd64-4e9a-ef09-65ba-98c524e769d8",
            "rank": "normal"
          }
        ],
        "P571": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P571",
              "hash": "050e5d3c5ac00ad1f0cad4d8b00d140ca1f844c3",
              "datavalue": {
                "value": {
                  "time": "+1985-00-00T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 9,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q43404$F5AEB15B-A65F-405C-84C2-68AC51B54C65",
            "rank": "normal",
            "references": [
              {
                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P159": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P159",
              "hash": "b120d88dbcb1590927192a1bf8ecc08d523a4f4b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 755741,
                  "id": "Q755741"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P281": [
                {
                  "snaktype": "value",
                  "property": "P281",
                  "hash": "e1d7c6436362e6bfa1ae2572f0efdb32da7e8d27",
                  "datavalue": {
                    "value": "20910",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P17": [
                {
                  "snaktype": "value",
                  "property": "P17",
                  "hash": "be4c6eafa2984964f04be85667263f5642ba1a72",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 30,
                      "id": "Q30"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P6375": [
                {
                  "snaktype": "value",
                  "property": "P6375",
                  "hash": "80d1cb10c994144c28b61d5ed78b2061866fa725",
                  "datavalue": {
                    "value": {
                      "text": "One Discovery Place",
                      "language": "en"
                    },
                    "type": "monolingualtext"
                  },
                  "datatype": "monolingualtext"
                }
              ]
            },
            "qualifiers-order": [
              "P281",
              "P17",
              "P6375"
            ],
            "id": "Q43404$EF38DA4C-2CEE-4B56-AA47-28AA17F5C0C0",
            "rank": "normal"
          }
        ],
        "P112": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P112",
              "hash": "8da8ac85484683efcf1dcd03bb1d1cea0e0f9eb3",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3658792,
                  "id": "Q3658792"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$112EEBC5-90A0-4F46-842A-7316358D827B",
            "rank": "normal"
          }
        ],
        "P648": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P648",
              "hash": "2a05aeb0e807abad4635dc25503f7efbb3a87e11",
              "datavalue": {
                "value": "OL2770422A",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$0B8F0675-39F4-42E7-993E-354E856DE280",
            "rank": "normal"
          }
        ],
        "P17": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P17",
              "hash": "be4c6eafa2984964f04be85667263f5642ba1a72",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 30,
                  "id": "Q30"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$56B95155-2BA2-4EF3-92D2-596234A75FDB",
            "rank": "normal"
          }
        ],
        "P1417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1417",
              "hash": "a7a0d64ea71522a3974f14be74c23c2722cef394",
              "datavalue": {
                "value": "topic/Discovery-Channel",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$0B79BB4D-D542-4FAB-957C-4478166CEC48",
            "rank": "normal"
          }
        ],
        "P127": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P127",
              "hash": "1d8c0d8fbc7037da5b6e7b79be0004cc358406b2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 621592,
                  "id": "Q621592"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$6D47151E-C714-4077-BBD8-DA7EEBE88A2C",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P3417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3417",
              "hash": "43f7ce284326820186fadeb18f4fa14c680cd338",
              "datavalue": {
                "value": "Discovery-Channel",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$C2B998E0-22E4-4C19-BED2-5463DAB9C5A1",
            "rank": "normal",
            "references": [
              {
                "hash": "3b0a5bb3c1f955edce73740124f7d935698092ad",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "3ac9682e789a3a3791d4fd088b265ea03abef101",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 51711,
                          "id": "Q51711"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P3579": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3579",
              "hash": "8cbf0e5a2811258193c915c3f149300ed51977e3",
              "datavalue": {
                "value": "discoverychina",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$EC719E87-68F6-4DFD-B241-4FA8283598DA",
            "rank": "normal",
            "references": [
              {
                "hash": "0ee3b3ba1c958f4c3dcba7ed8091fe4b57311348",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "cb49f6fa327b245e4a5aaf48c44b3f503bcd4265",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 30239,
                          "id": "Q30239"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P1830": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1830",
              "hash": "96fc5b6fc867933807de01490462ba9fd255da10",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3221020,
                  "id": "Q3221020"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$7BFEE7B0-6836-4F4B-9608-3A8FCB7AD45C",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1830",
              "hash": "9f33fae4de55729ab6d052835552238987d24168",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5281971,
                  "id": "Q5281971"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q43404$9D4BE2A3-9605-4FDB-A0AE-576AEC69D7B7",
            "rank": "normal"
          }
        ],
        "P3553": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3553",
              "hash": "389913ebf4eed4a5a3ef0625b35c622d92552456",
              "datavalue": {
                "value": "19565533",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$6dddaf91-4011-8301-0d5c-2b704af0019d",
            "rank": "normal"
          }
        ],
        "P154": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P154",
              "hash": "015efbc89d7ebd016aa0414ebec272426fdfc397",
              "datavalue": {
                "value": "2019 Discovery logo.svg",
                "type": "string"
              },
              "datatype": "commonsMedia"
            },
            "type": "statement",
            "id": "Q43404$0f07f7e8-4791-24b0-ef05-2f19178fc70e",
            "rank": "normal"
          }
        ],
        "P2003": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2003",
              "hash": "86ed559d7ef26db84be424fad9c72257cd983014",
              "datavalue": {
                "value": "discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$df195ac3-4ffc-08ce-f2b9-3ff72bcbaf25",
            "rank": "normal"
          }
        ],
        "P2013": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2013",
              "hash": "5cdf7d6f38e206e26c019b1ab5c13a505d6c662e",
              "datavalue": {
                "value": "Discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q43404$d2ac558f-4cb7-5818-86aa-5a10dc727aa1",
            "rank": "normal"
          }
        ],
        "P2002": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2002",
              "hash": "cdfbee17c8895cb85cf5d968af537dcf1c6a8bab",
              "datavalue": {
                "value": "discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P6552": [
                {
                  "snaktype": "value",
                  "property": "P6552",
                  "hash": "b4af577b6eac1a16fc1685c8ac513fd206504c7e",
                  "datavalue": {
                    "value": "17842366",
                    "type": "string"
                  },
                  "datatype": "external-id"
                }
              ],
              "P1552": [
                {
                  "snaktype": "value",
                  "property": "P1552",
                  "hash": "62f0039d240f7eeba6c6908a0d8807a6188324a1",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 28378282,
                      "id": "Q28378282"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P3744": [
                {
                  "snaktype": "value",
                  "property": "P3744",
                  "hash": "7f0fd9c7a0a3cfce57319f747504ae34ff9a9d60",
                  "datavalue": {
                    "value": {
                      "amount": "+8545436",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ],
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "e3dd0640d106956ae28b554d1fa70104c58e5ed7",
                  "datavalue": {
                    "value": {
                      "time": "+2020-02-29T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "b93a9e5e1b7c5761aecfa586449f98a2008e4702",
                  "datavalue": {
                    "value": {
                      "time": "+2008-12-03T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P6552",
              "P1552",
              "P3744",
              "P585",
              "P580"
            ],
            "id": "Q43404$f8279ed5-4e01-e3a2-c8df-0eb94f4ae315",
            "rank": "normal"
          }
        ]
      },
      "sitelinks": {
        "arwiki": {
          "site": "arwiki",
          "title": "قناة ديسكفري",
          "badges": []
        },
        "astwiki": {
          "site": "astwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "azwiki": {
          "site": "azwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "bgwiki": {
          "site": "bgwiki",
          "title": "Дискавъри Ченъл",
          "badges": []
        },
        "bnwiki": {
          "site": "bnwiki",
          "title": "ডিসকভারি চ্যানেল",
          "badges": []
        },
        "cawiki": {
          "site": "cawiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "cswiki": {
          "site": "cswiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "dawiki": {
          "site": "dawiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "elwiki": {
          "site": "elwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "eowiki": {
          "site": "eowiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "etwiki": {
          "site": "etwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "euwiki": {
          "site": "euwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "fawiki": {
          "site": "fawiki",
          "title": "شبکه تلویزیونی دیسکاوری",
          "badges": []
        },
        "fiwiki": {
          "site": "fiwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "glwiki": {
          "site": "glwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "guwiki": {
          "site": "guwiki",
          "title": "ડિસ્કવરી ચેનલ",
          "badges": []
        },
        "hewiki": {
          "site": "hewiki",
          "title": "ערוץ דיסקברי",
          "badges": []
        },
        "hiwiki": {
          "site": "hiwiki",
          "title": "डिस्कवरी चैनल",
          "badges": []
        },
        "hrwiki": {
          "site": "hrwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "huwiki": {
          "site": "huwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "hywiki": {
          "site": "hywiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "idwiki": {
          "site": "idwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "itwiki": {
          "site": "itwiki",
          "title": "Discovery Channel (Stati Uniti d'America)",
          "badges": []
        },
        "jawiki": {
          "site": "jawiki",
          "title": "ディスカバリーチャンネル",
          "badges": []
        },
        "jvwiki": {
          "site": "jvwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "knwiki": {
          "site": "knwiki",
          "title": "ಡಿಸ್ಕವರಿ ಚಾನೆಲ್",
          "badges": []
        },
        "kowiki": {
          "site": "kowiki",
          "title": "디스커버리 채널",
          "badges": []
        },
        "mkwiki": {
          "site": "mkwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "mlwiki": {
          "site": "mlwiki",
          "title": "ഡിസ്കവറി ചാനൽ",
          "badges": []
        },
        "mswiki": {
          "site": "mswiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "nlwiki": {
          "site": "nlwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "nnwiki": {
          "site": "nnwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "nowiki": {
          "site": "nowiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "plwiki": {
          "site": "plwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "rowiki": {
          "site": "rowiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "ruwikinews": {
          "site": "ruwikinews",
          "title": "Категория:Discovery Channel",
          "badges": []
        },
        "scowiki": {
          "site": "scowiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "simplewiki": {
          "site": "simplewiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "siwiki": {
          "site": "siwiki",
          "title": "ඩිස්කවරි නාලිකාව",
          "badges": []
        },
        "skwiki": {
          "site": "skwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "srwiki": {
          "site": "srwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "svwiki": {
          "site": "svwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "svwikinews": {
          "site": "svwikinews",
          "title": "Kategori:Discovery Channel",
          "badges": []
        },
        "tawiki": {
          "site": "tawiki",
          "title": "டிஸ்கவரி தொலைக்காட்சி",
          "badges": []
        },
        "tewiki": {
          "site": "tewiki",
          "title": "డిస్కవరీ ఛానల్",
          "badges": []
        },
        "thwiki": {
          "site": "thwiki",
          "title": "ดิสคัฟเวอรี่ แชนแนล",
          "badges": []
        },
        "tlwiki": {
          "site": "tlwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "trwiki": {
          "site": "trwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "vecwiki": {
          "site": "vecwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "viwiki": {
          "site": "viwiki",
          "title": "Discovery Channel",
          "badges": []
        },
        "wuuwiki": {
          "site": "wuuwiki",
          "title": "探索频道",
          "badges": []
        },
        "zh_yuewiki": {
          "site": "zh_yuewiki",
          "title": "發現頻道",
          "badges": []
        },
        "zhwiki": {
          "site": "zhwiki",
          "title": "探索頻道",
          "badges": []
        }
      }
    },
    "Q12772819": {
      "pageid": 14157593,
      "ns": 0,
      "title": "Q12772819",
      "lastrevid": 1281005482,
      "modified": "2020-09-23T06:08:24Z",
      "type": "item",
      "id": "Q12772819",
      "labels": {
        "en": {
          "language": "en",
          "value": "discovery"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "act of detecting something new"
        }
      },
      "aliases": {},
      "claims": {
        "P279": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P279",
              "hash": "743be153f4d27294d64874ad328aabf824594c59",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 451967,
                  "id": "Q451967"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q12772819$37638AA7-7DA5-4ADD-84CB-D77C05B7B8BA",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P279",
              "hash": "3fc97b254ec6e32d9e301280817ea7c0797fd81d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 37113105,
                  "id": "Q37113105"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q12772819$17901121-B52B-49CE-B035-32FB072590DF",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P279",
              "hash": "5d931672fdba0863cfb706adc09da8d9f01a7072",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1190554,
                  "id": "Q1190554"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q12772819$649394D9-9844-4ECE-B1FF-F392F4441704",
            "rank": "normal"
          }
        ],
        "P646": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P646",
              "hash": "3b0585e6915b1256f4d7b2777187c574c1d3e6f5",
              "datavalue": {
                "value": "/m/0dzcf",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$FADD196D-260D-4394-B5EC-4FE3AC227310",
            "rank": "normal",
            "references": [
              {
                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 15241312,
                          "id": "Q15241312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                      "datavalue": {
                        "value": {
                          "time": "+2013-10-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P577"
                ]
              }
            ]
          }
        ],
        "P910": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P910",
              "hash": "da50c0bd3185491c29eb65fa71800817f3b24fef",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 10193613,
                  "id": "Q10193613"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q12772819$9D696576-4EC4-413F-B6CC-CC641B4E58F2",
            "rank": "normal",
            "references": [
              {
                "hash": "a29a646602abf65105ed0f39a44231c962ece9ee",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "c6f1777471211df31724ac60175786f3872c83e9",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 177837,
                          "id": "Q177837"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P227": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P227",
              "hash": "8e1249d9b548790150be7cce303e3b6a79689e84",
              "datavalue": {
                "value": "4014841-5",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$ADBB00FA-D26C-4662-B766-D386C6888929",
            "rank": "normal",
            "references": [
              {
                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P1343": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1343",
              "hash": "62c309f8296338bd9647a7e758857137f3370310",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2657718,
                  "id": "Q2657718"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P478": [
                {
                  "snaktype": "value",
                  "property": "P478",
                  "hash": "7ec55205f2db1067ff9cc258d63c9c187f3bc517",
                  "datavalue": {
                    "value": "6",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ],
              "P304": [
                {
                  "snaktype": "value",
                  "property": "P304",
                  "hash": "1e4f53f004c6fb7290b235d83d85370fa7fdae1d",
                  "datavalue": {
                    "value": "204",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P478",
              "P304"
            ],
            "id": "Q12772819$08EFA310-440B-4BB0-85A4-DB1A842CE805",
            "rank": "normal",
            "references": [
              {
                "hash": "8bc722e6797143f2ba971ee5fedaeb0a331268e6",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "4b9ead388e47f64ea2ecb2b82c5d4f516003a8d5",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 1975217,
                          "id": "Q1975217"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P3417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3417",
              "hash": "3517f390e46e76cb08833f1c4af49b069d6ba868",
              "datavalue": {
                "value": "Discoveries",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$316A7EB1-B10B-46A7-BDC8-0807387B9823",
            "rank": "normal"
          }
        ],
        "P1051": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1051",
              "hash": "9a1259e43613f41f148e8c99f7d34efbe00091c6",
              "datavalue": {
                "value": "12000",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$65312665-7133-4261-A33D-7FABAD53256B",
            "rank": "normal"
          }
        ],
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "085c6a1d6cee9a9681c283357bc8bdf2d05ef832",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 41172303,
                  "id": "Q41172303"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "649214aa36043a894ba236af0134937bb67ee7fd",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 7991,
                      "id": "Q7991"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P805"
            ],
            "id": "Q12772819$C9B2309E-BE58-433C-9966-87DA7E828377",
            "rank": "normal"
          }
        ],
        "P4746": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4746",
              "hash": "d9fa66f2b8596f05e17f221a9a1a2de618152105",
              "datavalue": {
                "value": "137899",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$75CA2AFD-A406-4D41-8A66-C0D96F743FAE",
            "rank": "normal"
          }
        ],
        "P1417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1417",
              "hash": "a32d2de09f5ae943c9082a510acd66424571c79b",
              "datavalue": {
                "value": "topic/discovery-knowledge-achievement",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$68979397-EFC2-4066-B2F7-B7F2D765A4E7",
            "rank": "normal"
          }
        ],
        "P5357": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P5357",
              "hash": "e670fcdbe87a589b43017d991a21639db4c068da",
              "datavalue": {
                "value": "discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$1D3C4792-9CC1-4194-A064-707B028A3DEE",
            "rank": "normal"
          }
        ],
        "P3123": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3123",
              "hash": "4df5f66bb2a533203e2d38bab5cb0d805fecd2b3",
              "datavalue": {
                "value": "scientific-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$1E6E5C78-D574-413D-AC24-83EC52A38A0C",
            "rank": "normal"
          }
        ],
        "P1687": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1687",
              "hash": "56997a1f3af8b9382b92f10ee4420498cff5d698",
              "datavalue": {
                "value": {
                  "entity-type": "property",
                  "numeric-id": 575,
                  "id": "P575"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-property"
            },
            "type": "statement",
            "id": "Q12772819$B9F37D12-76C2-4F26-BC32-3340F049742E",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1687",
              "hash": "d6c30eb335d40cd4008a53a41d6762e6922f28f1",
              "datavalue": {
                "value": {
                  "entity-type": "property",
                  "numeric-id": 61,
                  "id": "P61"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-property"
            },
            "type": "statement",
            "id": "Q12772819$A622ADEB-456A-490A-875F-F35712338AFE",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1687",
              "hash": "68b4436fd756409329c969adc694916074679c28",
              "datavalue": {
                "value": {
                  "entity-type": "property",
                  "numeric-id": 189,
                  "id": "P189"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-property"
            },
            "type": "statement",
            "id": "Q12772819$52E76656-46ED-4065-89E6-C9E1FAE2F77D",
            "rank": "normal"
          }
        ],
        "P361": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P361",
              "hash": "9577875b53cff629b7704855d228090295dd2275",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 77468620,
                  "id": "Q77468620"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q12772819$669D50AE-2D83-4F81-ACDF-4C8D1DD9FFD1",
            "rank": "normal"
          }
        ],
        "P244": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P244",
              "hash": "c8ac1bbcb0c66f2c6b89e1234b280131cf87b27a",
              "datavalue": {
                "value": "sh93003312",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$5ACEEA68-3A7E-4586-8505-A4307093119D",
            "rank": "normal"
          }
        ],
        "P268": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P268",
              "hash": "ee2db26ff931c755828f1a42b2fde45138998c6d",
              "datavalue": {
                "value": "11944415s",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$F2C82304-5BA7-48AD-B0FE-7FA17E5D7426",
            "rank": "normal"
          }
        ],
        "P508": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P508",
              "hash": "77f18a24d63b537aa5794d051c2680de280b4b85",
              "datavalue": {
                "value": "36440",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$89D3F3C0-B44C-44A3-8EC8-DDAE4515ED26",
            "rank": "normal"
          }
        ],
        "P7818": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7818",
              "hash": "624e4b227229f3b0f7d653292583cce2ef3a1d2d",
              "datavalue": {
                "value": "Découverte",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$2C436214-476C-423C-848B-5534F0C3EDC6",
            "rank": "normal"
          }
        ],
        "P1552": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1552",
              "hash": "c9b2c72e790c4436f94b594efe5b9c30ec6da901",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2376542,
                  "id": "Q2376542"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q12772819$7E029B38-88DD-4E9D-84F5-3E6DDDF7341F",
            "rank": "normal"
          }
        ],
        "P7033": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7033",
              "hash": "7a0d7993a88b484640bb93e6b1723255a89ac1e3",
              "datavalue": {
                "value": "scot/13566",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q12772819$0F3EFD96-012C-42E5-9C30-0D5854C1EED7",
            "rank": "normal"
          }
        ]
      },
      "sitelinks": {
        "abwiki": {
          "site": "abwiki",
          "title": "Аарԥшымҭа",
          "badges": []
        },
        "arwiki": {
          "site": "arwiki",
          "title": "اكتشاف (رصد)",
          "badges": []
        },
        "azwiki": {
          "site": "azwiki",
          "title": "Kəşf",
          "badges": []
        },
        "azwikiquote": {
          "site": "azwikiquote",
          "title": "Kəşf",
          "badges": []
        },
        "bgwiki": {
          "site": "bgwiki",
          "title": "Откритие",
          "badges": []
        },
        "cawiki": {
          "site": "cawiki",
          "title": "Descobriment",
          "badges": []
        },
        "cswiki": {
          "site": "cswiki",
          "title": "Objev",
          "badges": []
        },
        "cvwiki": {
          "site": "cvwiki",
          "title": "Уçнăлăх",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Entdeckung",
          "badges": []
        },
        "dewikiquote": {
          "site": "dewikiquote",
          "title": "Entdeckung",
          "badges": []
        },
        "elwiki": {
          "site": "elwiki",
          "title": "Ανακάλυψη",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Discovery (observation)",
          "badges": []
        },
        "eowiki": {
          "site": "eowiki",
          "title": "Malkovro",
          "badges": []
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Descubrimiento",
          "badges": []
        },
        "eswikiquote": {
          "site": "eswikiquote",
          "title": "Descubrimiento",
          "badges": []
        },
        "fawiki": {
          "site": "fawiki",
          "title": "کشف",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Découverte scientifique",
          "badges": []
        },
        "glwiki": {
          "site": "glwiki",
          "title": "Descubrimento",
          "badges": []
        },
        "hewiki": {
          "site": "hewiki",
          "title": "תגלית",
          "badges": []
        },
        "huwiki": {
          "site": "huwiki",
          "title": "Felfedezés",
          "badges": []
        },
        "hywiki": {
          "site": "hywiki",
          "title": "Հայտնագործություն",
          "badges": []
        },
        "itwikiquote": {
          "site": "itwikiquote",
          "title": "Scoperta",
          "badges": []
        },
        "jawiki": {
          "site": "jawiki",
          "title": "発見",
          "badges": []
        },
        "kkwiki": {
          "site": "kkwiki",
          "title": "Ғылыми жаңалық",
          "badges": []
        },
        "kowiki": {
          "site": "kowiki",
          "title": "발견",
          "badges": []
        },
        "lbwiki": {
          "site": "lbwiki",
          "title": "Entdeckung",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Descoberta",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Открытие",
          "badges": []
        },
        "simplewiki": {
          "site": "simplewiki",
          "title": "Discovery (observation)",
          "badges": []
        },
        "skwiki": {
          "site": "skwiki",
          "title": "Objav",
          "badges": []
        },
        "skwikiquote": {
          "site": "skwikiquote",
          "title": "Objav",
          "badges": []
        },
        "svwiki": {
          "site": "svwiki",
          "title": "Upptäckt",
          "badges": []
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Наукове відкриття",
          "badges": []
        },
        "viwiki": {
          "site": "viwiki",
          "title": "Khám phá",
          "badges": []
        }
      }
    },
    "Q21296543": {
      "pageid": 23343348,
      "ns": 0,
      "title": "Q21296543",
      "lastrevid": 1283318994,
      "modified": "2020-09-27T21:19:14Z",
      "type": "item",
      "id": "Q21296543",
      "labels": {
        "en": {
          "language": "en",
          "value": "Star Trek: Discovery"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "American television series based on Star Trek"
        }
      },
      "aliases": {
        "en": [
          {
            "language": "en",
            "value": "ST: DSC"
          },
          {
            "language": "en",
            "value": "DSC"
          },
          {
            "language": "en",
            "value": "DIS"
          },
          {
            "language": "en",
            "value": "Discovery"
          }
        ]
      },
      "claims": {
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "40a93c25a36e6a07478de6eca4ba68f5b9aaa85f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5398426,
                  "id": "Q5398426"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$73dd403a-494c-c953-5c99-d7218fa79ef1",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "b1d37b198e280f08d53a4a0cf563359d8ea46252",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 62573441,
                  "id": "Q62573441"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$87fdb7ab-420e-76b6-4793-dc0866d19b6c",
            "rank": "normal"
          }
        ],
        "P1431": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1431",
              "hash": "5879f1f6851bff8e2296107bf8328c4cbd8804f8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 432598,
                  "id": "Q432598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$18943ec6-423d-41a7-e99e-a7f3dcafdb66",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1431",
              "hash": "80497ae9b00642251e1a0fa90d327bbd7476cfe4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 21663076,
                  "id": "Q21663076"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$10a0eaa4-4af0-32d9-5f66-efd14c0c3722",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1431",
              "hash": "bb1d66486c142ed7e3bb81c6aade339256519f0a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 995026,
                  "id": "Q995026"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$24407417-41ea-7f57-729f-a2f14049162d",
            "rank": "normal",
            "references": [
              {
                "hash": "479da7aff851c1d0c772c80569e5de3d20d23c13",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8e9a17d7c181f91b9cbca513a15bcd65dd2b9a36",
                      "datavalue": {
                        "value": "http://www.startrek.com/article/bryan-fuller-named-co-creator-of-new-star-trek-tv-series",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "db1f412eed137f39493351fc453202c7d3653700",
                      "datavalue": {
                        "value": {
                          "text": "Bryan Fuller Named Co-Creator of New Star Trek TV Series",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P1476"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1431",
              "hash": "0caded623c6ba836b8d6ae4a0116a2744f3bd976",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 7356345,
                  "id": "Q7356345"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$074e8118-4b97-1c56-0981-de82fe493242",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1431",
              "hash": "aceba7e3a7872b74aa17daea92ddde12e9b9d4b9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3018772,
                  "id": "Q3018772"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$913bedd7-4a70-c71b-c07d-b8c4d89d8ddc",
            "rank": "normal",
            "references": [
              {
                "hash": "aa30c81e2bfe02a26e29412c92986f0fbecac096",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "6a164248fc96bfa583bbb495cb63ae6401ec203c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 206855,
                          "id": "Q206855"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "42b07360a950a06b6fee81022138f6760aaaedf3",
                      "datavalue": {
                        "value": "https://ru.wikipedia.org/?oldid=104746961",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1431",
              "hash": "a370d787b009c1fc3bf59abb8bf31ca0f024b3fd",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 419454,
                  "id": "Q419454"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$40a16a78-4b85-6b45-0732-3e62cf713d48",
            "rank": "normal",
            "references": [
              {
                "hash": "aa30c81e2bfe02a26e29412c92986f0fbecac096",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "6a164248fc96bfa583bbb495cb63ae6401ec203c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 206855,
                          "id": "Q206855"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "42b07360a950a06b6fee81022138f6760aaaedf3",
                      "datavalue": {
                        "value": "https://ru.wikipedia.org/?oldid=104746961",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ],
        "P136": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "45cc35a978e1dd3d370a2601b0f4c7cb371b701b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 336059,
                  "id": "Q336059"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8ac43fe9-4524-efcf-bb95-99ff192d49b4",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "2e4b82353990cab002e5ef1f87b8640c8669b6fd",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 85133165,
                  "id": "Q85133165"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$19B7CC5D-A3D8-49AD-8983-B85EAD7D4EFE",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "202d8227cb86026ec9956eea1628a52cd8d3cdfb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 24925,
                  "id": "Q24925"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$6d8fbfeb-4b7e-0a32-6d06-47a5f7d540f7",
            "rank": "normal",
            "references": [
              {
                "hash": "aa30c81e2bfe02a26e29412c92986f0fbecac096",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "6a164248fc96bfa583bbb495cb63ae6401ec203c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 206855,
                          "id": "Q206855"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "42b07360a950a06b6fee81022138f6760aaaedf3",
                      "datavalue": {
                        "value": "https://ru.wikipedia.org/?oldid=104746961",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ],
        "P364": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P364",
              "hash": "cc2c15fb58feeae8fe7a641c0e2ddaf3f48e59f8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1860,
                  "id": "Q1860"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$143d9dcd-49a8-b5df-f1cc-a09c62a086d2",
            "rank": "preferred",
            "references": [
              {
                "hash": "65c7f84d051239f91cc90095b052e2d00070f2f0",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "05a2176a04251188610f9f78888e1e7dc6ae762d",
                      "datavalue": {
                        "value": "https://de.wikipedia.org/w/index.php?title=Star_Trek:_Discovery&oldid=193581532",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P364",
              "hash": "e011693632d15202b8059486d6786a19b6fa7dd7",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 10134,
                  "id": "Q10134"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$cc05e92c-432d-b6a0-de6d-a693243b406c",
            "rank": "normal",
            "references": [
              {
                "hash": "65c7f84d051239f91cc90095b052e2d00070f2f0",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "05a2176a04251188610f9f78888e1e7dc6ae762d",
                      "datavalue": {
                        "value": "https://de.wikipedia.org/w/index.php?title=Star_Trek:_Discovery&oldid=193581532",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ],
        "P495": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P495",
              "hash": "7f985e15819b74ed189d022e004890e66d2ae42e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 30,
                  "id": "Q30"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$65ffc20e-4521-ab8d-5b2a-d73e89b8b847",
            "rank": "normal",
            "references": [
              {
                "hash": "65c7f84d051239f91cc90095b052e2d00070f2f0",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "05a2176a04251188610f9f78888e1e7dc6ae762d",
                      "datavalue": {
                        "value": "https://de.wikipedia.org/w/index.php?title=Star_Trek:_Discovery&oldid=193581532",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ],
        "P272": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P272",
              "hash": "08c4a845c7fc74d8ba199943f8092f03e5b15c5d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2576666,
                  "id": "Q2576666"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$29e5d33a-4aa7-a318-d334-2536fb4fa02e",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P272",
              "hash": "df295f739adf1b412ef115183f345ba9465356b1",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 42305720,
                  "id": "Q42305720"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$75de5a66-436b-6887-1dbd-c461fcf7bb15",
            "rank": "normal"
          }
        ],
        "P155": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P155",
              "hash": "1e780cf82c260cb12120055abb5e74b8875ec90f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 380519,
                  "id": "Q380519"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$13cef2e0-4a1b-694d-7992-45b44cca4df9",
            "rank": "normal"
          }
        ],
        "P345": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P345",
              "hash": "c0adb43560567777836f60d53b04dea627f253cc",
              "datavalue": {
                "value": "tt5171438",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$3984ffeb-448c-5610-6ee7-e8ef8f34006d",
            "rank": "normal",
            "references": [
              {
                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P170": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P170",
              "hash": "fc299a84e0d182b25c77f4eb939f7968b470ed2f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 995026,
                  "id": "Q995026"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$426e57d1-4b74-df9a-d694-804e96236124",
            "rank": "normal",
            "references": [
              {
                "hash": "5b9873b1540b1f2e13da62fe412bed3539dc564b",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8e9a17d7c181f91b9cbca513a15bcd65dd2b9a36",
                      "datavalue": {
                        "value": "http://www.startrek.com/article/bryan-fuller-named-co-creator-of-new-star-trek-tv-series",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "a8a668d9d26b3fdd2ccddb1e0c17da3e629b2e0f",
                      "datavalue": {
                        "value": {
                          "time": "+2016-02-10T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "e1820cf98644b205b8d0e7277b424a3799e44e2d",
                      "datavalue": {
                        "value": {
                          "text": "Bryan Fuller Named Co-Creator of New Star Trek TV Series",
                          "language": "anp"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1476"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P170",
              "hash": "39ebac0f32d9fb455adb5c6ed24fb68869431f5b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 432598,
                  "id": "Q432598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$7a41aa8f-4593-3a63-906e-8de052951de8",
            "rank": "normal"
          }
        ],
        "P1476": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1476",
              "hash": "e597cff8d7dc880698c8bfac0434bbb10abc5c9c",
              "datavalue": {
                "value": {
                  "text": "Star Trek: Discovery",
                  "language": "en"
                },
                "type": "monolingualtext"
              },
              "datatype": "monolingualtext"
            },
            "type": "statement",
            "id": "Q21296543$5ee62316-459f-e918-e9e1-5c804ecc3ecf",
            "rank": "normal"
          }
        ],
        "P2002": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2002",
              "hash": "00aa67544342c82d01d5b7f73ba5000c4ce7e1e8",
              "datavalue": {
                "value": "StarTrekRoom",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P3744": [
                {
                  "snaktype": "value",
                  "property": "P3744",
                  "hash": "a685fac85dedf787f1e5101efe5bd66474f2a43d",
                  "datavalue": {
                    "value": {
                      "amount": "+35349",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                },
                {
                  "snaktype": "value",
                  "property": "P3744",
                  "hash": "24e3388141b713af8d012bc7681f412c65926e2a",
                  "datavalue": {
                    "value": {
                      "amount": "+61631",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                },
                {
                  "snaktype": "value",
                  "property": "P3744",
                  "hash": "04db6dd9cf778d7e7f8c18839184d3d820ecb458",
                  "datavalue": {
                    "value": {
                      "amount": "+62889",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ],
              "P6552": [
                {
                  "snaktype": "value",
                  "property": "P6552",
                  "hash": "0bf3ec41f13d39fc0d716a03050fdfbf7b4b0072",
                  "datavalue": {
                    "value": "700534740575584258",
                    "type": "string"
                  },
                  "datatype": "external-id"
                }
              ],
              "P1552": [
                {
                  "snaktype": "value",
                  "property": "P1552",
                  "hash": "62f0039d240f7eeba6c6908a0d8807a6188324a1",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 28378282,
                      "id": "Q28378282"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "3bd5fb4ab8f748bfaa7a0becb2a0929e439dbba8",
                  "datavalue": {
                    "value": {
                      "time": "+2020-04-27T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                },
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "4d359b5b4e3bf63985b89a5b4c90b86019a19d1e",
                  "datavalue": {
                    "value": {
                      "time": "+2020-07-03T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "8aa5081d4c9700a0fe4d9a50085c2a9ca5eba872",
                  "datavalue": {
                    "value": {
                      "time": "+2016-02-18T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                },
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "d3d7bfb9bd159985e2fa90fab87bb6b7008169e2",
                  "datavalue": {
                    "value": {
                      "time": "+2016-02-19T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P3744",
              "P6552",
              "P1552",
              "P585",
              "P580"
            ],
            "id": "Q21296543$c4d0ad23-4682-59eb-ee39-c36e9221ac69",
            "rank": "normal",
            "references": [
              {
                "hash": "830e0d3d65e6b91e769889d7d1177706b5c1e0ca",
                "snaks": {
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cd8210fc3215a6112ebad72d11663d1a56b14d67",
                      "datavalue": {
                        "value": {
                          "time": "+2018-05-10T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2002",
              "hash": "a70e84f894b7291b66f58640b5e846fb3a5c7cd4",
              "datavalue": {
                "value": "startrekcbs",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P3744": [
                {
                  "snaktype": "value",
                  "property": "P3744",
                  "hash": "6a285fd3510e928657da93af4f46bc7bd8c954fa",
                  "datavalue": {
                    "value": {
                      "amount": "+160859",
                      "unit": "1"
                    },
                    "type": "quantity"
                  },
                  "datatype": "quantity"
                }
              ],
              "P6552": [
                {
                  "snaktype": "value",
                  "property": "P6552",
                  "hash": "892c3c817828cf4f367e6f34e11cb487e9af3b20",
                  "datavalue": {
                    "value": "752743856941125632",
                    "type": "string"
                  },
                  "datatype": "external-id"
                }
              ],
              "P1552": [
                {
                  "snaktype": "value",
                  "property": "P1552",
                  "hash": "62f0039d240f7eeba6c6908a0d8807a6188324a1",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 28378282,
                      "id": "Q28378282"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "91feb88bb3fd89a683767dab82068f915803486e",
                  "datavalue": {
                    "value": {
                      "time": "+2016-07-12T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "f4da88e58bb9b446848b3eed88e75b74e12d6336",
                  "datavalue": {
                    "value": {
                      "time": "+2020-04-24T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P3744",
              "P6552",
              "P1552",
              "P580",
              "P585"
            ],
            "id": "Q21296543$b816b924-4539-0160-f112-bad414d05355",
            "rank": "preferred",
            "references": [
              {
                "hash": "bea8fca4657678b295cfdf96a820c938c9f5cb85",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "dbe2169719a4d35670be97cb831759e77e551db0",
                      "datavalue": {
                        "value": "http://www.startrek.com/article/new-discovery-launch-date-may-2017",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              },
              {
                "hash": "830e0d3d65e6b91e769889d7d1177706b5c1e0ca",
                "snaks": {
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cd8210fc3215a6112ebad72d11663d1a56b14d67",
                      "datavalue": {
                        "value": {
                          "time": "+2018-05-10T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2002",
              "hash": "00aa67544342c82d01d5b7f73ba5000c4ce7e1e8",
              "datavalue": {
                "value": "StarTrekRoom",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$662035C3-AD63-484A-B5B0-6BDF91820C3C",
            "rank": "normal"
          }
        ],
        "P856": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P856",
              "hash": "b6440f81a55aff956ee935d7c866b5075aa0aa47",
              "datavalue": {
                "value": "https://www.cbs.com/shows/star-trek-discovery/",
                "type": "string"
              },
              "datatype": "url"
            },
            "type": "statement",
            "id": "Q21296543$2a44aff3-4080-c492-0a9d-0dde21c8aa90",
            "rank": "normal"
          }
        ],
        "P154": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P154",
              "hash": "95901f004fc1f4659fb20f44d05ff4a057a11b32",
              "datavalue": {
                "value": "Star Trek Discovery logo.svg",
                "type": "string"
              },
              "datatype": "commonsMedia"
            },
            "type": "statement",
            "qualifiers": {
              "P2739": [
                {
                  "snaktype": "value",
                  "property": "P2739",
                  "hash": "11a30fab9e2d2882d76e2905be44e002906a252b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 63643196,
                      "id": "Q63643196"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P2739"
            ],
            "id": "Q21296543$bc3f4b07-4eab-2fa7-9103-d281001b8465",
            "rank": "normal"
          }
        ],
        "P2013": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2013",
              "hash": "7f73a3344619132607f119dc7ebb0083d605d568",
              "datavalue": {
                "value": "StarTrekCBS",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$47340cf6-4cbe-2727-6a4d-1f73a0e13a95",
            "rank": "normal"
          }
        ],
        "P750": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P750",
              "hash": "db2d73f4053eb95a3c9480c8cf9966eaa47ed9c3",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5009281,
                  "id": "Q5009281"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8e5017a9-4f07-b083-eae9-2ea1511a586e",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P750",
              "hash": "fa6caa4ecf52be8a10328adef1360ac99b60685d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 907311,
                  "id": "Q907311"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f23dc085-4c86-9487-e07e-53a4ffdc0213",
            "rank": "normal"
          }
        ],
        "P580": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P580",
              "hash": "f1fc3557f5e586025b6b55d073ca51d6fff1fb12",
              "datavalue": {
                "value": {
                  "time": "+2017-09-24T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 11,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q21296543$56740b79-49a1-1275-2732-199c86b2d2e2",
            "rank": "normal",
            "references": [
              {
                "hash": "9cb802796dbde50f2c8ff1745bb47215b58e62af",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "6c663fd1e3708bacc769e346b6626a96d6724eae",
                      "datavalue": {
                        "value": "http://www.elmundo.es/television/2017/06/24/594d4740e5fdea6e2b8b4579.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          }
        ],
        "P2003": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2003",
              "hash": "218ee39f4c78b2f070ae394e1cbb24f52ae5f492",
              "datavalue": {
                "value": "startrekcbs",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$65223a4a-4e34-d558-2947-0a622473899e",
            "rank": "normal"
          }
        ],
        "P161": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "855d745203a8f050da0c37079f5ec4283fb59538",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 7560935,
                  "id": "Q7560935"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "8b0b371f819dadcaf0f51c34fe64a1d772eb3868",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 40935468,
                      "id": "Q40935468"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$95411328-499b-8303-3d2e-ec8ddcf1ba00",
            "rank": "normal",
            "references": [
              {
                "hash": "3debc89b4461e9c3e250fc8508824c522280a47f",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3595ef10bdee19a6629d8622d0784aef5819e090",
                      "datavalue": {
                        "value": "http://deadline.com/2016/12/star-trek-discovery-sonequa-martin-green-cast-lead-rainsford-1201871015/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "5a0498cd330daa8b5eff307fa715c4a8bba139b0",
                      "datavalue": {
                        "value": {
                          "time": "+2016-12-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "ac913cb538d95ed9febcee7dda203bcc09dc0aa2",
                      "datavalue": {
                        "value": {
                          "text": "‘Star Trek Discovery’: Sonequa Martin-Green Cast As The Lead",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "03de5ccd528f3b5a39ad9476821134748acd07f7",
                      "datavalue": {
                        "value": {
                          "time": "+2016-12-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1683": [
                    {
                      "snaktype": "value",
                      "property": "P1683",
                      "hash": "e3e8223791c8fd1e58c6fbe9b96ba38530460bf7",
                      "datavalue": {
                        "value": {
                          "text": "The Walking Dead‘s Sonequa Martin-Green has landed the lead role of Rainsford in Star Trek: Discovery, the upcoming new series for CBS All Access, CBS’ live streaming and VOD service.",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1476",
                  "P577",
                  "P1683"
                ]
              },
              {
                "hash": "d538542c3e92b11e8232fe9a319fc4ae3f0567d4",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "24120802d5d555cf32ae9d4f44e7142e70c70729",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Main_cast",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "6d379d3dc9b0f47d88220c58bd24cbfb67c812c8",
                      "datavalue": {
                        "value": "Sonequa Martin-Green",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "257003c94266cfe9effa6bbe1b71936cea7c3d16",
                      "datavalue": {
                        "value": "Main cast",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "63f338e06a5c6a981b72dbbc35fe796b568e20a1",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 214289,
                  "id": "Q214289"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "c07eb79c4f8cdf491baa42f19814e4c8f745e473",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 43740811,
                      "id": "Q43740811"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                },
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "ab16af2571234b891448c289d9d1e47086462a37",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 47391140,
                      "id": "Q47391140"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$5e54680b-4f3e-596f-c95e-2b43731f38b7",
            "rank": "normal",
            "references": [
              {
                "hash": "2ecfd2ebbb42bec6e42b786af2c8571be9c660fc",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "12ed7ce775acdf5aaedfd41fd0e2dcc0f4cbde62",
                      "datavalue": {
                        "value": "http://www.startrek.com/article/star-trek-discovery-beams-up-three-cast-members",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "07d18bdfef327dbb02bf9d5f4766ccb52a72a9e1",
                      "datavalue": {
                        "value": {
                          "time": "+2016-11-30T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "ba0b9cc206f04a407ae61659f1b7e27d72afc68b",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery Beams Up Three Cast Members",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "69839f8f0327e12353869bde1116e4beaa0a9edb",
                      "datavalue": {
                        "value": {
                          "time": "+2016-11-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1683": [
                    {
                      "snaktype": "value",
                      "property": "P1683",
                      "hash": "eee150fb6b69537055f88d687dff851e59ca1739",
                      "datavalue": {
                        "value": {
                          "text": "Doug Jones, Michelle Yeoh and Anthony Rapp have been announced as the first three actors cast for Star Trek: Discovery.",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1476",
                  "P577",
                  "P1683"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "eb9d9696eaadda0137d8916c9cb3489e7d5b85cb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 39983,
                  "id": "Q39983"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "70e1bc0558369d4378bf612d6a93b83abc824686",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 42716550,
                      "id": "Q42716550"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$f1b5bb34-4f62-fe4f-9144-2d88ad867ba1",
            "rank": "normal",
            "references": [
              {
                "hash": "2ecfd2ebbb42bec6e42b786af2c8571be9c660fc",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "12ed7ce775acdf5aaedfd41fd0e2dcc0f4cbde62",
                      "datavalue": {
                        "value": "http://www.startrek.com/article/star-trek-discovery-beams-up-three-cast-members",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "07d18bdfef327dbb02bf9d5f4766ccb52a72a9e1",
                      "datavalue": {
                        "value": {
                          "time": "+2016-11-30T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "ba0b9cc206f04a407ae61659f1b7e27d72afc68b",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery Beams Up Three Cast Members",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "69839f8f0327e12353869bde1116e4beaa0a9edb",
                      "datavalue": {
                        "value": {
                          "time": "+2016-11-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1683": [
                    {
                      "snaktype": "value",
                      "property": "P1683",
                      "hash": "eee150fb6b69537055f88d687dff851e59ca1739",
                      "datavalue": {
                        "value": {
                          "text": "Doug Jones, Michelle Yeoh and Anthony Rapp have been announced as the first three actors cast for Star Trek: Discovery.",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1476",
                  "P577",
                  "P1683"
                ]
              },
              {
                "hash": "42e3c976c79b2f4cf439d51588981d577a67d765",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "24120802d5d555cf32ae9d4f44e7142e70c70729",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Main_cast",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "530b6bda3eb46e82b7aacd9abed5cd090367fc19",
                      "datavalue": {
                        "value": "Anthony Rapp",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "257003c94266cfe9effa6bbe1b71936cea7c3d16",
                      "datavalue": {
                        "value": "Main cast",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              },
              {
                "hash": "a07b3a497d579251157d8945c2eff6a36767443b",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "41dc7cea0edae5855be461c81d91094c5f7b75d7",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/de/wiki/Star_Trek:_Discovery?oldid=719916#Hauptcharaktere_und_Darsteller",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "530b6bda3eb46e82b7aacd9abed5cd090367fc19",
                      "datavalue": {
                        "value": "Anthony Rapp",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "10f8e4b6b842842dc21fe3a6c760fa63648c9a80",
                      "datavalue": {
                        "value": "Hauptcharaktere und Darsteller",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a3d754cdfb4749778ed36ae3a8056bb459ae0bb8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 461309,
                  "id": "Q461309"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "52a43dcb6692682dfa98f4328a28102e7cfa3a07",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 42713428,
                      "id": "Q42713428"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$2df5e274-49e2-3297-c907-90dadb19c60d",
            "rank": "normal",
            "references": [
              {
                "hash": "2ecfd2ebbb42bec6e42b786af2c8571be9c660fc",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "12ed7ce775acdf5aaedfd41fd0e2dcc0f4cbde62",
                      "datavalue": {
                        "value": "http://www.startrek.com/article/star-trek-discovery-beams-up-three-cast-members",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "07d18bdfef327dbb02bf9d5f4766ccb52a72a9e1",
                      "datavalue": {
                        "value": {
                          "time": "+2016-11-30T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "ba0b9cc206f04a407ae61659f1b7e27d72afc68b",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery Beams Up Three Cast Members",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "69839f8f0327e12353869bde1116e4beaa0a9edb",
                      "datavalue": {
                        "value": {
                          "time": "+2016-11-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1683": [
                    {
                      "snaktype": "value",
                      "property": "P1683",
                      "hash": "eee150fb6b69537055f88d687dff851e59ca1739",
                      "datavalue": {
                        "value": {
                          "text": "Doug Jones, Michelle Yeoh and Anthony Rapp have been announced as the first three actors cast for Star Trek: Discovery.",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1476",
                  "P577",
                  "P1683"
                ]
              },
              {
                "hash": "49a9bf8be6773297b8c55e191a43153e6e6850ff",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "24120802d5d555cf32ae9d4f44e7142e70c70729",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Main_cast",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "e3e69bd6c461288fd0599059f33c1135115eccbf",
                      "datavalue": {
                        "value": "Doug Jones",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "257003c94266cfe9effa6bbe1b71936cea7c3d16",
                      "datavalue": {
                        "value": "Main cast",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              },
              {
                "hash": "815305ce8f519b6ca223b03a7b78c6258b92b4d8",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "41dc7cea0edae5855be461c81d91094c5f7b75d7",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/de/wiki/Star_Trek:_Discovery?oldid=719916#Hauptcharaktere_und_Darsteller",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "e3e69bd6c461288fd0599059f33c1135115eccbf",
                      "datavalue": {
                        "value": "Doug Jones",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "10f8e4b6b842842dc21fe3a6c760fa63648c9a80",
                      "datavalue": {
                        "value": "Hauptcharaktere und Darsteller",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a1d41b86853a8b678b6653b7e2ab457593ec05bf",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 28921867,
                  "id": "Q28921867"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "41337562987543345e956e0433916af90c2f3dcf",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 43217835,
                      "id": "Q43217835"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$e014fd65-4774-35b6-e07a-738f785584a9",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              },
              {
                "hash": "a3504e5657147317c07ec4c47e6e2b8572ae7f58",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "24120802d5d555cf32ae9d4f44e7142e70c70729",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Main_cast",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "ba6107d732a21607d59dfd96d5e0772453c77025",
                      "datavalue": {
                        "value": "Mary Wiseman",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "257003c94266cfe9effa6bbe1b71936cea7c3d16",
                      "datavalue": {
                        "value": "Main cast",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              },
              {
                "hash": "a36822400401ac13942f690a2375cc73dbe86ca7",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "41dc7cea0edae5855be461c81d91094c5f7b75d7",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/de/wiki/Star_Trek:_Discovery?oldid=719916#Hauptcharaktere_und_Darsteller",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "ba6107d732a21607d59dfd96d5e0772453c77025",
                      "datavalue": {
                        "value": "Mary Wiseman",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "10f8e4b6b842842dc21fe3a6c760fa63648c9a80",
                      "datavalue": {
                        "value": "Hauptcharaktere und Darsteller",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "f3fa8e58e14e3193793df0537b2f64669cdb7107",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 535507,
                  "id": "Q535507"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "d452989533ddb58c962be7616b709fd9fa5d578d",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 2712069,
                      "id": "Q2712069"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$7d6e5418-4256-25e5-c5d5-484da2545d01",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "dd66b3256cc493c4e150275e5de714bac28a88eb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 7491731,
                  "id": "Q7491731"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "a875f23d802ceebff819dfff1190df011628253d",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 44569965,
                      "id": "Q44569965"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$69d4581e-49aa-b340-8ff8-b613e6e69841",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "28d19bbbcdd3bb8109bd92eb86d118b0a983df5f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 50359274,
                  "id": "Q50359274"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f84dc30f-4d6b-adfe-6609-8e089ac48f42",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "f0cc6c766870f8a9f19ce02d0418e972f3e6c3e4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 63124741,
                  "id": "Q63124741"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f42840cc-404d-b76c-b624-76ee204d9339",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "00ea50bf1f811a5aa229f8ad83d05dcfa73c979e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 214223,
                  "id": "Q214223"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "df0a9a2cf0073b7a7123b57589f4dc8dfcf86658",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 41796329,
                      "id": "Q41796329"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$dff3d79f-4305-f586-f3d1-41b5a923c953",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "f905b229f5458c6a3403ef4cae58dd004969f1fd",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 449561,
                  "id": "Q449561"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "131a834cf8445fbb4655455b4d5d56706c83717a",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 48080009,
                      "id": "Q48080009"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$31A62E9D-A721-407D-848B-7C5E13A424FB",
            "rank": "normal",
            "references": [
              {
                "hash": "697ebe753b838814bf6eb9bc6d52bbae34d1a790",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "5b1d8822665b93354ad9e43cfd669997cf9bf44e",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 3561957,
                          "id": "Q3561957"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "7cd6c71a65c031ad1e5fb731a6430617cdea8386",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 349548,
                  "id": "Q349548"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "b7b5656ecf47216f5ae806f781b6835b2d04f04f",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 3127322,
                      "id": "Q3127322"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$97ED922D-1D1E-4860-A411-B19B927F68CC",
            "rank": "normal",
            "references": [
              {
                "hash": "697ebe753b838814bf6eb9bc6d52bbae34d1a790",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "5b1d8822665b93354ad9e43cfd669997cf9bf44e",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 3561957,
                          "id": "Q3561957"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              },
              {
                "hash": "7fe23955863cb4f4c52cdab697f4996e2a0d5968",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3eee7a308a5baccca1f9452bfac6dd1728398b9d",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Recurring_characters",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "f28a6b47d811a96ab793e01d1ceed8189755a9f5",
                      "datavalue": {
                        "value": "Rainn Wilson",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "396ed367eeb3ac6787adb5b136822d9c37fcc26d",
                      "datavalue": {
                        "value": "Recurring characters",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "0876b7330daf7ad1e09ca45c5bfc4d801a84c765",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3270529,
                  "id": "Q3270529"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$CC5C6153-A49A-4803-A6FF-60DE91F1AAB8",
            "rank": "normal",
            "references": [
              {
                "hash": "697ebe753b838814bf6eb9bc6d52bbae34d1a790",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "5b1d8822665b93354ad9e43cfd669997cf9bf44e",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 3561957,
                          "id": "Q3561957"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              },
              {
                "hash": "f25e93f677b52b04e335620bd5d91e55ba651267",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "eb0261fbdf0d3ab5f9ebac76592732828120d2ec",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "cd1aa43c3f50deb30b87be484d9dbac0cb19e0fa",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 516483,
                  "id": "Q516483"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8473AF48-4554-405D-BA53-A4E769D5A9EB",
            "rank": "normal",
            "references": [
              {
                "hash": "697ebe753b838814bf6eb9bc6d52bbae34d1a790",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "5b1d8822665b93354ad9e43cfd669997cf9bf44e",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 3561957,
                          "id": "Q3561957"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "3a015798a957facf361daa7d902cd2aecb723343",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 16201541,
                  "id": "Q16201541"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$99CBCC25-F293-4412-89AF-9E2F2671BEE9",
            "rank": "normal",
            "references": [
              {
                "hash": "697ebe753b838814bf6eb9bc6d52bbae34d1a790",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "5b1d8822665b93354ad9e43cfd669997cf9bf44e",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 3561957,
                          "id": "Q3561957"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "40a966d06b889a87add1760fbf7b6dbc666f90f4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 231660,
                  "id": "Q231660"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "904e4179b8ae1ac9696d1b49d705308f675c1a18",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1412447,
                      "id": "Q1412447"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$90799e82-41fa-93ac-93e4-d3679ec2f9c9",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "80ca11baed95e04a16a061ad7c89b940ed6bce46",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1190037,
                  "id": "Q1190037"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "9214e3df2dd7ead73fb2514680f92cfdae2de1fd",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 48032489,
                      "id": "Q48032489"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$328309ad-48b9-efde-2736-1a17d402f53b",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "20ffef8b1d77094f7c48a1c2f89a90335fa7f363",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 30039197,
                  "id": "Q30039197"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "add582544d6971750edfdcb4d233def4cfafcc28",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 48078634,
                      "id": "Q48078634"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$f64a2bcb-4dda-d513-f15f-9ef75f8feea5",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "3db1a1f3fab3a835009d49e4fd4995dab3b94381",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 651681,
                  "id": "Q651681"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b971d537-4953-fd61-3ed2-fe3272062c53",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a6fe6dc3a43c010a5162536253a26788781c9634",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 50974754,
                  "id": "Q50974754"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "3f8daead9aa4d9d219f3eb7ef6563d45c92ae649",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 48081407,
                      "id": "Q48081407"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$9f976eec-4026-733b-bce4-a939b0b358a0",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "80e451635123f7b567789183b2a14c9fbc5743c9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 570006,
                  "id": "Q570006"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "5d81ca3ce32efaff6500d00dfa0f2fa9291e1d25",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 612625,
                      "id": "Q612625"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$c65aa3b8-490b-2c22-d55b-fc04af44bb39",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              },
              {
                "hash": "7bc6a61d4b9b87c3a010a4849d3e9c473311ce56",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "24120802d5d555cf32ae9d4f44e7142e70c70729",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Main_cast",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "f08ef18212fe2670c3af9176530528fe13eb2a2e",
                      "datavalue": {
                        "value": "Anson Mount",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "257003c94266cfe9effa6bbe1b71936cea7c3d16",
                      "datavalue": {
                        "value": "Main cast",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "16323383df873f81ad8d587458c7847f584daf62",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 732763,
                  "id": "Q732763"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$3f6fb56f-4cde-9a34-b020-060a55068443",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "c25bb88f0635fd8d4d1d57f2b16c359ef8b32b13",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68038158,
                  "id": "Q68038158"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "8b0b371f819dadcaf0f51c34fe64a1d772eb3868",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 40935468,
                      "id": "Q40935468"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$9f7aa2d5-429f-fd78-7a9a-cd330ecd6cc5",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "43ebe8114e872d9de89224494ec295577f6d09cb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 67648349,
                  "id": "Q67648349"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$2968de53-404d-bd78-b2e5-10d77b8b8e11",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "33a229780d3baef252a549003847ddd4ca5d7196",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 24963319,
                  "id": "Q24963319"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "8b6b4d1975000aa7519c45c6a99b95dca9cf46db",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 62077334,
                      "id": "Q62077334"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$4db5eaba-4a2b-13ca-8d05-985153de11e9",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "2112b34d53b894668cdfb8fc87eaace3345b11e6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 16145966,
                  "id": "Q16145966"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f3291795-44ce-bc73-f983-2abbd560992e",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "607f6ace07ba5234fe49689572d76633171caa2a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68339088,
                  "id": "Q68339088"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$22549a55-47d4-63d5-d714-38e0d88868c7",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "9183443bafbb9e7c5ffc7d96d3ced0352f7a0bf8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1338610,
                  "id": "Q1338610"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$941d4731-4cc4-a51d-42ec-b0527a9f4ca2",
            "rank": "normal",
            "references": [
              {
                "hash": "f65b3edff707083319cb55ef4c0bdd4225c5deb5",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1e656ab4cf6f9d63a8c9f449f2c9dfbff36a5bf2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "8fc2a46ee62b5eedb27cf649da1f9ccf81116604",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1320452,
                  "id": "Q1320452"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "404acfe78cd43361264bdbec4e70e7290a01f596",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 16341,
                      "id": "Q16341"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$476f7011-4418-0450-b4f8-ef6be31f4199",
            "rank": "normal",
            "references": [
              {
                "hash": "abfd2af540c4340dc6fed86658ee3ccec2989684",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              },
              {
                "hash": "55b393aa0de25937830e066c13d202233bea16ac",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3eee7a308a5baccca1f9452bfac6dd1728398b9d",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Recurring_characters",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "40d0353e01675bd149782b1b8c239f3fe471ebe3",
                      "datavalue": {
                        "value": "Ethan Peck",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "396ed367eeb3ac6787adb5b136822d9c37fcc26d",
                      "datavalue": {
                        "value": "Recurring characters",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "321d47450c8b17e0cd05ac57b4722dc7e036bbb3",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 16911059,
                  "id": "Q16911059"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$96c1cd2e-4418-43b4-568b-8dbd29e40c8c",
            "rank": "normal",
            "references": [
              {
                "hash": "abfd2af540c4340dc6fed86658ee3ccec2989684",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "d2658c3cdded33e67500adc39aa39cd657fa448a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 57002079,
                  "id": "Q57002079"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b58e432c-462c-9d7f-7bde-e3191d2959ee",
            "rank": "normal",
            "references": [
              {
                "hash": "abfd2af540c4340dc6fed86658ee3ccec2989684",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "50e1de7d5627d57ca09045fdfd9492b458903c2f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68441369,
                  "id": "Q68441369"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$7b3fb8d0-4217-2402-30de-56e8bd778faf",
            "rank": "normal",
            "references": [
              {
                "hash": "abfd2af540c4340dc6fed86658ee3ccec2989684",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "963d3a95712c946551b09c09a5812bffaa0857ef",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 62077689,
                  "id": "Q62077689"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$2243d91f-45af-a268-00fb-1071b787f940",
            "rank": "normal",
            "references": [
              {
                "hash": "abfd2af540c4340dc6fed86658ee3ccec2989684",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a650b5df8a2499cfc1522c1abb6e6686d2452ecb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 948310,
                  "id": "Q948310"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$7f6b5072-4b27-1e58-2a59-7b1451884d29",
            "rank": "normal",
            "references": [
              {
                "hash": "9a017996159798a89285ff1f41f7ec0130b6afcf",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "8cf46a026d6ff2c325c87fe0dd348ae391c6aeac",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68492294,
                  "id": "Q68492294"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$3a465ff8-414e-82e3-5b81-a45a7c0fadec",
            "rank": "normal",
            "references": [
              {
                "hash": "9a017996159798a89285ff1f41f7ec0130b6afcf",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "0c6ba68d02ce7f1e9758161fe5964fa98b7a8fbf",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 42418858,
                  "id": "Q42418858"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$815e97df-4f34-b715-8f8b-89220e62d6ae",
            "rank": "normal",
            "references": [
              {
                "hash": "9a017996159798a89285ff1f41f7ec0130b6afcf",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "75d4e4aa4b51cf29fe81b340084506ddc73a517f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "31021ae34ead834d6da5cb4dd135ff488c9f311a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3515945,
                  "id": "Q3515945"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$c4ba4c7e-47f9-14db-f81a-0c616d9cec21",
            "rank": "normal",
            "references": [
              {
                "hash": "92e127d08a68ca51cf8475288908d5b32c7edac2",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "c78f8833479c2d59b64c97c362661eb3887cf8e4",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-25T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "792cb4a4d3d3bf76511e6aee997797582b2be4c4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 7801308,
                  "id": "Q7801308"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$c79de180-4b39-eda3-60b6-ec634c7b603b",
            "rank": "normal",
            "references": [
              {
                "hash": "5e4eccb0ab125a098f610d37aa031a255ab99705",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e31edae43233ad56359523b1078be66486186ede",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "5fd830808495f98a5a64961dbbaf8df8d7679830",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68630001,
                  "id": "Q68630001"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$508793af-470f-edd2-79ab-d5c924d07823",
            "rank": "normal",
            "references": [
              {
                "hash": "5e4eccb0ab125a098f610d37aa031a255ab99705",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e31edae43233ad56359523b1078be66486186ede",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              },
              {
                "hash": "980c7763a0082c5be611aa32d12601ed16a11484",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3eee7a308a5baccca1f9452bfac6dd1728398b9d",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Recurring_characters",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "849a42db6abb34506b2bc1821bfb5f566eb5ada1",
                      "datavalue": {
                        "value": "Ali Momen",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "396ed367eeb3ac6787adb5b136822d9c37fcc26d",
                      "datavalue": {
                        "value": "Recurring characters",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "d4c3ea2812b13fe8f0e3cb5a86fbb431b4a02688",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68647093,
                  "id": "Q68647093"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$0bce4fd5-4974-77ab-e11b-326c21cfc887",
            "rank": "normal",
            "references": [
              {
                "hash": "5e4eccb0ab125a098f610d37aa031a255ab99705",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e31edae43233ad56359523b1078be66486186ede",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              },
              {
                "hash": "69ea9361779da69a21247622a8cc317a30c93a88",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3eee7a308a5baccca1f9452bfac6dd1728398b9d",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Recurring_characters",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "1725ad09b31c0970d23748067a33478325c7711a",
                      "datavalue": {
                        "value": "Bahia Watson",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "396ed367eeb3ac6787adb5b136822d9c37fcc26d",
                      "datavalue": {
                        "value": "Recurring characters",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "0628ebd4168b707686e169003841572501a6ab31",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5162503,
                  "id": "Q5162503"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$4b802c92-4666-f951-2734-cc82eb89369e",
            "rank": "normal",
            "references": [
              {
                "hash": "f25e93f677b52b04e335620bd5d91e55ba651267",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "eb0261fbdf0d3ab5f9ebac76592732828120d2ec",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "91964eb1d4c62932d1eec350b20fdc7e6a7479eb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68775694,
                  "id": "Q68775694"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$594e1954-49d0-86d2-135c-81eee2ba02c8",
            "rank": "normal",
            "references": [
              {
                "hash": "f25e93f677b52b04e335620bd5d91e55ba651267",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "eb0261fbdf0d3ab5f9ebac76592732828120d2ec",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "6f9d170bb40b1117337ea535ae19b509e09cca9e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 68817272,
                  "id": "Q68817272"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$04007318-4cf3-8c57-6f3a-cac729b23f03",
            "rank": "normal",
            "references": [
              {
                "hash": "f25e93f677b52b04e335620bd5d91e55ba651267",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "eb0261fbdf0d3ab5f9ebac76592732828120d2ec",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "43358f35beba60070b1b088c3c1c36616a86d34d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 52236130,
                  "id": "Q52236130"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$e4aedf1d-4a13-f040-7ed1-3a548127237f",
            "rank": "normal",
            "references": [
              {
                "hash": "038bbc13b68d1160ec7f8244f082d8b058811cc2",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "50ef68ec1b41a6ea7968b1b15d54c03db6f692f9",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a4447469c46e11ad5245821344fa6b59badff846",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 63285715,
                  "id": "Q63285715"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$325b4261-4f1c-e4d8-16ec-598a40a8f45d",
            "rank": "normal",
            "references": [
              {
                "hash": "038bbc13b68d1160ec7f8244f082d8b058811cc2",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "50ef68ec1b41a6ea7968b1b15d54c03db6f692f9",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "0b1ef81431267b48e848fd3635e0ba6d9f6e59b5",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69054814,
                  "id": "Q69054814"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f7b77b5e-43bf-0193-c714-5ffdf509a291",
            "rank": "normal",
            "references": [
              {
                "hash": "7b8fbe1a9c1b950a30bd8a6d39cfbb3fcd22a637",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "186ff288ba97a69a10d97967d90243c601816ed8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "fcf2c8bd8f32dc708c77345e45355333c87c8afe",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69087443,
                  "id": "Q69087443"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "404acfe78cd43361264bdbec4e70e7290a01f596",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 16341,
                      "id": "Q16341"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$4e956f62-41ca-87d7-60a7-36289ae0d69e",
            "rank": "normal",
            "references": [
              {
                "hash": "7b8fbe1a9c1b950a30bd8a6d39cfbb3fcd22a637",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "186ff288ba97a69a10d97967d90243c601816ed8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "365c8b909e81624aa8e47354602593132abe49a4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69506379,
                  "id": "Q69506379"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$82686757-4abf-1805-ed28-1eab9e0c41e3",
            "rank": "normal",
            "references": [
              {
                "hash": "a5fd884d58484ce2b8ab20aceb2c5b159c627ad8",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "777797883908e289524fd7301cd9a4cf7fc26bff",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "9cfec0a6ff1c4e7121ee34e8749c5988079f651e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 202792,
                  "id": "Q202792"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "e53b485d37982a4f492dbef62ec22899e6ef144f",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1568510,
                      "id": "Q1568510"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$7e885192-459a-2d8d-bfe3-242f4fd609b4",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              },
              {
                "hash": "d8429ad5e89a4a0dfc1cefad6062f510a461e5da",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3eee7a308a5baccca1f9452bfac6dd1728398b9d",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Recurring_characters",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "a07c85146ad84d945189eae2bab4c553fe5412bc",
                      "datavalue": {
                        "value": "Rebecca Romijn",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "396ed367eeb3ac6787adb5b136822d9c37fcc26d",
                      "datavalue": {
                        "value": "Recurring characters",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "2a8b2ace565675e0f7d555d248a76d4beba569b5",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 441836,
                  "id": "Q441836"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8a58bcd4-427a-e052-4ef5-b0af471f368c",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "8b5f77ba4a9af79643dc7864355951bd5bd20c45",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69525944,
                  "id": "Q69525944"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$3d64f37a-4390-a23b-d447-6cc89823098a",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              },
              {
                "hash": "9bc65bc632b6c3b7fb96261b111c45976f4111fd",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3eee7a308a5baccca1f9452bfac6dd1728398b9d",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/wiki/Star_Trek:_Discovery?oldid=2393120#Recurring_characters",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "64f2ad61689e5c7189880cfdfc220db18d510b56",
                      "datavalue": {
                        "value": "Christopher Russell",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ],
                  "P958": [
                    {
                      "snaktype": "value",
                      "property": "P958",
                      "hash": "396ed367eeb3ac6787adb5b136822d9c37fcc26d",
                      "datavalue": {
                        "value": "Recurring characters",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810",
                  "P958"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "384bc3a8178c4dc27c2e6100121601b166634308",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69527493,
                  "id": "Q69527493"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$cf5acda7-4f80-ea33-4a4d-3527506a1f07",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "9f66bd3fbc740adfba01f75081f59bbd1b73d7de",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69544731,
                  "id": "Q69544731"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$3bbe2f25-4cf9-aa28-0f61-2fbdf9bf3ea4",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "c85de3950368525cf415b27b40af66dc158c25ff",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 56927373,
                  "id": "Q56927373"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P453": [
                {
                  "snaktype": "value",
                  "property": "P453",
                  "hash": "159d21a7ff0a8ad1c9a3c6947b93731784734405",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 56926823,
                      "id": "Q56926823"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P453"
            ],
            "id": "Q21296543$6ebf9d3c-4d83-bf02-e1cf-e43860343778",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "1ab78ec82f8d46d035c3ec508577afb7ea6482ca",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1990966,
                  "id": "Q1990966"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$e1d1f8e8-4193-5615-b955-91c078f54e8f",
            "rank": "normal",
            "references": [
              {
                "hash": "8db1f5b2d5093aa416822b29933ffce71d34a99b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8699bfda9ce9d1794a3050693fc9d352b816e567",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "1d9d000302d16c98dd06d52b78c2539472e8c90e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69841809,
                  "id": "Q69841809"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$4c0b1b5e-4852-37bd-3c67-64972d9e7a70",
            "rank": "normal",
            "references": [
              {
                "hash": "a3b8e9a7f8aac137f6e8c788d483943a4801785b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1f53dc24793188c0a5a134af78600c50b44ce4c8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-06T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "64be8a350ebae0b30f91f673bdcc0b6c08d033ab",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5317847,
                  "id": "Q5317847"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$761ce163-4907-39e8-51e4-e46474544e92",
            "rank": "normal",
            "references": [
              {
                "hash": "a3b8e9a7f8aac137f6e8c788d483943a4801785b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1f53dc24793188c0a5a134af78600c50b44ce4c8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-06T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "09549c50e1c4381f9115b5c9a682739f3e92b873",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69903446,
                  "id": "Q69903446"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$6b82c43c-4b4f-e826-f342-1bc98d0851a5",
            "rank": "normal",
            "references": [
              {
                "hash": "a3b8e9a7f8aac137f6e8c788d483943a4801785b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1f53dc24793188c0a5a134af78600c50b44ce4c8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-06T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "afb9812619dda5efff62181afc4b8c4299a7ffb8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2837131,
                  "id": "Q2837131"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$9045732d-4cf3-f325-9214-bcc06147e048",
            "rank": "normal",
            "references": [
              {
                "hash": "f71ee5a29ad4a4dc6c18bcef57e8fd4808f9bb64",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "b1b2416dc558aac38cb000a3632a2d4d928e6fe0",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-07T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "99cf73225f29238ef1a3228d69b3112d5904893e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 69974862,
                  "id": "Q69974862"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$431b9011-4368-8c6d-da51-ce220eb0367d",
            "rank": "normal",
            "references": [
              {
                "hash": "f71ee5a29ad4a4dc6c18bcef57e8fd4808f9bb64",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "b1b2416dc558aac38cb000a3632a2d4d928e6fe0",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-07T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "42aa338a02bcfb6be5450601a3b5a31f40f35b59",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 59579779,
                  "id": "Q59579779"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f8170225-48fe-e461-1336-876194c81c86",
            "rank": "normal",
            "references": [
              {
                "hash": "f71ee5a29ad4a4dc6c18bcef57e8fd4808f9bb64",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "b1b2416dc558aac38cb000a3632a2d4d928e6fe0",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-07T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "db83a4db7c8318c1d681a26b9d329b966d7ad1cf",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 70357284,
                  "id": "Q70357284"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$da0d261e-4828-7283-bc0b-b686a59a00a9",
            "rank": "normal",
            "references": [
              {
                "hash": "0c40607eca5fb4e0147b51e343376612bb570971",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "29e5b060b3fa4398327f14fdc9c3c8a45e3bb67f",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-10T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "459e598588294aa4f2bb4c81accf4454edfa3a1f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 70846755,
                  "id": "Q70846755"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$bb541762-46e1-f381-fa72-08485d47323c",
            "rank": "normal",
            "references": [
              {
                "hash": "c91873864385e1cd49443890b41062610b1cdfff",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "f89fe76d36f9a99298132059bffc453af2fcb505",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a45d4ab35535700c41bbe36deede961234a4845b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 70873739,
                  "id": "Q70873739"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$a21c7eb4-4fc8-cc6b-07cc-4e6efcfbdb4a",
            "rank": "normal",
            "references": [
              {
                "hash": "c91873864385e1cd49443890b41062610b1cdfff",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "f89fe76d36f9a99298132059bffc453af2fcb505",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "fcc9d9455f1712afc55bfa1986507c03278f82af",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 71106466,
                  "id": "Q71106466"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$852306e6-4428-19ae-31a2-a0fef27e8d55",
            "rank": "normal",
            "references": [
              {
                "hash": "c91873864385e1cd49443890b41062610b1cdfff",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "f89fe76d36f9a99298132059bffc453af2fcb505",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "70afd293e42893305349d9194c1d1a96b054efd5",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 71358379,
                  "id": "Q71358379"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b5c1547e-4653-e547-ad01-e5fc3ad09112",
            "rank": "normal",
            "references": [
              {
                "hash": "ae9e6dc50ebc1b56298436f29e55d0ec3bba7eab",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8febdffd5b895f0a6a793e2d422ade4fa3e25490",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-18T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "2c57c25db85f2d7fcec594218c06a7708a0bc76b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 434844,
                  "id": "Q434844"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$43d2f4ea-42b3-6e6a-8070-754f73399e21",
            "rank": "normal",
            "references": [
              {
                "hash": "30dbcb2003b8cd9641b9196400fd234b1c6becc8",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "34c54e4fe19e29e3fa210a5a882c96e8e6252672",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-21T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "dfe5a37de186ea5ca4856b55de21b9fd28777244",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 57452613,
                  "id": "Q57452613"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$098fba33-423d-1355-b24e-fa5185d6937d",
            "rank": "normal",
            "references": [
              {
                "hash": "30dbcb2003b8cd9641b9196400fd234b1c6becc8",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "34c54e4fe19e29e3fa210a5a882c96e8e6252672",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-21T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "e57a2cc0adee3f7c8a8b9568f818b24828f024a2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 24335234,
                  "id": "Q24335234"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b723339c-422b-ce79-d75c-e0a4c4fde82a",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "d22c0b881bf4c8ec64956263386c1efa920aed01",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3163137,
                  "id": "Q3163137"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$29430cb2-4810-6457-881c-9f626e776d42",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "65a909062fdb702acfad68f2e596a018235dec90",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 233575,
                  "id": "Q233575"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$83aaf9b8-441a-f342-795b-38b3e92f8b17",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "df244bd898965c42b4c98ef3f891abc1b9c5a2e6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5591276,
                  "id": "Q5591276"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b06e33de-4fa6-2760-6a82-432a7f1ab5d4",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "86424cb6f6d949edca5a4c946ab0a82570cc4a08",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 71971463,
                  "id": "Q71971463"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$cca8004f-4d77-e089-1b7e-78b80a153122",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "ebbce305303c09d46c66e22e403755caccca05e2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 57002298,
                  "id": "Q57002298"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$5411b7e2-405e-149f-240b-a85a22c8ccd7",
            "rank": "normal",
            "references": [
              {
                "hash": "38c866342436e40b364dfac006c6869e85fd7513",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "7812473f3f3d1013f3c1e23e0e11047ece0c2a9c",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-22T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "f1636d8342acd901dcd6481ad43564543f087491",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1101612,
                  "id": "Q1101612"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$a4fa6ee7-4d0e-8359-a431-024c0a0ece42",
            "rank": "normal",
            "references": [
              {
                "hash": "5e99171d1e47b8219d81f59248b333147392105e",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "87831f7d7ffb41d1a72efc77c457e3a26f9e30c8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-23T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "10342e83ff471475b1a2bae550b9aad711d33b2a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 72147765,
                  "id": "Q72147765"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$6a2a3715-4779-9770-764f-3c4b77db35fd",
            "rank": "normal",
            "references": [
              {
                "hash": "73b48e7f993c79ba5d9db3ffe7d33cce4327fb05",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "6dbcd98a0f10be08c2231d95a76187f29feb5e70",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "91e56f037d97aba208f251d3daf39c71163bfbea",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 6162357,
                  "id": "Q6162357"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$617e822a-420d-86e4-4210-fd9584c2736e",
            "rank": "normal",
            "references": [
              {
                "hash": "73b48e7f993c79ba5d9db3ffe7d33cce4327fb05",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "6dbcd98a0f10be08c2231d95a76187f29feb5e70",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a9f85c55c6c8a2bdcd046b17454db02d00d0b4da",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2903668,
                  "id": "Q2903668"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8ab910b4-4a76-c4c0-1eba-de43091a761e",
            "rank": "normal",
            "references": [
              {
                "hash": "73b48e7f993c79ba5d9db3ffe7d33cce4327fb05",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "6dbcd98a0f10be08c2231d95a76187f29feb5e70",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-24T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "e0b0b8e5266d36bd321d890a5ca676e65c12b319",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 72230620,
                  "id": "Q72230620"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$d9053335-4514-12b6-4005-acca33649af6",
            "rank": "normal",
            "references": [
              {
                "hash": "11f0e405003349d8e0f72804d60ecd4296a9cfec",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "0aa69b6ec91b09354368b5079a732ffe7488c857",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-25T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "120b396aa864821c14f64d73f65ae3e25608b2b4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 72366928,
                  "id": "Q72366928"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$e7a2cbbc-4d07-0ffe-33ec-c7f5fbc518f0",
            "rank": "normal",
            "references": [
              {
                "hash": "ca56134cd1eae61107993f598efe55513237b51e",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "2934796778fa3d5ee75be6c5e17b4a00ec621252",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "0fc729a2f4094dfa7681c4d5092948243ebf0de8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5162584,
                  "id": "Q5162584"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b5232352-4454-b3c3-7a77-8e3ec9ece07b",
            "rank": "normal",
            "references": [
              {
                "hash": "ca56134cd1eae61107993f598efe55513237b51e",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "2934796778fa3d5ee75be6c5e17b4a00ec621252",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "433e0e56c6462e7e443ed11d16de5ead2386a961",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 72577921,
                  "id": "Q72577921"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$53fb6e2f-4ee9-1fe3-3192-062f5c33427d",
            "rank": "normal",
            "references": [
              {
                "hash": "b42e954986762051c8e5d323bfbd793158f3ba12",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "77ebde15945a605baeba3e02eb8d0b6f29a224b9",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "6a7da5bacd136c29ae8eb8a50139b148beff9cf0",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 72670384,
                  "id": "Q72670384"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f3cf1af6-4542-4bf9-e47f-5fccb51c75f3",
            "rank": "normal",
            "references": [
              {
                "hash": "1a815f9270ed93d78929c995abe15f56577b3e5b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "64e6644766e4e3a89226fe67a8eddc11ce7e40a6",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "f4da539c5221922970ee05df88c674d6edc2094d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 66819366,
                  "id": "Q66819366"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$ec5be7c8-456e-d240-e461-14227e135962",
            "rank": "normal",
            "references": [
              {
                "hash": "1a815f9270ed93d78929c995abe15f56577b3e5b",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "64e6644766e4e3a89226fe67a8eddc11ce7e40a6",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-29T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "9d2e50e9e9bbe685101ad9d9485175da231bf27b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 72941488,
                  "id": "Q72941488"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$40adc2b4-493a-bd44-2eca-2608c2a3814c",
            "rank": "normal",
            "references": [
              {
                "hash": "e641646fb4ec577e4cbedf0ec42359b7340420df",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "250688cad92e074ace49f49c56f5f6c79888ad96",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-30T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "27ce82df9e75139e5ec688eb72e5c4efc7b3835e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 73891277,
                  "id": "Q73891277"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$c2345522-4043-5469-e502-ad8d6908bac7",
            "rank": "normal",
            "references": [
              {
                "hash": "b71e9f76449b886dd2fbf9e37d28160e164a2545",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "b0e92e68055ac0d2e38022e5e6b1775b1ccd7726",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-07T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "684638d796bafdf94d0e787d56a89210c3d9a6df",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 74071333,
                  "id": "Q74071333"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$07e0f515-4ff9-2d7c-da81-19c9000264c0",
            "rank": "normal",
            "references": [
              {
                "hash": "b71e9f76449b886dd2fbf9e37d28160e164a2545",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "b0e92e68055ac0d2e38022e5e6b1775b1ccd7726",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-07T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "2b454c3e8bd4c673835599b8de01a4649a378f3a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 74213433,
                  "id": "Q74213433"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$81b7f208-449f-eefa-6226-5c9ef927645f",
            "rank": "normal",
            "references": [
              {
                "hash": "a54c3fc8e9caa71f476d34abfde931fae442e646",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e2766eda638c7b57d9bb8e38f12a0e44c21e6521",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-11T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "55bd6139c92f790fa721de97f7a8cdb11f38605d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 74520881,
                  "id": "Q74520881"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$c29bb951-454a-d35b-5bd8-e8bcd292f8da",
            "rank": "normal",
            "references": [
              {
                "hash": "a54c3fc8e9caa71f476d34abfde931fae442e646",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e2766eda638c7b57d9bb8e38f12a0e44c21e6521",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-11T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "345c1da84dd6e0400d5fc1fd84cbe4a40b059047",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2569647,
                  "id": "Q2569647"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$3bbcda89-4e15-1188-ed4f-466607ff4fa7",
            "rank": "normal",
            "references": [
              {
                "hash": "a54c3fc8e9caa71f476d34abfde931fae442e646",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e2766eda638c7b57d9bb8e38f12a0e44c21e6521",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-11T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "14ea911f28cf0f536028abe7c0b6a013a5a28a70",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 662257,
                  "id": "Q662257"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$037bd43d-4e35-c289-9d80-20e0b1aefa4d",
            "rank": "normal",
            "references": [
              {
                "hash": "a54c3fc8e9caa71f476d34abfde931fae442e646",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e2766eda638c7b57d9bb8e38f12a0e44c21e6521",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-11T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "4d4571ea0b993e3be51a92d2544ce7af4736a8ff",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 64891312,
                  "id": "Q64891312"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8fcde891-4ddd-cf6a-849b-0c726433b64e",
            "rank": "normal",
            "references": [
              {
                "hash": "a54c3fc8e9caa71f476d34abfde931fae442e646",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e2766eda638c7b57d9bb8e38f12a0e44c21e6521",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-11T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "c80dad392e996b3888d6a9e39d4254260b67cac3",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 74728418,
                  "id": "Q74728418"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f2f644ed-4d33-7ea3-6197-fba1288c1bdd",
            "rank": "normal",
            "references": [
              {
                "hash": "26e4ffdcf96866ae6832252431dfdaf3ce645863",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "3a30b71e3f2b4e0ef568f215352e869ab085b1a8",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "ca3a6ed466c6b47c33a96652b4785d76c12fc929",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 74970086,
                  "id": "Q74970086"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$819954bb-438e-703a-1a41-2ae0b33879f4",
            "rank": "normal",
            "references": [
              {
                "hash": "9a9b2415c6db4f53a2ce050f6e9d0b98d3d069ce",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "d810edcd98d10b5e4bfb7c61af5ffbecd5847217",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5360620,
                  "id": "Q5360620"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$6d9b1365-46e9-58c3-3651-94127a9e15a7",
            "rank": "normal",
            "references": [
              {
                "hash": "358f2d0c01e0559963c064dc280cee8d9726938c",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "d6ca30ed1a46c77845702174620d00b71b7cead6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 77043583,
                  "id": "Q77043583"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$d0767c4f-415a-d706-10bc-aca6240dc073",
            "rank": "normal",
            "references": [
              {
                "hash": "358f2d0c01e0559963c064dc280cee8d9726938c",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "a99f7bebf4d66e62c0506c6806ba65dd20ab34a8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 4942414,
                  "id": "Q4942414"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$99398b55-41e1-69e9-6d1b-7e774b5d79d7",
            "rank": "normal",
            "references": [
              {
                "hash": "358f2d0c01e0559963c064dc280cee8d9726938c",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "3620dbaa5acefe9ad4185b594e47dc19e60b98fc",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 23061598,
                  "id": "Q23061598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$6dc2ac60-4fd7-d582-433a-ab4af277fa72",
            "rank": "normal",
            "references": [
              {
                "hash": "358f2d0c01e0559963c064dc280cee8d9726938c",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "c82c7d2ae7e1424aebd5e663239bfbdc16baa12a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 56062807,
                  "id": "Q56062807"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$ced8d63b-4281-4cde-8189-69cf981e765f",
            "rank": "normal",
            "references": [
              {
                "hash": "3f31c8636740276dd506029a4198e42e8b0bfaff",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e8258c9476277fe87484cda97c7a3838231d32a5",
                      "datavalue": {
                        "value": {
                          "time": "+2020-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P854",
                  "P813"
                ]
              },
              {
                "hash": "c115657cd757119999caee4547a1285ec1ae5c46",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "f5bf7a60c0ce3cc2bb4945f4405f6c3763fcaf9c",
                      "datavalue": {
                        "value": "https://www.cnn.com/2020/09/02/entertainment/star-trek-discovery-nonbinary-transgender-characters/index.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e8258c9476277fe87484cda97c7a3838231d32a5",
                      "datavalue": {
                        "value": {
                          "time": "+2020-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P161",
              "hash": "d1a224ff6c6e7418760b0916cadf722d11339779",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 99673126,
                  "id": "Q99673126"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f21b7f38-4ded-4b25-b56b-731ccda477d4",
            "rank": "normal",
            "references": [
              {
                "hash": "3f31c8636740276dd506029a4198e42e8b0bfaff",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e8258c9476277fe87484cda97c7a3838231d32a5",
                      "datavalue": {
                        "value": {
                          "time": "+2020-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P854",
                  "P813"
                ]
              },
              {
                "hash": "c115657cd757119999caee4547a1285ec1ae5c46",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "f5bf7a60c0ce3cc2bb4945f4405f6c3763fcaf9c",
                      "datavalue": {
                        "value": "https://www.cnn.com/2020/09/02/entertainment/star-trek-discovery-nonbinary-transgender-characters/index.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e8258c9476277fe87484cda97c7a3838231d32a5",
                      "datavalue": {
                        "value": {
                          "time": "+2020-09-27T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P3417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3417",
              "hash": "2acbbfed274e536abe9fc63eafbf20e2f3f2009b",
              "datavalue": {
                "value": "Star-Trek-Discovery-2017-TV-series",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$B0618E03-6FEE-4B07-BB05-DBC1B0DD4B68",
            "rank": "normal"
          }
        ],
        "P2529": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2529",
              "hash": "62ee900737c96118b9b381ed2f85d19ecefce92e",
              "datavalue": {
                "value": "424901",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$6B86A82D-6693-4D03-ACB7-DD9C8726925F",
            "rank": "normal",
            "references": [
              {
                "hash": "3bf39867b037e8e494a8389ae8a03bad6825a7fc",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "5946b91c53409c48f5f1fb0319ed41fc67a764da",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 191168,
                          "id": "Q191168"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P2603": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2603",
              "hash": "41cf791b3c0b6bb08481d9f1d4f7e2de2915b9f9",
              "datavalue": {
                "value": "977754",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$BF20C33F-8E07-4F16-83EE-27DA3BE7C6F8",
            "rank": "normal"
          }
        ],
        "P449": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P449",
              "hash": "3fa507848577a2b89dfa20722c58ba13aa2f730f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 43380,
                  "id": "Q43380"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "f1fc3557f5e586025b6b55d073ca51d6fff1fb12",
                  "datavalue": {
                    "value": {
                      "time": "+2017-09-24T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P582": [
                {
                  "snaktype": "value",
                  "property": "P582",
                  "hash": "dca56860e0dde75d680cc7037a24b603af8fb58d",
                  "datavalue": {
                    "value": {
                      "time": "+2017-09-24T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P580",
              "P582"
            ],
            "id": "Q21296543$2D5B3B9C-82BF-433F-B348-9F02A2A36445",
            "rank": "normal",
            "references": [
              {
                "hash": "ed8bd3f9343e9a35e58b67284f26a67859f1808d",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "07596fc82d3ed4d248b85e5543852cc31e37dc8c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 199913,
                          "id": "Q199913"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P449",
              "hash": "ab1cb30a6a1da2619e6754ce145d09df9bbca49f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 27903045,
                  "id": "Q27903045"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P518": [
                {
                  "snaktype": "value",
                  "property": "P518",
                  "hash": "b32357a6ed00a4df44cf5bf0708d310584f04fd7",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 30,
                      "id": "Q30"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P518"
            ],
            "id": "Q21296543$1f1e1f85-439f-b602-fc61-270254aeeb80",
            "rank": "normal",
            "references": [
              {
                "hash": "aa30c81e2bfe02a26e29412c92986f0fbecac096",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "6a164248fc96bfa583bbb495cb63ae6401ec203c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 206855,
                          "id": "Q206855"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "42b07360a950a06b6fee81022138f6760aaaedf3",
                      "datavalue": {
                        "value": "https://ru.wikipedia.org/?oldid=104746961",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ],
        "P2437": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2437",
              "hash": "8730a8bb245cd3b6017c1a9827e78ac5df2e8fa4",
              "datavalue": {
                "value": {
                  "amount": "+3",
                  "unit": "1"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "fe1cbbbeb09a594537a61cd6a3ccea2098257aa8",
                  "datavalue": {
                    "value": {
                      "time": "+2019-02-27T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P585"
            ],
            "id": "Q21296543$1a38f62d-462a-2378-94e8-edfb184b560a",
            "rank": "normal",
            "references": [
              {
                "hash": "e949f9a5c39b6ccca61d78a290d8998119dfb0dc",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "68a51f8e9ab171e58250ac9b8b1a321138fbbe54",
                      "datavalue": {
                        "value": "https://intl.startrek.com/news/discovery-renewed-season-three",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              },
              {
                "hash": "d8af3cefbfa5736a91dd5851413dc8d53d5805f7",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "e597cff8d7dc880698c8bfac0434bbb10abc5c9c",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "ea405083ee908607512740d912c5fed83ee87b68",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P1113": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1113",
              "hash": "23c5e3c91f20eb64e40dbc527e946a04a58af702",
              "datavalue": {
                "value": {
                  "amount": "+34",
                  "unit": "1"
                },
                "type": "quantity"
              },
              "datatype": "quantity"
            },
            "type": "statement",
            "id": "Q21296543$83AF3D9A-E1C8-40A4-A0F1-29506130F49B",
            "rank": "normal",
            "references": [
              {
                "hash": "d5847b9b6032aa8b13dae3c2dfd9ed5d114d21b3",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "5a343e7e758a4282a01316d3e959b6e653b767fc",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 11920,
                          "id": "Q11920"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              },
              {
                "hash": "d8af3cefbfa5736a91dd5851413dc8d53d5805f7",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "e597cff8d7dc880698c8bfac0434bbb10abc5c9c",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "ea405083ee908607512740d912c5fed83ee87b68",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P1258": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1258",
              "hash": "029daa4741cddef6cf528eb5c617d5258862807b",
              "datavalue": {
                "value": "tv/star_trek_discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$2df77c29-4d91-57d1-8394-c4ba3a985734",
            "rank": "normal"
          }
        ],
        "P1712": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1712",
              "hash": "2cea8d875939c43ed05e0d7f645cab7a26f618ad",
              "datavalue": {
                "value": "tv/star-trek-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$fe1f8e2b-4c46-2ab4-196e-4e340fc0f2b3",
            "rank": "normal"
          }
        ],
        "P373": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P373",
              "hash": "5e320597b8d0d36ed672e488d0c0fc8539e83491",
              "datavalue": {
                "value": "Star Trek: Discovery",
                "type": "string"
              },
              "datatype": "string"
            },
            "type": "statement",
            "id": "Q21296543$686b620e-45cb-9734-c59b-41c69bb7cdb2",
            "rank": "normal"
          }
        ],
        "P840": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P840",
              "hash": "dda27b084a3c6b2362bc8e6268d2f3541591748a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 18043309,
                  "id": "Q18043309"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "f6c76ea4d2d3ae1049bb0ce93a71f2057fc9d1be",
                  "datavalue": {
                    "value": {
                      "time": "+2256-05-01T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 10,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P580"
            ],
            "id": "Q21296543$37d18c22-4c8e-7298-1aad-3bc25b885839",
            "rank": "normal"
          }
        ],
        "P910": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P910",
              "hash": "c6cb90514b328a7be202967f9960e7642edd8931",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 41095962,
                  "id": "Q41095962"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8d9709a3-491d-785b-a78d-5579080279be",
            "rank": "normal"
          }
        ],
        "P2638": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2638",
              "hash": "cc92607058ad4a53bb0f948e6336d8975cdb877a",
              "datavalue": {
                "value": "shows/star-trek-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$c4d9e008-4818-1400-e4d4-60badefee258",
            "rank": "normal"
          }
        ],
        "P915": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P915",
              "hash": "4cfbc32265a7766b63edd415fb9aa8598bae73b9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2095595,
                  "id": "Q2095595"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$379ad8f5-443d-adfa-e663-de46febc0bce",
            "rank": "normal",
            "references": [
              {
                "hash": "f88f2d295229139335dedfd943ba64414021fb72",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "440b4bfa342383f7509f7328fe0f4e1372bad797",
                      "datavalue": {
                        "value": "http://www.imdb.com/title/tt5171438/locations?ref_=tt_dt_dt",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P345": [
                    {
                      "snaktype": "value",
                      "property": "P345",
                      "hash": "c0adb43560567777836f60d53b04dea627f253cc",
                      "datavalue": {
                        "value": "tt5171438",
                        "type": "string"
                      },
                      "datatype": "external-id"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P248",
                  "P345"
                ]
              }
            ]
          }
        ],
        "P361": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P361",
              "hash": "6a54cba8394e8155c5911e03a42458aefd51d7f6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3500963,
                  "id": "Q3500963"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$63b5d554-456a-39ad-2ee4-3b3407bea46f",
            "rank": "normal"
          }
        ],
        "P1813": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1813",
              "hash": "f5d3944402a1f93146d505ea6fe0555ac6c9b275",
              "datavalue": {
                "value": {
                  "text": "DIS",
                  "language": "en"
                },
                "type": "monolingualtext"
              },
              "datatype": "monolingualtext"
            },
            "type": "statement",
            "id": "Q21296543$8db05ae8-42ca-f429-5a97-c4a8c57f0a77",
            "rank": "preferred",
            "references": [
              {
                "hash": "e68317621da3b081f06cdedfd40524c295c9f240",
                "snaks": {
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "925f07b38f726051a728ff692613202f1fb6a231",
                      "datavalue": {
                        "value": "https://en.wikipedia.org/wiki/Template:Star_Trek_abbreviations",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P4656"
                ]
              },
              {
                "hash": "c3bb52630f5c0fc02572c58a3547a7f45da087c8",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "af3c8108d2206ee0c5ef162db3576c7f2e469ebb",
                      "datavalue": {
                        "value": "http://www.ex-astris-scientia.org/database/glossary.htm",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              },
              {
                "hash": "78b69ce07d1d0027923ea0fd5882c7e36eda1a0e",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "19ddbe7e7933d2fee3a48176ae049453ef5f9fce",
                      "datavalue": {
                        "value": {
                          "text": "Abbreviation for Star Trek Series",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "ec79c13d26d71c32be34c844c09308b239839a1c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 67507716,
                          "id": "Q67507716"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P304": [
                    {
                      "snaktype": "value",
                      "property": "P304",
                      "hash": "1ff9f0ddf9c36972baceef1ee815675d6c5791d0",
                      "datavalue": {
                        "value": "13–16",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P248",
                  "P304"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1813",
              "hash": "f8a1ba4459522a35248cb877427673bdd96f1857",
              "datavalue": {
                "value": {
                  "text": "DSC",
                  "language": "en"
                },
                "type": "monolingualtext"
              },
              "datatype": "monolingualtext"
            },
            "type": "statement",
            "id": "Q21296543$c8accadd-4da7-ba53-f753-cdd379b21de3",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1813",
              "hash": "4f17c81f33d1afbe80f22de2835d7b79b2dfea4c",
              "datavalue": {
                "value": {
                  "text": "STD",
                  "language": "en"
                },
                "type": "monolingualtext"
              },
              "datatype": "monolingualtext"
            },
            "type": "statement",
            "id": "Q21296543$2f8e6625-40b9-4de8-87c3-00121a289214",
            "rank": "normal"
          }
        ],
        "P1874": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1874",
              "hash": "ae711842fe8aaa8f601a0441dc4954cd064f6c4f",
              "datavalue": {
                "value": "80126024",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$6909d508-43d5-5cc6-2261-74742c7bc6d4",
            "rank": "normal"
          }
        ],
        "P4665": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4665",
              "hash": "71b94caba1b5fcfab2df707ee80949499991e65b",
              "datavalue": {
                "value": "1110945",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$77D78E24-4BE0-4767-836D-E71DF0F53112",
            "rank": "normal",
            "references": [
              {
                "hash": "6945c7f21a216fec240306b3def25f537698a5fa",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "b444eb02e3c9e850b533255b67b5f60c2293b496",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 199864,
                          "id": "Q199864"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P138": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P138",
              "hash": "00941632b0e2961e452874cb0a114ca66a114630",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 47462450,
                  "id": "Q47462450"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$326c166c-4bb0-f201-842b-6ea135be6cbb",
            "rank": "normal"
          }
        ],
        "P1267": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1267",
              "hash": "561f7f44a3b8fb832f448c6a4db9dd0fc4caa526",
              "datavalue": {
                "value": "19949",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$b1664795-4060-8509-f951-8a25e428f410",
            "rank": "normal"
          }
        ],
        "P3984": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3984",
              "hash": "9da1e591a673e76ca40f347f3e022e4e9944e817",
              "datavalue": {
                "value": "StarTrekDiscovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "c3cb2f68d05e871096ee50c7efbdc503b7c1f81d",
                  "datavalue": {
                    "value": {
                      "time": "+2016-07-23T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "359cda9bd50878238b414657edfda931fe20e391",
                  "datavalue": {
                    "value": "Star Trek: Discovery",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P407",
              "P580",
              "P1810"
            ],
            "id": "Q21296543$36c70c75-429d-b7c5-2287-093b882bcd38",
            "rank": "normal",
            "references": [
              {
                "hash": "848c7514b88b1f487526b9556ccde288c97daabd",
                "snaks": {
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "be0f82c1f563fe0acd805d40974b9ab3e372c220",
                      "datavalue": {
                        "value": {
                          "time": "+2018-05-06T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P813"
                ]
              }
            ]
          }
        ],
        "P527": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "f3cc66098cab601ec9a30632cc8ba882fa6d95d6",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 41477806,
                  "id": "Q41477806"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1545": [
                {
                  "snaktype": "value",
                  "property": "P1545",
                  "hash": "2a1ced1dca90648ea7e306acbadd74fc81a10722",
                  "datavalue": {
                    "value": "1",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1545"
            ],
            "id": "Q21296543$54469276-712F-4566-A2ED-59060950846F",
            "rank": "normal",
            "references": [
              {
                "hash": "d8af3cefbfa5736a91dd5851413dc8d53d5805f7",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "e597cff8d7dc880698c8bfac0434bbb10abc5c9c",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "ea405083ee908607512740d912c5fed83ee87b68",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "09ddd8869ae66a17c3cdb6b38a4a941642651459",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 51902986,
                  "id": "Q51902986"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1545": [
                {
                  "snaktype": "value",
                  "property": "P1545",
                  "hash": "7241753c62a310cf84895620ea82250dcea65835",
                  "datavalue": {
                    "value": "2",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1545"
            ],
            "id": "Q21296543$0a6c47e6-4c2d-b03b-d2cb-06238c30c49e",
            "rank": "normal",
            "references": [
              {
                "hash": "d8af3cefbfa5736a91dd5851413dc8d53d5805f7",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "e597cff8d7dc880698c8bfac0434bbb10abc5c9c",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "ea405083ee908607512740d912c5fed83ee87b68",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P527",
              "hash": "7b5729361c0cc2d11eb658070a2febfb22bc19a0",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 63113909,
                  "id": "Q63113909"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1545": [
                {
                  "snaktype": "value",
                  "property": "P1545",
                  "hash": "0e979f28bf306fefdcd352b4eb8dee5da2153a6d",
                  "datavalue": {
                    "value": "3",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1545"
            ],
            "id": "Q21296543$d2456ed3-4839-6611-fc0e-74fbb56fa15c",
            "rank": "normal",
            "references": [
              {
                "hash": "e949f9a5c39b6ccca61d78a290d8998119dfb0dc",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "68a51f8e9ab171e58250ac9b8b1a321138fbbe54",
                      "datavalue": {
                        "value": "https://intl.startrek.com/news/discovery-renewed-season-three",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              },
              {
                "hash": "d8af3cefbfa5736a91dd5851413dc8d53d5805f7",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "e597cff8d7dc880698c8bfac0434bbb10abc5c9c",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "ea405083ee908607512740d912c5fed83ee87b68",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "8513db67d8bb3e2a38df7bbdb73fd52fa9ed63b5",
                      "datavalue": {
                        "value": {
                          "time": "+2019-12-02T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P3141": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3141",
              "hash": "cb42c5b4ada3251d7270d5362d9305486d99d70f",
              "datavalue": {
                "value": "t0014725",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$827fc768-4b61-cc18-4461-81d10012691d",
            "rank": "normal"
          }
        ],
        "P4834": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4834",
              "hash": "363b0914b8f35a20471e318e91a120e5518de67a",
              "datavalue": {
                "value": "38496",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$074C91B0-0CB5-4BD3-AACC-73CFE48AE13D",
            "rank": "normal"
          }
        ],
        "P57": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "470085d2e1c0d703baafb80f430cd3bf1604dcf2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3018772,
                  "id": "Q3018772"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$31be3607-474a-8fd1-da23-d941e96d0932",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "91ec619201986db6b615cd2991e3d7ab34d522f8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 4679312,
                  "id": "Q4679312"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$87d4af37-46b8-b528-c2f7-e85c85930d96",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "107a06b1d9b352e87228bf6a4258bf86087a5c8c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 419454,
                  "id": "Q419454"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$aa769b0b-40ca-f83d-9997-9582521b43d5",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "b8f83c62c1d706226217070a2d5d296c4bcee737",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 17090902,
                  "id": "Q17090902"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$c9a6ae0f-4d6b-b199-7ee3-4655ce2c7a1e",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "7f832c38d4f63271dc62fb653cadbede24296b18",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 6514839,
                  "id": "Q6514839"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$fb4d2687-4d3e-3d5d-820e-1bd706afd886",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "5168a072ac167f082205aea94c3dba5a7b064956",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 11856301,
                  "id": "Q11856301"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$554c085f-4da5-de3d-ed98-661d43b9a003",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "da7794e009391593c074ff0b594845435ecf0b64",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 5231164,
                  "id": "Q5231164"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$84ab679d-4ff9-4b20-5fa7-2e6d34295f46",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "1c614c91524f34d62f1043e6bc76dcda633233c8",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2129942,
                  "id": "Q2129942"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$77c4f0d4-4ba6-9f4b-de97-29ea9e12e194",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "989eb03ec6fefe74d7119ad5152a41d066314938",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 346595,
                  "id": "Q346595"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$d02e8edb-41f5-97ef-3bcf-fda03c93d840",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "3275944b32b037756ced8982840a650867863b09",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 20987428,
                  "id": "Q20987428"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$c76ad55a-477d-1141-f225-d88f9aa2e412",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "b9d037a5f6e5c1e2092cb0921e11a59a16815dde",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 18705002,
                  "id": "Q18705002"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$e5b21de9-46d3-a189-a1d4-4ff57dde9f0f",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "419d2b0c8d339939e5197b42c41dfd12e113423e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3018806,
                  "id": "Q3018806"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$207ca346-41b3-882f-1959-e2d8b0181255",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "9c807fc1dbae727f770c0727c6ef24f8523067ac",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 63114170,
                  "id": "Q63114170"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$91731351-4807-518f-1ef5-f5c98b49d76c",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "58169f1065d3a320d10f8c638f3de123f05faf77",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 16745401,
                  "id": "Q16745401"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$0bdad3fe-49ca-deb5-b4b3-92055cb76f70",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "9a4af77a934dde71b95b22741c989592464f9d62",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 432598,
                  "id": "Q432598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$ba42afb6-426f-be71-e809-638f06499508",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P57",
              "hash": "74ca08ed6bccaed46382654ecfb42e556cf2edde",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 29341423,
                  "id": "Q29341423"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$568db531-44ee-5dab-c718-1f1266a1492c",
            "rank": "normal",
            "references": [
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P480": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P480",
              "hash": "d36b9302c955144aca5dcdff03e8d5998e045413",
              "datavalue": {
                "value": "549756",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$b29e1387-4931-b977-7585-252f5fe02a7e",
            "rank": "normal"
          }
        ],
        "P1881": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1881",
              "hash": "f168047ae30da90df298d4814a3c8980b0583051",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 41641814,
                  "id": "Q41641814"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$D7F0E95E-3317-4660-9F5D-3FE11388ED56",
            "rank": "normal"
          }
        ],
        "P5099": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P5099",
              "hash": "de87a886eb482c75187bef0b64f203ffd7441670",
              "datavalue": {
                "value": "telefilm/startrekdiscovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$9150A43D-4BC8-4490-8187-1C812499A3A1",
            "rank": "normal",
            "references": [
              {
                "hash": "d5847b9b6032aa8b13dae3c2dfd9ed5d114d21b3",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "5a343e7e758a4282a01316d3e959b6e653b767fc",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 11920,
                          "id": "Q11920"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P4983": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4983",
              "hash": "2a4d50e37b042a990b370d4cf9a8d8d8d1159760",
              "datavalue": {
                "value": "67198",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$00BF216C-7AA8-47F4-AA4F-8D9A741C9708",
            "rank": "normal"
          }
        ],
        "P1562": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1562",
              "hash": "10b8de1964e87324ca29afadc8ceabcb747cf8ec",
              "datavalue": {
                "value": "v694473",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$b5059e95-4ea5-c26a-914b-ec644c389428",
            "rank": "normal"
          }
        ],
        "P5032": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P5032",
              "hash": "0210613626c778925c0afa6ca850a0dbb469d4ee",
              "datavalue": {
                "value": "757950",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$d2a00f42-4771-b819-2e07-69e820a10715",
            "rank": "normal"
          }
        ],
        "P3138": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3138",
              "hash": "189a522d88b91f60877fa2846b26fd8f01ef2c76",
              "datavalue": {
                "value": "303312",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$85c3bc92-4ad7-343b-4ee9-b3624138d815",
            "rank": "normal"
          }
        ],
        "P905": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P905",
              "hash": "8ac3c9fc714c7c1b4ca97e2892d9767f16a22f35",
              "datavalue": {
                "value": "190089",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$29fbf6bb-4028-b800-3a3e-515247065a47",
            "rank": "normal"
          }
        ],
        "P3804": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3804",
              "hash": "10a89eedc822b2895b9cb9c308c8fb25ff054809",
              "datavalue": {
                "value": "874935",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$6766ea18-4c36-b678-ff4f-9dcb57ad8667",
            "rank": "normal"
          }
        ],
        "P4835": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4835",
              "hash": "0462d018acf6eb79c1e6652c0ddf6dc41d989934",
              "datavalue": {
                "value": "328711",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$9be48a00-4dea-2fa6-644c-54f8ef003d04",
            "rank": "normal"
          }
        ],
        "P2704": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2704",
              "hash": "32cc23fabdca973755e8d328a7d84c232ac943ab",
              "datavalue": {
                "value": "10.5240/FFB4-22E6-C037-BDB0-AC9D-8",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$ac1adeb8-49c8-a506-8818-781def055e54",
            "rank": "normal"
          }
        ],
        "P162": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P162",
              "hash": "97da483c5331198372e1ad90d0ce971f12c683a7",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 432598,
                  "id": "Q432598"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$66DF5F80-CF12-4839-8EFF-B1686F1A07E6",
            "rank": "normal",
            "references": [
              {
                "hash": "65c7f84d051239f91cc90095b052e2d00070f2f0",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "05a2176a04251188610f9f78888e1e7dc6ae762d",
                      "datavalue": {
                        "value": "https://de.wikipedia.org/w/index.php?title=Star_Trek:_Discovery&oldid=193581532",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              },
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P344": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P344",
              "hash": "ff3a9e48cb7f447d8fcf6844f4c559ecc0c60d81",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1314113,
                  "id": "Q1314113"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8D4686DE-0A66-403D-AE80-53631B956AFB",
            "rank": "normal",
            "references": [
              {
                "hash": "65c7f84d051239f91cc90095b052e2d00070f2f0",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "05a2176a04251188610f9f78888e1e7dc6ae762d",
                      "datavalue": {
                        "value": "https://de.wikipedia.org/w/index.php?title=Star_Trek:_Discovery&oldid=193581532",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              },
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P344",
              "hash": "9100dd17af99fc8192fdc949d1402f88cfeada25",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 75031199,
                  "id": "Q75031199"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$4450c4af-4031-5c83-c350-b6485654b64b",
            "rank": "normal",
            "references": [
              {
                "hash": "9a9b2415c6db4f53a2ce050f6e9d0b98d3d069ce",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "cc135801f09114c284b392066216488f154108b2",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-14T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P5327": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P5327",
              "hash": "602620e236737c0bb0c01cfe2f3eeb13684533ce",
              "datavalue": {
                "value": "star-trek-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$1EC66B3B-8807-4275-9F28-CAA4CEE8E893",
            "rank": "normal",
            "references": [
              {
                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P1434": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1434",
              "hash": "542ba764f9ac83dfb6169078dbf1b6aec3337841",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 18043309,
                  "id": "Q18043309"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$918D1CF1-2F1A-49B5-B3E7-BE6EBB199449",
            "rank": "normal"
          }
        ],
        "P1811": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1811",
              "hash": "8e08b2895640cb2639d0aae30b62fdd96eb6a3f0",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 41525256,
                  "id": "Q41525256"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$353a1ea5-4652-ddbc-5a0d-3796f2ba2c3b",
            "rank": "normal"
          }
        ],
        "P144": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P144",
              "hash": "d317ad849c3a0b16504b994e0c2e56d9a5e03386",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1077,
                  "id": "Q1077"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$57e84acf-4fd6-efd0-9ccb-34c7d72d2230",
            "rank": "normal"
          }
        ],
        "P674": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "9cac7e38335b76ea21597be2cd1c8255194437b3",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 40935468,
                  "id": "Q40935468"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P5800": [
                {
                  "snaktype": "value",
                  "property": "P5800",
                  "hash": "afed9751e23af2354b04716a9670fe0529577675",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 215972,
                      "id": "Q215972"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P5800"
            ],
            "id": "Q21296543$e0a35f44-48a0-31fe-8ad2-343368a6ed6b",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "d8d2bf551c1ebfb817fd8bab755c36aa13b11023",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 42713428,
                  "id": "Q42713428"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$9f1e3cb0-40af-d45e-b701-b8e5ffbf3130",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "1a33b6418d72ce550cd50d06cd3c8299784b7a8e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 41796329,
                  "id": "Q41796329"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$b6987517-49e1-9b8c-4e50-6177dad68945",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "0136ce7b633bfa650456fac796e80b4b9e57a91b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 42716550,
                  "id": "Q42716550"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$7274d2b9-45c9-1125-b5a6-ed6bd10c9b3c",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "4f99df5aa76e85d2540e25b3ff66b7b9d9b2e09e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 61655496,
                  "id": "Q61655496"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$151ea553-4b71-3894-205b-607536bffc5d",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "346b20cf0bb4ec0ffbdb9eb9f5e7a5cbaf69078a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 48080009,
                  "id": "Q48080009"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$7294E566-FBBE-46E9-918E-076E67F528AC",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "1b202adb4ba90b5c6835f0626ea0a95153a26a01",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 48032489,
                  "id": "Q48032489"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$1AF35097-4545-4534-8DC4-8F8D747F75E7",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "a8131d3ebed1f8a1de0c8e7e41cece9dfd7e391a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 43740811,
                  "id": "Q43740811"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$8D4C5A01-E4E8-49F5-96A2-39B9780876B4",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "7a78853b03319a17b3f662b599d8560bfaa9570b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 47391140,
                  "id": "Q47391140"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$AA58D179-6A03-4DBD-A17D-B3D2E8D2FAFE",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "97f7f2d4f00e63214df943ab8d29c4bf3e50191f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 44569965,
                  "id": "Q44569965"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$754EBD91-3497-42BA-AFF1-689C593AE1D0",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "8b4840a1c84ae2006d0bdb1039394f3b5a811439",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2712069,
                  "id": "Q2712069"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$FEAF65E1-54AD-43BD-9B84-885D7D7DBA4E",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "1d68927c6606f5483d37bd04fdccdbaa226cedeb",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1412447,
                  "id": "Q1412447"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$EAFD669F-B591-4C31-A4A6-78CE6413E305",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "cdc8cbca4dc169c873ddbdb7cc0ef5c50a21723b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 3127322,
                  "id": "Q3127322"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$05EBEB2E-3637-4E9B-A939-FDF1467C36D6",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "68e343710fe54bd99d43a0dbbe1caa5e668b3d3f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 48081407,
                  "id": "Q48081407"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$D65E3E45-A12D-46A5-BEF8-A3262F317B94",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "892da95507875fbc82221a025fa7ec69fb7d7a71",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 43217835,
                  "id": "Q43217835"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$CB4B1FA4-1718-4EDE-9055-15D979EFBF91",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "9d8cf4498cf611db7995f07396412c8eb48b69ff",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 48078634,
                  "id": "Q48078634"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$EB274637-7F56-464D-BFB8-4F0C3D4969DA",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "041637400ce7187c39a943ee5edd8565223e560e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 612625,
                  "id": "Q612625"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$B8F5A4DE-52F8-4139-9D0C-FD012699EFC1",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "8b6096fa6e5f82a1db853ff362e91e1bd0a0fb58",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 16341,
                  "id": "Q16341"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$4e2db31a-48af-efa0-880d-8a6ef6fc9c53",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "029a65a61f5895dcab7ff409ced0845035b23733",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1568510,
                  "id": "Q1568510"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$4b8f01d1-418b-ccd2-490e-3f0d3cf0909c",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P674",
              "hash": "39c4083a37e8c26627be4da4ccf3ff290fb4a4d1",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 56926823,
                  "id": "Q56926823"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$583f5054-4603-d9db-003e-c0f0a86ad9a9",
            "rank": "normal"
          }
        ],
        "P2512": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2512",
              "hash": "168e6c8c843874bce89859792d6d808116dd7d0b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 56816581,
                  "id": "Q56816581"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$f75097e4-4939-a2f4-e13e-9fd81553f0d8",
            "rank": "normal"
          }
        ],
        "P5925": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P5925",
              "hash": "c6adf3d101430da864d5c1e18e17bab4a42e063d",
              "datavalue": {
                "value": "star-trek-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$DC7E51CD-53D1-4F6A-8406-AC5712B7E493",
            "rank": "normal"
          }
        ],
        "P407": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P407",
              "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1860,
                  "id": "Q1860"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$7EBEBE91-2106-4E14-917E-A38D45DAEEBE",
            "rank": "normal"
          }
        ],
        "P2671": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2671",
              "hash": "8a14a99e7dd3cedefd7d4dddc2d38a1b747d0411",
              "datavalue": {
                "value": "/g/11bwn53rt3",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$914475c6-4572-c147-3724-b1233b53201c",
            "rank": "normal"
          }
        ],
        "P214": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P214",
              "hash": "7c0517359564ee22a23b6dbf2a2adfb68bff1918",
              "datavalue": {
                "value": "3111152684012423430003",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$fe6a4551-4507-b682-1d0c-10b3e3d3866b",
            "rank": "normal"
          }
        ],
        "P244": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P244",
              "hash": "f44e84cf3d25c0505ad7cfc054f1dfac89278aa8",
              "datavalue": {
                "value": "no2018151189",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$4778b70f-4224-5fd4-f3a4-32a9999e5583",
            "rank": "normal",
            "references": [
              {
                "hash": "63309730314f4c20bf6b1008fe8ffd2b155272b3",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6b7d4330c4aac4caec4ede9de0311ce273f88ecd",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 54919,
                          "id": "Q54919"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P1695": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1695",
              "hash": "e17278e66ac6c931b571e3f9f99c49f2825cedae",
              "datavalue": {
                "value": "A37586506",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$aa973529-46b5-25ac-10a1-506ce78452f5",
            "rank": "normal",
            "references": [
              {
                "hash": "63309730314f4c20bf6b1008fe8ffd2b155272b3",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6b7d4330c4aac4caec4ede9de0311ce273f88ecd",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 54919,
                          "id": "Q54919"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P6643": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6643",
              "hash": "baa0a9c206a98d13167c08ea055faf6aa3fff99c",
              "datavalue": {
                "value": "star-trek-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$9F84698D-6B44-4973-A6F5-6562727898E4",
            "rank": "normal"
          }
        ],
        "P86": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P86",
              "hash": "21c20450424a5d087507208bb8f21ba9001dc9ab",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 6174877,
                  "id": "Q6174877"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$982E1DAA-124E-49ED-A968-ECFBD7EE9379",
            "rank": "normal",
            "references": [
              {
                "hash": "209488ded05bd581de828997aad98aa98eb0cfbf",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "39434703e77c8b91795a9b39b5f1b9a01a30b1c7",
                      "datavalue": {
                        "value": "https://de.wikipedia.org/w/index.php?title=Star_Trek:_Discovery&oldid=188740099",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              },
              {
                "hash": "6b7dd33be98a59d9386139e9e4797ff58f3763a1",
                "snaks": {
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "260f531377dd7e949694675c71e029d286e918cd",
                      "datavalue": {
                        "value": {
                          "text": "Star Trek: Discovery – Full Cast & Crew",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "8f9592058ab56fbd806d515a9380667cdc82a3c9",
                      "datavalue": {
                        "value": "https://www.imdb.com/title/tt5171438/fullcredits",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "6ff43c6ce02fc9e2012771b5595093e7f0c33162",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 37312,
                          "id": "Q37312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1efcd41b94db8c55e11e389cf7027914eaf79ded",
                      "datavalue": {
                        "value": {
                          "time": "+2019-10-12T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P1476",
                  "P854",
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P7107": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7107",
              "hash": "8035ccdffc3d4d1413149b820b89070faa0be1a4",
              "datavalue": {
                "value": "star-trek-discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$2D5D8EE0-B370-4623-89D3-E7EF161847FF",
            "rank": "normal"
          }
        ],
        "P7285": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7285",
              "hash": "0525f842fda06f188a9b15f01a9253ad9bd86f26",
              "datavalue": {
                "value": "1134306",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$b0ef2bb5-48d6-66c1-b983-e79344e57f91",
            "rank": "normal"
          }
        ],
        "P7299": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7299",
              "hash": "6c4c12651c72ca5b1202b9b386ddb692212eaf00",
              "datavalue": {
                "value": "200605",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$6C32BB11-A33F-4E04-82FB-FCD1E3EA8EC9",
            "rank": "normal"
          }
        ],
        "P3302": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3302",
              "hash": "a1fb7b5cfa17c533b51972826ec1c4a9fef31911",
              "datavalue": {
                "value": "123523",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$03f4be72-44cd-35b5-e2fc-1c224d5072f7",
            "rank": "normal"
          }
        ],
        "P3135": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3135",
              "hash": "56283605246777e1486e958beca815ff1f101882",
              "datavalue": {
                "value": "2048946",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$29d024c1-48ec-d94a-2f4f-2d2c4ba059c7",
            "rank": "normal"
          }
        ],
        "P6262": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6262",
              "hash": "3c16e50a2f946daf6cae43502741fa09aee26573",
              "datavalue": {
                "value": "memory-beta:Star_Trek:_Discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "359cda9bd50878238b414657edfda931fe20e391",
                  "datavalue": {
                    "value": "Star Trek: Discovery",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P407",
              "P1810"
            ],
            "id": "Q21296543$C6B859D8-EDA0-476C-9842-4DD692048C3C",
            "rank": "normal",
            "references": [
              {
                "hash": "b26c1dcb7ea32f95fcbf692c923387124c7a5af1",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "765b1ad234bd84ad2fb433976e78ca3e47a8e692",
                      "datavalue": {
                        "value": "https://memory-beta.fandom.com/wiki/Star_Trek:_Discovery?oldid=661420",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "6612924e0d0305c72bd45c8f41978130983940e3",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-04T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "359cda9bd50878238b414657edfda931fe20e391",
                      "datavalue": {
                        "value": "Star Trek: Discovery",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6262",
              "hash": "06337fd80ffd5c5b66948d3b35846052acf59be1",
              "datavalue": {
                "value": "memory-alpha:Star_Trek:_Discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "359cda9bd50878238b414657edfda931fe20e391",
                  "datavalue": {
                    "value": "Star Trek: Discovery",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P407",
              "P1810"
            ],
            "id": "Q21296543$224e51fb-493c-045e-2b04-ccb03831e47c",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6262",
              "hash": "e4011961599c2c6b3b9c0bccaf9f381cad53a2e3",
              "datavalue": {
                "value": "de.memory-alpha:Star_Trek:_Discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "46bfd327b830f66f7061ea92d1be430c135fa91f",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 188,
                      "id": "Q188"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1810": [
                {
                  "snaktype": "value",
                  "property": "P1810",
                  "hash": "359cda9bd50878238b414657edfda931fe20e391",
                  "datavalue": {
                    "value": "Star Trek: Discovery",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P407",
              "P1810"
            ],
            "id": "Q21296543$C67C91AC-7725-47AA-A109-0C4C4860FED1",
            "rank": "normal",
            "references": [
              {
                "hash": "ce5e744a0c57e4902dcca83d097b23dd4a4b9e82",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "db5fb6bdb9a83032afdd1dcd51e84202f3c3e0f1",
                      "datavalue": {
                        "value": "https://memory-alpha.fandom.com/de/wiki/Star_Trek:_Discovery?oldid=719916",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "1c5acb2b410595b83525d62e9c996f5b02aa7ebf",
                      "datavalue": {
                        "value": {
                          "time": "+2019-11-06T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P1810": [
                    {
                      "snaktype": "value",
                      "property": "P1810",
                      "hash": "359cda9bd50878238b414657edfda931fe20e391",
                      "datavalue": {
                        "value": "Star Trek: Discovery",
                        "type": "string"
                      },
                      "datatype": "string"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813",
                  "P1810"
                ]
              }
            ]
          }
        ],
        "P4780": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4780",
              "hash": "7c673489768f8de07f5702a9ea78ee37cc8c5546",
              "datavalue": {
                "value": "93489",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$631D2017-3A5A-48A6-8032-AF9EA3C63C37",
            "rank": "normal"
          }
        ],
        "P4784": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4784",
              "hash": "d93f2a05430babded5bcb952d2b7517497e2cb12",
              "datavalue": {
                "value": "4722",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$FC5F20A6-2330-4F34-98CD-9C45801E1F03",
            "rank": "normal"
          }
        ],
        "P7091": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7091",
              "hash": "6b2fc438a9ea7c7a85ce27d02e20b2f6722ef258",
              "datavalue": {
                "value": "5774271",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$5EAFE9C8-E1DA-4083-BAC3-D0AFCD2281CC",
            "rank": "normal"
          }
        ],
        "P7293": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7293",
              "hash": "691306443dd5046121677637c8a1edc72e5637c5",
              "datavalue": {
                "value": "9810616691905606",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$a089ea35-476a-d036-2b50-94ec62af6dba",
            "rank": "normal"
          }
        ],
        "P950": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P950",
              "hash": "6dbe9cefd9664efc9d16762ff7f8039b2a9821b1",
              "datavalue": {
                "value": "XX5840745",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$453DB513-2DC1-4E76-A213-E6B538791415",
            "rank": "normal"
          }
        ],
        "P6949": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6949",
              "hash": "aed48a3f5f207b97762f0053a275201d62543369",
              "datavalue": {
                "value": {
                  "time": "+2015-11-02T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 11,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q21296543$ae833fe1-4149-41c0-1ba5-5c3dc1bb6b56",
            "rank": "normal"
          }
        ],
        "P166": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P166",
              "hash": "8705663c22887a52368c1d3fedeb11e51ce92ada",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 24616,
                  "id": "Q24616"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "6174553681261aeec411766adf691fdeec1dee47",
                  "datavalue": {
                    "value": {
                      "time": "+2018-00-00T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 9,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "b492e2ca59fae46f1574c977c0849a2c8dda83df",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 48043593,
                      "id": "Q48043593"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1346": [
                {
                  "snaktype": "value",
                  "property": "P1346",
                  "hash": "96c7bc0d30e0a7ae03687a73bc5ca705e6ed2703",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 214223,
                      "id": "Q214223"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P585",
              "P805",
              "P1346"
            ],
            "id": "Q21296543$bd7533c1-494e-b7d1-3ad9-aef525c8b7b6",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P166",
              "hash": "c0c7dcb51faf5b99c9bd8a20532b38464bbff152",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1263057,
                  "id": "Q1263057"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "6174553681261aeec411766adf691fdeec1dee47",
                  "datavalue": {
                    "value": {
                      "time": "+2018-00-00T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 9,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "71c6d17df74ac796871d8eff3627036e8ebab211",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 50626247,
                      "id": "Q50626247"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1346": [
                {
                  "snaktype": "value",
                  "property": "P1346",
                  "hash": "9dd47a2f37a2c4ea52f9d019497d9013ba34650d",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 7560935,
                      "id": "Q7560935"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P585",
              "P805",
              "P1346"
            ],
            "id": "Q21296543$5171fae1-485e-8c17-5361-afc22a4d6e50",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P166",
              "hash": "5cff29a9f1d0d6d98bbea7c98ae67c4fafccee1e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 23010098,
                  "id": "Q23010098"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "6174553681261aeec411766adf691fdeec1dee47",
                  "datavalue": {
                    "value": {
                      "time": "+2018-00-00T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 9,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "71c6d17df74ac796871d8eff3627036e8ebab211",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 50626247,
                      "id": "Q50626247"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P585",
              "P805"
            ],
            "id": "Q21296543$bca8a54f-4149-94c8-5d28-c04c56b10a51",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P166",
              "hash": "ffdb6c765571f893383c6760dc792ed2455e8b95",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 25025421,
                  "id": "Q25025421"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "77f348fcb49110a0de3c2faf4865527dc30dcbc9",
                  "datavalue": {
                    "value": {
                      "time": "+2019-00-00T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 9,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "05e9431a618d8394943a5ed5c17997466bef2442",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 67646363,
                      "id": "Q67646363"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P585",
              "P805"
            ],
            "id": "Q21296543$7d926dd4-4d60-7855-86ba-186d171d5391",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P166",
              "hash": "dcaff86b53236e9a4aa49b18283f01edd52f113c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 83947774,
                  "id": "Q83947774"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "77f348fcb49110a0de3c2faf4865527dc30dcbc9",
                  "datavalue": {
                    "value": {
                      "time": "+2019-00-00T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 9,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "b61a25593b083797a3c897496d5f158990bf64ff",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 65588477,
                      "id": "Q65588477"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P585",
              "P805"
            ],
            "id": "Q21296543$87c6d5b5-4702-c64c-c31a-83dbf35f3a18",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P166",
              "hash": "97a61bae8465f0f516b161ee047e2b1503cb8329",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 83947906,
                  "id": "Q83947906"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P585": [
                {
                  "snaktype": "value",
                  "property": "P585",
                  "hash": "77f348fcb49110a0de3c2faf4865527dc30dcbc9",
                  "datavalue": {
                    "value": {
                      "time": "+2019-00-00T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 9,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P805": [
                {
                  "snaktype": "value",
                  "property": "P805",
                  "hash": "b61a25593b083797a3c897496d5f158990bf64ff",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 65588477,
                      "id": "Q65588477"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ],
              "P1346": [
                {
                  "snaktype": "value",
                  "property": "P1346",
                  "hash": "9dd47a2f37a2c4ea52f9d019497d9013ba34650d",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 7560935,
                      "id": "Q7560935"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P585",
              "P805",
              "P1346"
            ],
            "id": "Q21296543$8c8cda53-437d-2af1-3b1e-1a201732b0d4",
            "rank": "normal"
          }
        ],
        "P156": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P156",
              "hash": "e81657d4b68118e7595d73d2648eb93dbe94e851",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 62573305,
                  "id": "Q62573305"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$4519e81e-491a-857e-15e3-4c5e75cdcec6",
            "rank": "normal",
            "references": [
              {
                "hash": "aa30c81e2bfe02a26e29412c92986f0fbecac096",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "6a164248fc96bfa583bbb495cb63ae6401ec203c",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 206855,
                          "id": "Q206855"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "42b07360a950a06b6fee81022138f6760aaaedf3",
                      "datavalue": {
                        "value": "https://ru.wikipedia.org/?oldid=104746961",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ],
        "P6381": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6381",
              "hash": "cf238855062599a1283c12d1e46e7be4af8076c1",
              "datavalue": {
                "value": "1483487348",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$FD58F047-F091-4352-91DE-AD67C06342A0",
            "rank": "normal"
          }
        ],
        "P3121": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3121",
              "hash": "78b1cab51b641cdb5139969677d8c927202bfe4e",
              "datavalue": {
                "value": "StarTrekDiscovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q21296543$DE456903-7122-4FF5-BAFD-8A943252A338",
            "rank": "normal"
          }
        ],
        "P8345": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P8345",
              "hash": "8fd9675dd0b3a71dd4b70a6b3b45b87cf345410d",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1092,
                  "id": "Q1092"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$a8408986-4b3f-b21d-6575-2df50f5b0897",
            "rank": "normal"
          }
        ],
        "P941": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P941",
              "hash": "c523cc4bcc4757bd0f5d06038f7e03f637572011",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 326228,
                  "id": "Q326228"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q21296543$924603f3-4325-b2f1-a6e8-5acac9cccd93",
            "rank": "normal"
          }
        ]
      },
      "sitelinks": {
        "arwiki": {
          "site": "arwiki",
          "title": "ستار تريك: ديسكفري(مسلسل تلفزيوني)",
          "badges": []
        },
        "bewiki": {
          "site": "bewiki",
          "title": "Зорны шлях: Дыскавэры",
          "badges": []
        },
        "bgwiki": {
          "site": "bgwiki",
          "title": "Стар Трек: Дискавъри",
          "badges": []
        },
        "bswiki": {
          "site": "bswiki",
          "title": "Zvjezdane staze: Discovery",
          "badges": []
        },
        "cawiki": {
          "site": "cawiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "cswiki": {
          "site": "cswiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "dawiki": {
          "site": "dawiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "enwikiquote": {
          "site": "enwikiquote",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "eowiki": {
          "site": "eowiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "fiwiki": {
          "site": "fiwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Star Trek : Discovery",
          "badges": []
        },
        "hewiki": {
          "site": "hewiki",
          "title": "מסע בין כוכבים: דיסקברי",
          "badges": []
        },
        "hrwiki": {
          "site": "hrwiki",
          "title": "Zvjezdane staze: Discovery",
          "badges": []
        },
        "huwiki": {
          "site": "huwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "itwiki": {
          "site": "itwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "itwikiquote": {
          "site": "itwikiquote",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "jawiki": {
          "site": "jawiki",
          "title": "スタートレック:ディスカバリー",
          "badges": []
        },
        "kkwiki": {
          "site": "kkwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "kowiki": {
          "site": "kowiki",
          "title": "스타 트렉: 디스커버리",
          "badges": []
        },
        "nlwiki": {
          "site": "nlwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "nowiki": {
          "site": "nowiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "plwiki": {
          "site": "plwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "rowiki": {
          "site": "rowiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Звёздный путь: Дискавери",
          "badges": []
        },
        "shwiki": {
          "site": "shwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "slwiki": {
          "site": "slwiki",
          "title": "Zvezdne steze: Discovery",
          "badges": []
        },
        "srwiki": {
          "site": "srwiki",
          "title": "Звездане стазе: Дискавери",
          "badges": []
        },
        "svwiki": {
          "site": "svwiki",
          "title": "Star Trek: Discovery",
          "badges": []
        },
        "thwiki": {
          "site": "thwiki",
          "title": "สตาร์ เทรค: ดิสคัฟเวอรี่",
          "badges": []
        },
        "trwiki": {
          "site": "trwiki",
          "title": "Uzay Yolu: Keşif",
          "badges": []
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Зоряний шлях: Дискавері",
          "badges": []
        },
        "zhwiki": {
          "site": "zhwiki",
          "title": "星際爭霸戰：發現號",
          "badges": []
        }
      }
    },
    "Q54384": {
      "pageid": 56962,
      "ns": 0,
      "title": "Q54384",
      "lastrevid": 1155196388,
      "modified": "2020-04-11T14:46:26Z",
      "type": "item",
      "id": "Q54384",
      "labels": {
        "en": {
          "language": "en",
          "value": "Discovery"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "space shuttle orbiter"
        }
      },
      "aliases": {
        "en": [
          {
            "language": "en",
            "value": "OV-103"
          },
          {
            "language": "en",
            "value": "Space Shuttle Discovery"
          },
          {
            "language": "en",
            "value": "OV103"
          },
          {
            "language": "en",
            "value": "Orbital Vehicle 103"
          },
          {
            "language": "en",
            "value": "Discovery Space Shuttle"
          }
        ]
      },
      "claims": {
        "P373": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P373",
              "hash": "414e3d26accf571046efeb441fff5717ccd9ced2",
              "datavalue": {
                "value": "Space Shuttle Discovery",
                "type": "string"
              },
              "datatype": "string"
            },
            "type": "statement",
            "id": "q54384$D14838C0-4F2F-4913-814C-65B0FC948E6C",
            "rank": "normal"
          }
        ],
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "4ab8726efd34582074a7d58f693059d2de7d62d3",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1064394,
                  "id": "Q1064394"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "q54384$6e631374-4cc5-bf05-bd87-c859c0e8ead2",
            "rank": "normal"
          }
        ],
        "P625": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P625",
              "hash": "42f81a1c1f7f72eb5ed749e8b92e2b210ef305d5",
              "datavalue": {
                "value": {
                  "latitude": 38.911372,
                  "longitude": -77.445224,
                  "altitude": null,
                  "precision": 1e-06,
                  "globe": "http://www.wikidata.org/entity/Q2"
                },
                "type": "globecoordinate"
              },
              "datatype": "globe-coordinate"
            },
            "type": "statement",
            "id": "q54384$729465c8-4661-7d42-fd21-4ba929809ea3",
            "rank": "normal"
          }
        ],
        "P793": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P793",
              "hash": "7db4a0c53c9b0b12e75b81e8a103dca625a24801",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1362364,
                  "id": "Q1362364"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P580": [
                {
                  "snaktype": "value",
                  "property": "P580",
                  "hash": "dd5bc0351e145aca1dac5deeae2e1a22b73d1a4e",
                  "datavalue": {
                    "value": {
                      "time": "+1984-08-30T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ],
              "P582": [
                {
                  "snaktype": "value",
                  "property": "P582",
                  "hash": "e267c9627240cb1a0bde60ca37a2757da1a6677d",
                  "datavalue": {
                    "value": {
                      "time": "+1984-09-05T00:00:00Z",
                      "timezone": 0,
                      "before": 0,
                      "after": 0,
                      "precision": 11,
                      "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                    },
                    "type": "time"
                  },
                  "datatype": "time"
                }
              ]
            },
            "qualifiers-order": [
              "P580",
              "P582"
            ],
            "id": "q54384$d1229afb-4fe9-3ada-3372-1ac2ee01f260",
            "rank": "normal"
          }
        ],
        "P18": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P18",
              "hash": "b75943530b775bb038afddd694785717f419863f",
              "datavalue": {
                "value": "STS-124 launch from a distance.jpg",
                "type": "string"
              },
              "datatype": "commonsMedia"
            },
            "type": "statement",
            "id": "q54384$b5f885a8-4727-09a7-9c49-d5a91beffc9e",
            "rank": "normal"
          }
        ],
        "P17": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P17",
              "hash": "be4c6eafa2984964f04be85667263f5642ba1a72",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 30,
                  "id": "Q30"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$4da82248-4375-0cf4-833c-33018175fdbb",
            "rank": "normal"
          }
        ],
        "P138": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P138",
              "hash": "1854ef057accb8754a617cb7ac3d873d8eb77ed9",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 389965,
                  "id": "Q389965"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$0f57f707-447c-4092-afa7-b0519eb19dae",
            "rank": "normal",
            "references": [
              {
                "hash": "58ad2a89695b70ce22c7554cc3409b5c342b2ed8",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3e3dedd67b86dd10ade15ed56118f676a66fa02e",
                      "datavalue": {
                        "value": "https://www.nasa.gov/centers/kennedy/shuttleoperations/orbiters/discovery-info.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P138",
              "hash": "46bfdf9e5287a730e58fcbc97786c22a186c876e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 847233,
                  "id": "Q847233"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$72befb5a-41d5-1324-9e47-dfaca7fb95eb",
            "rank": "normal",
            "references": [
              {
                "hash": "58ad2a89695b70ce22c7554cc3409b5c342b2ed8",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3e3dedd67b86dd10ade15ed56118f676a66fa02e",
                      "datavalue": {
                        "value": "https://www.nasa.gov/centers/kennedy/shuttleoperations/orbiters/discovery-info.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P138",
              "hash": "8b480632a040da76dc122e7396958cc96282d75c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1564604,
                  "id": "Q1564604"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$1f0ef617-46c1-be56-b408-c19317a78d2c",
            "rank": "normal",
            "references": [
              {
                "hash": "58ad2a89695b70ce22c7554cc3409b5c342b2ed8",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3e3dedd67b86dd10ade15ed56118f676a66fa02e",
                      "datavalue": {
                        "value": "https://www.nasa.gov/centers/kennedy/shuttleoperations/orbiters/discovery-info.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P138",
              "hash": "ea50ec5a8f8197ef8c26aae62feca5b05e0d77dd",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 82257,
                  "id": "Q82257"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$860b7f8f-4758-bc65-d3ed-7f0698e1158d",
            "rank": "normal",
            "references": [
              {
                "hash": "58ad2a89695b70ce22c7554cc3409b5c342b2ed8",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "3e3dedd67b86dd10ade15ed56118f676a66fa02e",
                      "datavalue": {
                        "value": "https://www.nasa.gov/centers/kennedy/shuttleoperations/orbiters/discovery-info.html",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P854"
                ]
              }
            ]
          }
        ],
        "P227": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P227",
              "hash": "c9817f0eb6de84076ba073529ee5297050beac80",
              "datavalue": {
                "value": "4467628-1",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$4207265F-D1FB-413C-96BC-B203C401F3B7",
            "rank": "normal",
            "references": [
              {
                "hash": "9a24f7c0208b05d6be97077d855671d1dfdbc0dd",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "d38375ffe6fe142663ff55cd783aa4df4301d83d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 48183,
                          "id": "Q48183"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P646": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P646",
              "hash": "2b10808a2c9ed8ee29dc22a0fd655a846e33e1f2",
              "datavalue": {
                "value": "/m/06_t4",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$A3EC88EC-F9C7-4832-86B7-1C9027913566",
            "rank": "normal",
            "references": [
              {
                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 15241312,
                          "id": "Q15241312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                      "datavalue": {
                        "value": {
                          "time": "+2013-10-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P577"
                ]
              }
            ]
          }
        ],
        "P856": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P856",
              "hash": "5eb23bb16d79613f29192c155a7325759e9512f1",
              "datavalue": {
                "value": "http://www.nasa.gov/centers/kennedy/shuttleoperations/orbiters/discovery-info_prt.htm",
                "type": "string"
              },
              "datatype": "url"
            },
            "type": "statement",
            "qualifiers": {
              "P407": [
                {
                  "snaktype": "value",
                  "property": "P407",
                  "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 1860,
                      "id": "Q1860"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P407"
            ],
            "id": "Q54384$336C3368-850A-40BF-8A12-C32D66131637",
            "rank": "normal",
            "references": [
              {
                "hash": "a29a646602abf65105ed0f39a44231c962ece9ee",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "c6f1777471211df31724ac60175786f3872c83e9",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 177837,
                          "id": "Q177837"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P3417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3417",
              "hash": "a2bb1159f2d7e4054f71e06e66f209488c0ea650",
              "datavalue": {
                "value": "Space-Shuttle-Discovery-2",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$B9948ACC-0D5C-4593-8568-D26326A72C95",
            "rank": "normal",
            "references": [
              {
                "hash": "3b0a5bb3c1f955edce73740124f7d935698092ad",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "3ac9682e789a3a3791d4fd088b265ea03abef101",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 51711,
                          "id": "Q51711"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P137": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P137",
              "hash": "8b2ab6e2110ad80767ac1ce9a57451ddf9e5ef02",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 23548,
                  "id": "Q23548"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$656aeeae-42b6-5058-dfb5-38672c1288c7",
            "rank": "normal"
          }
        ],
        "P3430": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3430",
              "hash": "e95e57db40eb8f2ed60ff585ccae3ebca84d22ce",
              "datavalue": {
                "value": "w6vh9tfx",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$74464fb2-452c-3b86-6db1-c04996f1e87d",
            "rank": "normal"
          }
        ],
        "P1417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1417",
              "hash": "b6a6e393121c02bdabe00b8f67c5546755e962cd",
              "datavalue": {
                "value": "topic/Discovery-space-shuttle",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$A14ED8A7-914D-411A-A3BF-E33339EB642E",
            "rank": "normal"
          }
        ],
        "P244": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P244",
              "hash": "15ca5b385ce235b205746a7ff6deb6705cc642c4",
              "datavalue": {
                "value": "no89003749",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$6017CFDB-23FA-425F-9AD7-C650EA1C20B3",
            "rank": "normal",
            "references": [
              {
                "hash": "ac5d47e9fbcc281bc0d27a205ae02e22ad24ce31",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "b560dc6b281a39d061e189d2eb299a426a06f1a2",
                      "datavalue": {
                        "value": "https://github.com/JohnMarkOckerbloom/ftl/blob/master/data/wikimap",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "0dcf4f64e93fdcc654e2c7534285881fe48b9f3d",
                      "datavalue": {
                        "value": {
                          "time": "+2019-04-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P1296": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1296",
              "hash": "cbad5161d532f83e39192b19edadf0cad639310d",
              "datavalue": {
                "value": "0246506",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$E27D5A4E-5D42-4366-9118-D0FA45C8B361",
            "rank": "normal"
          }
        ],
        "P7818": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7818",
              "hash": "8db38b47cd7474ae5791cfda9d371290707c2c5a",
              "datavalue": {
                "value": "Navette_spatiale_Discovery",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q54384$090E7B04-ACFC-4039-B195-FACF50B2C72D",
            "rank": "normal"
          }
        ],
        "P495": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P495",
              "hash": "7f985e15819b74ed189d022e004890e66d2ae42e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 30,
                  "id": "Q30"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q54384$26EA24F1-2F0B-40FB-944B-2C500E8DB969",
            "rank": "normal",
            "references": [
              {
                "hash": "e1e8b771f3488e41838ba219396070832e6bc22b",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P4656": [
                    {
                      "snaktype": "value",
                      "property": "P4656",
                      "hash": "fa4818266f63feb5eba7060593d522376f38e35b",
                      "datavalue": {
                        "value": "https://en.wikipedia.org/w/index.php?title=Space_Shuttle_Discovery&oldid=945230828",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P143",
                  "P4656"
                ]
              }
            ]
          }
        ]
      },
      "sitelinks": {
        "afwiki": {
          "site": "afwiki",
          "title": "Ruimtependeltuig Discovery",
          "badges": []
        },
        "arwiki": {
          "site": "arwiki",
          "title": "ديسكفري (مكوك فضاء)",
          "badges": []
        },
        "be_x_oldwiki": {
          "site": "be_x_oldwiki",
          "title": "Дыскавэры (шатл)",
          "badges": []
        },
        "bewiki": {
          "site": "bewiki",
          "title": "Шатл Дыскаверы",
          "badges": []
        },
        "bgwiki": {
          "site": "bgwiki",
          "title": "Дискавъри (совалка)",
          "badges": []
        },
        "bnwiki": {
          "site": "bnwiki",
          "title": "ডিসকভারি নভোখেয়াযান",
          "badges": []
        },
        "cawiki": {
          "site": "cawiki",
          "title": "Transbordador espacial Discovery",
          "badges": []
        },
        "commonswiki": {
          "site": "commonswiki",
          "title": "Category:Space Shuttle Discovery",
          "badges": []
        },
        "cswiki": {
          "site": "cswiki",
          "title": "Discovery (raketoplán)",
          "badges": []
        },
        "dawiki": {
          "site": "dawiki",
          "title": "Discovery (rumfærge)",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Discovery (Raumfähre)",
          "badges": []
        },
        "elwiki": {
          "site": "elwiki",
          "title": "Διαστημικό Λεωφορείο Ντισκάβερι",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Space Shuttle Discovery",
          "badges": []
        },
        "eowiki": {
          "site": "eowiki",
          "title": "Kosmopramo Discovery",
          "badges": []
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Transbordador espacial Discovery",
          "badges": []
        },
        "etwiki": {
          "site": "etwiki",
          "title": "Kosmosesüstik Discovery",
          "badges": []
        },
        "euwiki": {
          "site": "euwiki",
          "title": "Discovery (anezka)",
          "badges": []
        },
        "fawiki": {
          "site": "fawiki",
          "title": "فضاپیمای دیسکاوری",
          "badges": []
        },
        "fiwiki": {
          "site": "fiwiki",
          "title": "Discovery (avaruussukkula)",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Discovery (navette spatiale)",
          "badges": []
        },
        "glwiki": {
          "site": "glwiki",
          "title": "Transbordador espacial Discovery",
          "badges": []
        },
        "hewiki": {
          "site": "hewiki",
          "title": "מעבורת החלל דיסקברי",
          "badges": []
        },
        "hiwiki": {
          "site": "hiwiki",
          "title": "डिस्कवरी अंतरिक्ष यान",
          "badges": []
        },
        "huwiki": {
          "site": "huwiki",
          "title": "Discovery űrrepülőgép",
          "badges": []
        },
        "idwiki": {
          "site": "idwiki",
          "title": "Pesawat ulang-alik Discovery",
          "badges": []
        },
        "iowiki": {
          "site": "iowiki",
          "title": "Spaco-paromo Discovery",
          "badges": []
        },
        "itwiki": {
          "site": "itwiki",
          "title": "Space Shuttle Discovery",
          "badges": []
        },
        "jawiki": {
          "site": "jawiki",
          "title": "スペースシャトル・ディスカバリー",
          "badges": []
        },
        "jvwiki": {
          "site": "jvwiki",
          "title": "Discovery (pesawat luar angkasa)",
          "badges": []
        },
        "kawiki": {
          "site": "kawiki",
          "title": "დისკავერი (შატლი)",
          "badges": []
        },
        "kowiki": {
          "site": "kowiki",
          "title": "디스커버리 우주왕복선",
          "badges": []
        },
        "lbwiki": {
          "site": "lbwiki",
          "title": "Discovery (Raumfär)",
          "badges": []
        },
        "ltwiki": {
          "site": "ltwiki",
          "title": "Space Shuttle Discovery",
          "badges": []
        },
        "lvwiki": {
          "site": "lvwiki",
          "title": "Discovery (kosmoplāns)",
          "badges": []
        },
        "mlwiki": {
          "site": "mlwiki",
          "title": "ഡിസ്കവറി സ്പേസ് ഷട്ടിൽ",
          "badges": []
        },
        "mrwiki": {
          "site": "mrwiki",
          "title": "स्पेस शटल डिस्कव्हरी",
          "badges": []
        },
        "mswiki": {
          "site": "mswiki",
          "title": "Bolak-balik angkasa lepas Discovery",
          "badges": []
        },
        "nlwiki": {
          "site": "nlwiki",
          "title": "Discovery (ruimteveer)",
          "badges": []
        },
        "nnwiki": {
          "site": "nnwiki",
          "title": "Romferja «Discovery»",
          "badges": []
        },
        "nowiki": {
          "site": "nowiki",
          "title": "Discovery (romferge)",
          "badges": []
        },
        "plwiki": {
          "site": "plwiki",
          "title": "Discovery (wahadłowiec)",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Discovery (ônibus espacial)",
          "badges": [
            "Q17437798"
          ]
        },
        "rowiki": {
          "site": "rowiki",
          "title": "Naveta spațială Discovery",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Дискавери (шаттл)",
          "badges": []
        },
        "scowiki": {
          "site": "scowiki",
          "title": "Space Shuttle Discovery",
          "badges": []
        },
        "simplewiki": {
          "site": "simplewiki",
          "title": "Space Shuttle Discovery",
          "badges": []
        },
        "skwiki": {
          "site": "skwiki",
          "title": "Discovery (raketoplán)",
          "badges": []
        },
        "slwiki": {
          "site": "slwiki",
          "title": "Raketoplan Discovery",
          "badges": []
        },
        "svwiki": {
          "site": "svwiki",
          "title": "Discovery (rymdfärja)",
          "badges": []
        },
        "tawiki": {
          "site": "tawiki",
          "title": "டிஸ்கவரி விண்ணோடம்",
          "badges": []
        },
        "thwiki": {
          "site": "thwiki",
          "title": "กระสวยอวกาศดิสคัฟเวอรี",
          "badges": []
        },
        "trwiki": {
          "site": "trwiki",
          "title": "Discovery Uzay Mekiği",
          "badges": []
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Діскавері (шатл)",
          "badges": []
        },
        "viwiki": {
          "site": "viwiki",
          "title": "Tàu con thoi Discovery",
          "badges": []
        },
        "yowiki": {
          "site": "yowiki",
          "title": "Ọkọ̀-àlọbọ̀ Òfurufú Discovery",
          "badges": []
        },
        "zhwiki": {
          "site": "zhwiki",
          "title": "發現號太空梭",
          "badges": []
        }
      }
    },
    "Q211051": {
      "pageid": 206770,
      "ns": 0,
      "title": "Q211051",
      "lastrevid": 1279322350,
      "modified": "2020-09-19T19:44:38Z",
      "type": "item",
      "id": "Q211051",
      "labels": {
        "en": {
          "language": "en",
          "value": "Discovery"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "Wikimedia disambiguation page"
        }
      },
      "aliases": {},
      "claims": {
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "0ebb78ffecd3415a2dbc8db900881ff784fead2a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 4167410,
                  "id": "Q4167410"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q211051$B96B71F4-91C1-4F06-8805-FE537A2A9D24",
            "rank": "normal"
          }
        ],
        "P1889": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1889",
              "hash": "1b31f5e1eaf937beb3c7e41caff089f04527ce4f",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2487075,
                  "id": "Q2487075"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1013": [
                {
                  "snaktype": "value",
                  "property": "P1013",
                  "hash": "758a8defa0676780ff8d05bf8a0a446b946af704",
                  "datavalue": {
                    "value": {
                      "entity-type": "item",
                      "numeric-id": 55761780,
                      "id": "Q55761780"
                    },
                    "type": "wikibase-entityid"
                  },
                  "datatype": "wikibase-item"
                }
              ]
            },
            "qualifiers-order": [
              "P1013"
            ],
            "id": "Q211051$aa0a2705-413d-bafd-36dc-8d681bc7d727",
            "rank": "normal",
            "references": [
              {
                "hash": "83dadc88b78cbf9ffb5a563d66e1d31f824bfdb4",
                "snaks": {
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "ae021614fbb48d5cf72d0eb62058820dc2318345",
                      "datavalue": {
                        "value": {
                          "time": "+2019-03-15T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P813"
                ]
              }
            ]
          }
        ],
        "P1365": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1365",
              "hash": "63295c9d018b87cee8fbc88217904a6e18a6183e",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 93178187,
                  "id": "Q93178187"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q211051$88148F16-ADD2-407D-90D9-A20D60DA624E",
            "rank": "normal",
            "references": [
              {
                "hash": "a416ca3230971556eccfbc8a8420bcf52066e312",
                "snaks": {
                  "P3452": [
                    {
                      "snaktype": "value",
                      "property": "P3452",
                      "hash": "713200e6cd22f76ff7f8c7f92aeb12c05ed5abac",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 93178187,
                          "id": "Q93178187"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P3452"
                ]
              }
            ]
          }
        ]
      },
      "sitelinks": {
        "arwiki": {
          "site": "arwiki",
          "title": "ديسكفري (توضيح)",
          "badges": []
        },
        "be_x_oldwiki": {
          "site": "be_x_oldwiki",
          "title": "Discovery",
          "badges": []
        },
        "cawiki": {
          "site": "cawiki",
          "title": "Discovery",
          "badges": []
        },
        "cebwiki": {
          "site": "cebwiki",
          "title": "Discovery",
          "badges": []
        },
        "cswiki": {
          "site": "cswiki",
          "title": "Discovery",
          "badges": []
        },
        "dawiki": {
          "site": "dawiki",
          "title": "Discovery",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Discovery",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Discovery",
          "badges": []
        },
        "eowiki": {
          "site": "eowiki",
          "title": "Discovery",
          "badges": []
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Discovery (desambiguación)",
          "badges": []
        },
        "etwiki": {
          "site": "etwiki",
          "title": "Discovery (täpsustus)",
          "badges": []
        },
        "fawiki": {
          "site": "fawiki",
          "title": "اکتشاف (ابهام‌زدایی)",
          "badges": []
        },
        "fiwiki": {
          "site": "fiwiki",
          "title": "Discovery",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Discovery",
          "badges": []
        },
        "hewiki": {
          "site": "hewiki",
          "title": "דיסקברי",
          "badges": []
        },
        "huwiki": {
          "site": "huwiki",
          "title": "Discovery (egyértelműsítő lap)",
          "badges": []
        },
        "idwiki": {
          "site": "idwiki",
          "title": "Discovery",
          "badges": []
        },
        "itwiki": {
          "site": "itwiki",
          "title": "Discovery",
          "badges": []
        },
        "jawiki": {
          "site": "jawiki",
          "title": "ディスカバリー",
          "badges": []
        },
        "jvwiki": {
          "site": "jvwiki",
          "title": "Discovery",
          "badges": []
        },
        "kowiki": {
          "site": "kowiki",
          "title": "디스커버리",
          "badges": []
        },
        "ndswiki": {
          "site": "ndswiki",
          "title": "Discovery",
          "badges": []
        },
        "nlwiki": {
          "site": "nlwiki",
          "title": "Discovery",
          "badges": []
        },
        "nnwiki": {
          "site": "nnwiki",
          "title": "Discovery",
          "badges": []
        },
        "nowiki": {
          "site": "nowiki",
          "title": "Discovery",
          "badges": []
        },
        "plwiki": {
          "site": "plwiki",
          "title": "Discovery",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Discovery",
          "badges": []
        },
        "rowiki": {
          "site": "rowiki",
          "title": "Discovery",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Discovery",
          "badges": []
        },
        "shwiki": {
          "site": "shwiki",
          "title": "Discovery",
          "badges": []
        },
        "simplewiki": {
          "site": "simplewiki",
          "title": "Discovery",
          "badges": []
        },
        "skwiki": {
          "site": "skwiki",
          "title": "Discovery",
          "badges": []
        },
        "slwiki": {
          "site": "slwiki",
          "title": "Discovery",
          "badges": []
        },
        "svwiki": {
          "site": "svwiki",
          "title": "Discovery",
          "badges": []
        },
        "trwiki": {
          "site": "trwiki",
          "title": "Discovery",
          "badges": []
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Діскавері",
          "badges": []
        },
        "zhwiki": {
          "site": "zhwiki",
          "title": "发现",
          "badges": []
        }
      }
    },
    "Q1901313": {
      "pageid": 1831357,
      "ns": 0,
      "title": "Q1901313",
      "lastrevid": 1280017437,
      "modified": "2020-09-21T07:50:59Z",
      "type": "item",
      "id": "Q1901313",
      "labels": {
        "en": {
          "language": "en",
          "value": "Discovery"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "2001 album by Daft Punk"
        }
      },
      "aliases": {},
      "claims": {
        "P577": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P577",
              "hash": "b620e9344e7dd1569173d01512bc267f118b3657",
              "datavalue": {
                "value": {
                  "time": "+2001-03-03T00:00:00Z",
                  "timezone": 0,
                  "before": 0,
                  "after": 0,
                  "precision": 11,
                  "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                },
                "type": "time"
              },
              "datatype": "time"
            },
            "type": "statement",
            "id": "Q1901313$eea2cc96-489c-4d29-3861-9d2930fd9fb2",
            "rank": "normal"
          }
        ],
        "P175": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P175",
              "hash": "45ffdf325afc8935f50190321e6934d416839693",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 185828,
                  "id": "Q185828"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "q1901313$70BC6BE3-0E54-45FF-B98E-48B437D98F20",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P264": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P264",
              "hash": "0cdc9f5c7475062c72a52b06dcc7dacfb30ae6f4",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 203059,
                  "id": "Q203059"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "q1901313$C7E708CE-1F1D-4F30-BFF4-CBE81E957FCC",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "c61af646fdb2a3c078ee1c5fb85ce38c32faed0c",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 208569,
                  "id": "Q208569"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "q1901313$4FCDE87D-F998-4567-891E-70F082C64760",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P155": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P155",
              "hash": "0e406a21bb3554957119e1282828dcc491fef927",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 920504,
                  "id": "Q920504"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "q1901313$365967F2-C905-41B0-9AB7-155F41A9FDA2",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P156": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P156",
              "hash": "88cd0154cd4dc78a402259ec114328e387690099",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1194636,
                  "id": "Q1194636"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "q1901313$013CC5D3-D4A0-42C3-B9A6-CC3620970F90",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P436": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P436",
              "hash": "e5c0af04e8cfe11ac577847dd1174230ff501a22",
              "datavalue": {
                "value": "48117b90-a16e-34ca-a514-19c702df1158",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "q1901313$0BB5C989-040B-4C1F-900D-499504AB084A",
            "rank": "normal",
            "references": [
              {
                "hash": "706208b3024200fd0a39ad499808dd0d98d74065",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "623cc8f0e2f65afe4d66b91962d354a2f3aa9a27",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 14005,
                          "id": "Q14005"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P646": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P646",
              "hash": "7a2123e27924fe1f8235d6e774b84579bfe52dee",
              "datavalue": {
                "value": "/m/03vzc2",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$0997B6FD-B22D-421C-AA86-97EF22281A64",
            "rank": "normal",
            "references": [
              {
                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 15241312,
                          "id": "Q15241312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                      "datavalue": {
                        "value": {
                          "time": "+2013-10-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P577"
                ]
              }
            ]
          }
        ],
        "P162": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P162",
              "hash": "3d9bf9f90f40e0447741aba7071dc07e9d1adbde",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 185828,
                  "id": "Q185828"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$FDC8B097-9A9A-4B03-AF65-10E124A19679",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P1729": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1729",
              "hash": "46e8c2e842f1c5f40836ef6c41d4a64f92df25d4",
              "datavalue": {
                "value": "mw0000119560",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "qualifiers": {
              "P2093": [
                {
                  "snaktype": "value",
                  "property": "P2093",
                  "hash": "7ca59d9c73883b5e6c06b5e629fee4bb4d211c53",
                  "datavalue": {
                    "value": "John Bush",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P2093"
            ],
            "id": "Q1901313$9212C551-7906-4B1A-9624-D5224EDC684B",
            "rank": "normal",
            "references": [
              {
                "hash": "8df0073e122a5d92d4f711179443974799a3bf19",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "623cc8f0e2f65afe4d66b91962d354a2f3aa9a27",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 14005,
                          "id": "Q14005"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "add7659bae5b35cd46e8de0c32ac6ce3e0ceded6",
                      "datavalue": {
                        "value": {
                          "time": "+2015-09-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P1954": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1954",
              "hash": "434f6ccc6bbca96693e46d79fbbf1ac31414f36d",
              "datavalue": {
                "value": "26647",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$68E03EC7-9797-4900-937A-7747236ECB1E",
            "rank": "normal",
            "references": [
              {
                "hash": "8df0073e122a5d92d4f711179443974799a3bf19",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "623cc8f0e2f65afe4d66b91962d354a2f3aa9a27",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 14005,
                          "id": "Q14005"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "add7659bae5b35cd46e8de0c32ac6ce3e0ceded6",
                      "datavalue": {
                        "value": {
                          "time": "+2015-09-03T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P136": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "db5eecfd40bc3db0327f8025fcfd1ebddb41a889",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 20502,
                  "id": "Q20502"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$0D36CE5B-ED92-4CD3-A531-F147FC1F7C58",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "ec746b51fa6de44683451887ce6aae4ed996a57a",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 58339,
                  "id": "Q58339"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$c4e2efa0-91c5-4bd6-9a44-1e5831783ff7",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "05f9a4a7b560db9f83b1c495b4b982d819c193bf",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1190485,
                  "id": "Q1190485"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$fd49a5d5-fc27-4f06-8af3-b921234614c9",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P136",
              "hash": "26ce942a5c34d8cfbb602d1288729c5acf7cc989",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1455292,
                  "id": "Q1455292"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$95ce770f-a8e9-4bb3-a502-9f31d297cde6",
            "rank": "normal",
            "references": [
              {
                "hash": "fa278ebfc458360e5aed63d5058cca83c46134f1",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "e4f6d9441d0600513c4533c672b5ab472dc73694",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 328,
                          "id": "Q328"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P407": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P407",
              "hash": "daf1c4fcb58181b02dff9cc89deb084004ddae4b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 1860,
                  "id": "Q1860"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$519721C0-23A2-4D03-BB3B-1B9C3DAF8CB7",
            "rank": "normal",
            "references": [
              {
                "hash": "a26de075d569cdc0b76f42996be91cb9f438dfe6",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "1bd14de446e94fd10367d482c65af9203ac07bf9",
                      "datavalue": {
                        "value": "https://rateyourmusic.com/release/album/daft-punk/discovery/",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P1683": [
                    {
                      "snaktype": "value",
                      "property": "P1683",
                      "hash": "44f884856d72205293344a2ecfce48797a7ae022",
                      "datavalue": {
                        "value": {
                          "text": "Language: English",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P1683"
                ]
              }
            ]
          }
        ],
        "P2581": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2581",
              "hash": "63a3b68ad777b4fdec999d0a87e5b669c06bf83a",
              "datavalue": {
                "value": "03874798n",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$1DC5E9FA-3C2B-4905-B24C-77AED550C68A",
            "rank": "normal",
            "references": [
              {
                "hash": "248ac337a217a5f5eed7139a82a4e60931611af0",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "25b816aab41db18565946259c950aed6de05dd1e",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 4837690,
                          "id": "Q4837690"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P248"
                ]
              }
            ]
          }
        ],
        "P1417": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1417",
              "hash": "18e537de2f9ca15a4d21796e91ec86b5faf7b826",
              "datavalue": {
                "value": "topic/Discovery-album-by-Daft-Punk",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$28CEC380-BB5A-44E4-B47F-1C982B82835B",
            "rank": "normal"
          }
        ],
        "P361": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P361",
              "hash": "add30a1486bae1a23c93b6cc48a6cf42ccaf5dcc",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2612773,
                  "id": "Q2612773"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q1901313$a40e883b-4eb8-2e5f-1ee3-d6bef1b4a3ec",
            "rank": "normal"
          }
        ],
        "P4300": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4300",
              "hash": "9083dad2343e808faa2d57ff42d53e5498cfce03",
              "datavalue": {
                "value": "OLAK5uy_mz6eafmqdRHSaR4IwG0ll6J6rgv0_ZpGw",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$5B412769-2B37-4707-9BA1-EEAC247EEF81",
            "rank": "normal",
            "references": [
              {
                "hash": "955f18efe5bbdfdedc4c35d7debc6d97664c7b76",
                "snaks": {
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "a29df15d00c7fc3fb51b2c32e05911e4932f2dcd",
                      "datavalue": {
                        "value": "https://music.youtube.com/playlist?list=OLAK5uy_mz6eafmqdRHSaR4IwG0ll6J6rgv0_ZpGw",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ],
                  "P1476": [
                    {
                      "snaktype": "value",
                      "property": "P1476",
                      "hash": "b28238007a01cee4673dc5c8af63c8465abc7c07",
                      "datavalue": {
                        "value": {
                          "text": "YouTube Music",
                          "language": "en"
                        },
                        "type": "monolingualtext"
                      },
                      "datatype": "monolingualtext"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "c7a3cf0887e1a94bac364752449b07d5eec5d68c",
                      "datavalue": {
                        "value": {
                          "time": "+2020-06-04T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P854",
                  "P1476",
                  "P813"
                ]
              }
            ]
          }
        ],
        "P658": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P658",
              "hash": "af4617568b5b660b9ca899551afb3f8f03b78d52",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2617236,
                  "id": "Q2617236"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1545": [
                {
                  "snaktype": "value",
                  "property": "P1545",
                  "hash": "2a1ced1dca90648ea7e306acbadd74fc81a10722",
                  "datavalue": {
                    "value": "1",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1545"
            ],
            "id": "Q1901313$616c53f4-4ed6-422f-162b-b0c65a823c5f",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P658",
              "hash": "87d869f35d7341e94c8f7e8ba642d81ba39ce7b2",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 2698216,
                  "id": "Q2698216"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "qualifiers": {
              "P1545": [
                {
                  "snaktype": "value",
                  "property": "P1545",
                  "hash": "7241753c62a310cf84895620ea82250dcea65835",
                  "datavalue": {
                    "value": "2",
                    "type": "string"
                  },
                  "datatype": "string"
                }
              ]
            },
            "qualifiers-order": [
              "P1545"
            ],
            "id": "Q1901313$9c0febda-4ae6-8c4f-64c2-7a06b15889b9",
            "rank": "normal"
          }
        ],
        "P5749": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P5749",
              "hash": "f721d7f00b277f1dcb595211f053bc839214f8fb",
              "datavalue": {
                "value": "B0064UPU4G",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$AC0278C8-16A1-4C04-ADCB-29D185D76277",
            "rank": "normal",
            "references": [
              {
                "hash": "f5bdc6cf34489363d66e9288450eb4ff02f007cf",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "fa28758dedb471bbd17a5773562e57ccb962622d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 31181,
                          "id": "Q31181"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e31edae43233ad56359523b1078be66486186ede",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "9c1214d3497d879dc0399065cbd6d4f9c11169c9",
                      "datavalue": {
                        "value": "https://www.allmusic.com/album/mw0000119560",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P813",
                  "P854"
                ]
              }
            ]
          }
        ],
        "P2205": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2205",
              "hash": "17042813d9bf373076eb9ddb542d3ac66d3e216f",
              "datavalue": {
                "value": "2noRn2Aes5aoNVsU6iWThc",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$6CE3C7D1-FEE6-4324-B60A-97928F750F2C",
            "rank": "normal",
            "references": [
              {
                "hash": "f5bdc6cf34489363d66e9288450eb4ff02f007cf",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "fa28758dedb471bbd17a5773562e57ccb962622d",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 31181,
                          "id": "Q31181"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P813": [
                    {
                      "snaktype": "value",
                      "property": "P813",
                      "hash": "e31edae43233ad56359523b1078be66486186ede",
                      "datavalue": {
                        "value": {
                          "time": "+2019-09-26T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ],
                  "P854": [
                    {
                      "snaktype": "value",
                      "property": "P854",
                      "hash": "9c1214d3497d879dc0399065cbd6d4f9c11169c9",
                      "datavalue": {
                        "value": "https://www.allmusic.com/album/mw0000119560",
                        "type": "string"
                      },
                      "datatype": "url"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P813",
                  "P854"
                ]
              }
            ]
          }
        ],
        "P1712": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P1712",
              "hash": "4df75001c4117ac43e811b0ddf60bc3272d59198",
              "datavalue": {
                "value": "music/discovery/daft-punk",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$1C828C86-D2D3-4A2E-986E-61FC5F89C092",
            "rank": "normal"
          }
        ],
        "P2723": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P2723",
              "hash": "be6e22cff65a891b553aecc45523aec0b9b74708",
              "datavalue": {
                "value": "302127",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$73925764-4ac4-e03d-f85a-4824a2a32de7",
            "rank": "normal"
          }
        ],
        "P4199": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P4199",
              "hash": "a98c6397b546a64dff20c21db572003865c3b009",
              "datavalue": {
                "value": "B4t6yqqvhnb2hy4st4uisjrcsrm",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q1901313$562d5dab-4e5d-5de3-98a6-fb36f1954801",
            "rank": "normal"
          }
        ]
      },
      "sitelinks": {
        "dawiki": {
          "site": "dawiki",
          "title": "Discovery (Daft Punk-album)",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Discovery (Daft-Punk-Album)",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Discovery (Daft Punk album)",
          "badges": [
            "Q17437798"
          ]
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Discovery (álbum de Daft Punk)",
          "badges": []
        },
        "fawiki": {
          "site": "fawiki",
          "title": "اکتشاف (آلبوم دفت پانک)",
          "badges": []
        },
        "fiwiki": {
          "site": "fiwiki",
          "title": "Discovery (Daft Punkin albumi)",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Discovery (album de Daft Punk)",
          "badges": []
        },
        "hewiki": {
          "site": "hewiki",
          "title": "דיסקברי (אלבום)",
          "badges": []
        },
        "itwiki": {
          "site": "itwiki",
          "title": "Discovery (Daft Punk)",
          "badges": []
        },
        "jawiki": {
          "site": "jawiki",
          "title": "ディスカバリー (ダフト・パンクのアルバム)",
          "badges": []
        },
        "kawiki": {
          "site": "kawiki",
          "title": "Discovery (Daft Punk-ის ალბომი)",
          "badges": []
        },
        "nlwiki": {
          "site": "nlwiki",
          "title": "Discovery (Daft Punk)",
          "badges": []
        },
        "plwiki": {
          "site": "plwiki",
          "title": "Discovery (Daft Punk)",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Discovery (álbum de Daft Punk)",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Discovery (альбом Daft Punk)",
          "badges": []
        },
        "skwiki": {
          "site": "skwiki",
          "title": "Discovery (Daft Punk)",
          "badges": []
        },
        "svwiki": {
          "site": "svwiki",
          "title": "Discovery (musikalbum av Daft Punk)",
          "badges": []
        },
        "trwiki": {
          "site": "trwiki",
          "title": "Discovery (Daft Punk albümü)",
          "badges": []
        }
      }
    },
    "Q483998": {
      "pageid": 455563,
      "ns": 0,
      "title": "Q483998",
      "lastrevid": 1270656526,
      "modified": "2020-09-03T18:33:39Z",
      "type": "item",
      "id": "Q483998",
      "labels": {
        "en": {
          "language": "en",
          "value": "anagnorisis"
        }
      },
      "descriptions": {
        "en": {
          "language": "en",
          "value": "moment in a play or other work when a character makes a critical discovery"
        }
      },
      "aliases": {
        "en": [
          {
            "language": "en",
            "value": "Agnitio"
          },
          {
            "language": "en",
            "value": "discovery"
          }
        ]
      },
      "claims": {
        "P646": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P646",
              "hash": "d7e0e001d5d929151ee1530e9cf186061226c948",
              "datavalue": {
                "value": "/m/067h0k",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q483998$89249C58-11DD-4201-99D6-8A535FCBD1AB",
            "rank": "normal",
            "references": [
              {
                "hash": "2b00cb481cddcac7623114367489b5c194901c4a",
                "snaks": {
                  "P248": [
                    {
                      "snaktype": "value",
                      "property": "P248",
                      "hash": "a94b740202b097dd33355e0e6c00e54b9395e5e0",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 15241312,
                          "id": "Q15241312"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ],
                  "P577": [
                    {
                      "snaktype": "value",
                      "property": "P577",
                      "hash": "fde79ecb015112d2f29229ccc1ec514ed3e71fa2",
                      "datavalue": {
                        "value": {
                          "time": "+2013-10-28T00:00:00Z",
                          "timezone": 0,
                          "before": 0,
                          "after": 0,
                          "precision": 11,
                          "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                      },
                      "datatype": "time"
                    }
                  ]
                },
                "snaks-order": [
                  "P248",
                  "P577"
                ]
              }
            ]
          }
        ],
        "P31": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "e802e1942c1a9eec231f562312e36be92df69c11",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 15177520,
                  "id": "Q15177520"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q483998$A6739038-F3F3-4F11-8C6C-361C0C3114A7",
            "rank": "normal"
          },
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P31",
              "hash": "2119858156283feb7d5c497eb8a41ca6c4fcfd3b",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 10428845,
                  "id": "Q10428845"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q483998$82b70224-4f73-2953-8cd2-3078f56cb3b3",
            "rank": "normal"
          }
        ],
        "P3365": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P3365",
              "hash": "31770d894ab57f5f73bfdbd28b0d877713f8d52b",
              "datavalue": {
                "value": "agnizione",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q483998$EFDCC8BE-E880-4679-9065-10F9F60636C1",
            "rank": "normal",
            "references": [
              {
                "hash": "d5847b9b6032aa8b13dae3c2dfd9ed5d114d21b3",
                "snaks": {
                  "P143": [
                    {
                      "snaktype": "value",
                      "property": "P143",
                      "hash": "5a343e7e758a4282a01316d3e959b6e653b767fc",
                      "datavalue": {
                        "value": {
                          "entity-type": "item",
                          "numeric-id": 11920,
                          "id": "Q11920"
                        },
                        "type": "wikibase-entityid"
                      },
                      "datatype": "wikibase-item"
                    }
                  ]
                },
                "snaks-order": [
                  "P143"
                ]
              }
            ]
          }
        ],
        "P910": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P910",
              "hash": "b0b6481b4bbdae185098078910f5bc8ffa34bcdc",
              "datavalue": {
                "value": {
                  "entity-type": "item",
                  "numeric-id": 31978821,
                  "id": "Q31978821"
                },
                "type": "wikibase-entityid"
              },
              "datatype": "wikibase-item"
            },
            "type": "statement",
            "id": "Q483998$C56D7C69-3E1F-4AB8-8669-00ADD4AAD54D",
            "rank": "normal"
          }
        ],
        "P6366": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P6366",
              "hash": "7505b0a8bb15fb678170e9eccffb204ae65e7f56",
              "datavalue": {
                "value": "2776691879",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q483998$562A97C3-91F0-432A-B6C5-2F26623E13E7",
            "rank": "normal"
          }
        ],
        "P7982": [
          {
            "mainsnak": {
              "snaktype": "value",
              "property": "P7982",
              "hash": "6bb2ac30f62069ccac675e0ec2f67b62cab020a0",
              "datavalue": {
                "value": "50191",
                "type": "string"
              },
              "datatype": "external-id"
            },
            "type": "statement",
            "id": "Q483998$6F6660A6-A19E-4E7F-894C-4D5E35969743",
            "rank": "normal"
          }
        ]
      },
      "sitelinks": {
        "cawiki": {
          "site": "cawiki",
          "title": "Anagnòrisi",
          "badges": []
        },
        "dewiki": {
          "site": "dewiki",
          "title": "Anagnorisis",
          "badges": []
        },
        "enwiki": {
          "site": "enwiki",
          "title": "Anagnorisis",
          "badges": []
        },
        "eswiki": {
          "site": "eswiki",
          "title": "Anagnórisis",
          "badges": []
        },
        "fawiki": {
          "site": "fawiki",
          "title": "بازشناخت",
          "badges": []
        },
        "frwiki": {
          "site": "frwiki",
          "title": "Anagnorisis",
          "badges": []
        },
        "glwiki": {
          "site": "glwiki",
          "title": "Anagnórise",
          "badges": []
        },
        "iawiki": {
          "site": "iawiki",
          "title": "Anagnorisis",
          "badges": []
        },
        "iswiki": {
          "site": "iswiki",
          "title": "Kennsl",
          "badges": []
        },
        "itwiki": {
          "site": "itwiki",
          "title": "Agnizione",
          "badges": []
        },
        "lawiki": {
          "site": "lawiki",
          "title": "Anagnorisis",
          "badges": []
        },
        "nlwiki": {
          "site": "nlwiki",
          "title": "Agnitio",
          "badges": []
        },
        "ptwiki": {
          "site": "ptwiki",
          "title": "Anagnórise",
          "badges": []
        },
        "ruwiki": {
          "site": "ruwiki",
          "title": "Узнавание",
          "badges": []
        },
        "sdwiki": {
          "site": "sdwiki",
          "title": "ايناگورسس",
          "badges": []
        },
        "shwiki": {
          "site": "shwiki",
          "title": "Anagnorizam",
          "badges": []
        },
        "ukwiki": {
          "site": "ukwiki",
          "title": "Анагноризм",
          "badges": []
        },
        "zhwiki": {
          "site": "zhwiki",
          "title": "醒悟",
          "badges": []
        }
      }
    }
  },
  "success": 1
}
```
