import config
from io import open
import re, json
from elasticsearch import Elasticsearch
from es_helper import analyze_query, search, extract_response

def print_result(query, res):
    matches = extract_response(res)
    if matches is not None:
        for match in sorted(matches, key = lambda x: -x[1]):
            print('{}, {}, {}'.format(
                query,
                match[0], # filename
                match[1], # score
            ))

def main():
    es_conn = Elasticsearch(config.ES_HOSTS)

    # Elasticsearch Query grammar can be found here:
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html
    # To understand score of the result, check:
    # https://www.elastic.co/guide/en/elasticsearch/guide/current/relevance-intro.html#explain

    # Boolean Query "Obama"
    f = open('../lab1-q1/topics/air.topics')
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
        print(res)
        print_result(query, res)

if __name__ == '__main__':
    main()
