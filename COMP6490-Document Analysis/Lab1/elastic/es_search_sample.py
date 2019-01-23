#
# Created by Umanga Bista.
#

import config
from io import open
import re, json
from elasticsearch import Elasticsearch
from es_helper import analyze_query, search, extract_response

def print_result(index, res, resf):
    matches = extract_response(res)
    if matches is not None:
        num = 0
        for match in sorted(matches, key = lambda x: -x[1]):
            resf.write(str(index) + ' Q0 ' + match[0] + ' ' + str(num) + ' ' + str(match[1]) + " longfei\n")
            num += 1

def main():
    es_conn = Elasticsearch(config.ES_HOSTS)

    # Elasticsearch Query grammar can be found here:
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html
    # To understand score of the result, check:
    # https://www.elastic.co/guide/en/elasticsearch/guide/current/relevance-intro.html#explain

    # Boolean Query "Obama"
    f = open('../gov-test-collection/topics/gov.topics')

    resf = open('retrieved.txt', 'w')

    for line in f:
        index = line[:2]
        query = line[3:]

        res = es_conn.search(index = config.INDEX_NAME,
            body={
                  "_source": ["filename"],
                  "query": {
                    "match" : {
                      "text" : {
                        "query" : query,
                      }
                    }
                  }
                }
            )
        print_result(index, res, resf)

if __name__ == '__main__':
    main()
