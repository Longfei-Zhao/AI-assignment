#
# Created by Umanga Bista.
#

import config_gov
from io import open
import re, json
from elasticsearch import Elasticsearch
from es_helper_gov import analyze_query, search, extract_response

def main():
    es_conn = Elasticsearch(config_gov.ES_HOSTS)

    # Elasticsearch Query grammar can be found here:
    # https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html
    # To understand score of the result, check:
    # https://www.elastic.co/guide/en/elasticsearch/guide/current/relevance-intro.html#explain

    # Boolean Query "gov.topics"
    # default is OR

    f = open('../gov-test-collection/topics/gov.topics')
    retrievedOutput = open('retrieved_gov.txt','wt')
    for line in f:
        keywordLine = line.split(' ')
        queryID = keywordLine[0]
        del keywordLine[0]
        #queryKeyword = keywordLine
        queryKeyword = analyze_query(' '.join(keywordLine), es_conn, config_gov.INDEX_NAME)
        #print queryKeyword
        '''     
        res = es_conn.search(index=config_gov.INDEX_NAME,
                             body={
                                 "_source": ["filename"],
                                 "query": {
                                     "match": {
                                         "text": {
                                             "query": queryKeyword,
                                         }
                                     }
                                 }
                             }
                             )                     
        matches = extract_response(res)
        '''

        matches = search(' '.join(queryKeyword),es_conn,config_gov.INDEX_NAME)

        if matches is not None:
            orderCount = 0
            for match in sorted(matches, key=lambda x: -x[1]):
                '''
               outputLine  = '{} {} {} {} {}'.format(
                    queryID,
                    'Q0',
                    match[0],  # filename
                    match[1],  # score
                    'my_IR_system1 \n'
                ) 
               '''

                outputLine = str(queryID) + ' Q0 ' + str(match[0]) + ' ' + str(orderCount) + ' ' + str(match[1]) + ' my_IR_system1 ' + '\n'
                retrievedOutput.write(unicode(outputLine))
                print outputLine
                orderCount += 1
        #print queryKeyword
    retrievedOutput.close()


if __name__ == '__main__':
    main()
