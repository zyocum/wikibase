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
    ...
```