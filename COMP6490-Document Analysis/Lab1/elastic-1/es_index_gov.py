#
# Created by Umanga Bista.
#

from elasticsearch import Elasticsearch
from data import read_dataset
import config_gov
from es_helper_gov import create_index

def main():
    ## create an es client
    es_conn = Elasticsearch(config_gov.ES_HOSTS)
    ## create the index if it doesn't exist
    create_index(es_conn = es_conn, index_name = config_gov.INDEX_NAME)
    dataset = read_dataset(config_gov.DOCS_PATH)
    counter_read, counter_idx_failed = 0, 0 ## counters

    while True:
        try:
            doc = next(dataset)
            res = es_conn.index(
                index = config_gov.INDEX_NAME,
                doc_type = config_gov.DOC_TYPE,
                id = doc.filename,
                body = doc._asdict())
            counter_read += 1

            if counter_read % config_gov.PRINT_EVERY == 0:
                print('indexed {} documents'.format(counter_read))

            if not res['created']:
                print('indexing `{}` failed'.format(doc.path))
                counter_idx_failed += 1

        except StopIteration:
            print('finished reading docs from `{}`'.format(config_gov.DOCS_PATH))
            break

    print('indexed {} docs to index `{}`, failed to index {} docs'.format(
        counter_read,
        config_gov.INDEX_NAME,
        counter_idx_failed
    ))

if __name__ == '__main__':
    main()
