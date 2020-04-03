import sys
import json

import elasticsearch

INDEX_NAME = "consultas"


def get_symptoms():
    """
    Retorna a query string passada como argumento da linha de comando.
    """

    return " ".join(sys.argv[1:])


def main():
    """
    Pesquisa as entradas no ES utlizando a query string passada na linha de
    comando.
    """

    es = elasticsearch.Elasticsearch(hosts=["localhost"])
    symptoms = get_symptoms()
    # gera a query do ES
    query = {
        "query": {"query_string": {"query": symptoms, "default_field": "descricao"}}
    }
    result = es.search(index=INDEX_NAME, body=query)
    print(json.dumps(result))
    for hit in result["hits"]["hits"]:
        print(hit["_source"])


if __name__ == "__main__":
    main()
