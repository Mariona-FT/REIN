from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from elasticsearch.exceptions import NotFoundError

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=None, required=True, help='Index to search')

    args = parser.parse_args()

    index = args.index
    print("hola1")
    try:
        client = Elasticsearch()
        sc = scan(client, index=index, query={"query": {"match_all": {}}})
        print("hola")
        for r in sc:
            print(r['_source']['path'], '\t', r['_source']['text'].encode('ascii','replace'))
    except NotFoundError:
        raise(NameError(f'Index {index} does not exist'))


