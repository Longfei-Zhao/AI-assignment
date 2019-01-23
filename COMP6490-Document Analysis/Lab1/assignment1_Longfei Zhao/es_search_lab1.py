import config
from io import open
import re, json
from elasticsearch import Elasticsearch
from es_helper import analyze_query, search, extract_response

def main():
    es_conn = Elasticsearch(config.ES_HOSTS)
    f = open('retrieved.txt', 'w')
    for line in open('../gov-test-collection/topics/gov.topics'):
        content = line.split()
        index = content.pop(0)
        query = ' '.join(content)

        matches = search(query, es_conn, config.INDEX_NAME)
        if matches is not None:
            num = 0
            for match in sorted(matches, key = lambda x: -x[1]):
                f.write(str(index) + ' Q0 ' + match[0] + ' ' + str(num) + ' ' + str(match[1]) + " longfei\n")
                num += 1
if __name__ == '__main__':
    main()
