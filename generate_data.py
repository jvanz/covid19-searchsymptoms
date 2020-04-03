from datetime import datetime

import pandas as pd
import numpy as np
import elasticsearch

INDEX_NAME = "consultas"
SINTOMAS = [
    "dor de cabeça",
    "febre",
    "falte de ar",
    "coriza",
    "diarreia",
    "dor de barriga",
    "dor muscular",
    "dor abdominal",
    "perda de cabelo",
    "tontura",
]


def get_data(samples_count=500):
    """
    Gera uma lista aleatoria de descrições de sintomes. Retona a lista com um
    id e sintomas.
    """
    samples = []
    for i in range(samples_count):
        np.random.shuffle(SINTOMAS)
        samples.append([i, " ".join(SINTOMAS[:3])])
    return samples


def generate_dataset():
    """
    Gera um arquivo CSV com dados aleatorios de consultas.
    """
    # Gera dados ficticios de descrições de doencas
    data = pd.DataFrame(data=get_data(), columns=["id", "descricao"])
    data.to_csv("data.csv", index=False)


def create_es_index(es):
    """
    Cria o indece "consultas" no ElasticSearch.
    """
    es.indices.delete(index=INDEX_NAME)
    es.indices.create(index=INDEX_NAME, ignore=400)


def load_data_into_es(es):
    """
    Carrega dos dados do csv no indece do ElasticSearch.
    """
    data = pd.read_csv("data.csv", index_col="id")
    for entry in data.itertuples():
        ret = es.index(
            index=INDEX_NAME,
            id=entry.Index,
            body={
                "id": entry.Index,
                "descricao": entry.descricao,
                "timestamp": datetime.now(),
            },
        )
        print(ret)


def query_es(es):
    """
    Busca um registro simples para ver se o indece esta funcionando.
    """
    print(es.get(index=INDEX_NAME, id=77)["_source"])


def main():
    generate_dataset()

    es = elasticsearch.Elasticsearch(hosts=["localhost"])
    create_es_index(es)
    load_data_into_es(es)

    query_es(es)


if __name__ == "__main__":
    main()
