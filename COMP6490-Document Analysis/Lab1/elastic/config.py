# ES CONNECTION SETTINGS
# elasticsearch hosts
ES_HOSTS = ['http://localhost:9200']

########################################################################
########################### ES INDEXING SETTINGS #######################
## path to es_settings.json
## documentation here: https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis.html
SETTINGS_PATH = './es_settings_english.json'
DOC_TYPE = 'doc' ## this should match with es_settings_sample.json

## path to the sample collection of documents
DOCS_PATH = '../gov-test-collection/documents/'
INDEX_NAME = 'longfei' ## name of index

## print to stdout after indexing this many docs
PRINT_EVERY = 1

########################################################################
######################### ES SEARCH SETTINGS ###########################
# path to the query file
# you can make your search algorithm read queries from the following path and generate outputs
QUERY_TOPICS_PATH = '../gov-test-collection/topics/gov.topics'

MY_NAME = 'longfei' ## as in assignment doc
