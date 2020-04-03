# covid19-searchsymptoms

Para rodar o script que popula o ES com dados aleatórios:

```bash
make runes
pip install --user -r requirements.txt
python3 generate_data.py
```

Roda um busca no ES utilizando a [query string](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html) passada na linha de comando

```bash
jvanz@earth:~/covid19-search> python3 search.py "febre"
{"took": 1, "timed_out": false, "_shards": {"total": 1, "successful": 1, "skipped": 0, "failed": 0}, "hits": {"total": {"value": 133, "relation": "eq"}, "max_score": 1.6611487, "hits": [{"_index": "consultas", "
_type": "_doc", "_id": "4", "_score": 1.6611487, "_source": {"id": 4, "descricao": "febre tontura coriza", "timestamp": "2020-04-02T20:41:32.713836"}}, {"_index": "consultas", "_type": "_doc", "_id": "51", "_sco
re": 1.6611487, "_source": {"id": 51, "descricao": "febre diarreia tontura", "timestamp": "2020-04-02T20:41:33.339701"}}, {"_index": "consultas", "_type": "_doc", "_id": "176", "_score": 1.6611487, "_source": {"
id": 176, "descricao": "coriza diarreia febre", "timestamp": "2020-04-02T20:41:35.155054"}}, {"_index": "consultas", "_type": "_doc", "_id": "194", "_score": 1.6611487, "_source": {"id": 194, "descricao": "febre
 tontura coriza", "timestamp": "2020-04-02T20:41:35.434996"}}, {"_index": "consultas", "_type": "_doc", "_id": "209", "_score": 1.6611487, "_source": {"id": 209, "descricao": "diarreia coriza febre", "timestamp$
: "2020-04-02T20:41:35.645286"}}, {"_index": "consultas", "_type": "_doc", "_id": "220", "_score": 1.6611487, "_source": {"id": 220, "descricao": "febre coriza tontura", "timestamp": "2020-04-02T20:41:35.801045$
}}, {"_index": "consultas", "_type": "_doc", "_id": "222", "_score": 1.6611487, "_source": {"id": 222, "descricao": "diarreia coriza febre", "timestamp": "2020-04-02T20:41:35.824905"}}, {"_index": "consultas", $
_type": "_doc", "_id": "224", "_score": 1.6611487, "_source": {"id": 224, "descricao": "diarreia coriza febre", "timestamp": "2020-04-02T20:41:35.848044"}}, {"_index": "consultas", "_type": "_doc", "_id": "230"$
 "_score": 1.6611487, "_source": {"id": 230, "descricao": "tontura febre diarreia", "timestamp": "2020-04-02T20:41:35.936112"}}, {"_index": "consultas", "_type": "_doc", "_id": "232", "_score": 1.6611487, "_sou$
ce": {"id": 232, "descricao": "febre diarreia tontura", "timestamp": "2020-04-02T20:41:35.967557"}}]}}
{'id': 4, 'descricao': 'febre tontura coriza', 'timestamp': '2020-04-02T20:41:32.713836'}
{'id': 51, 'descricao': 'febre diarreia tontura', 'timestamp': '2020-04-02T20:41:33.339701'}
{'id': 176, 'descricao': 'coriza diarreia febre', 'timestamp': '2020-04-02T20:41:35.155054'}
{'id': 194, 'descricao': 'febre tontura coriza', 'timestamp': '2020-04-02T20:41:35.434996'}
{'id': 209, 'descricao': 'diarreia coriza febre', 'timestamp': '2020-04-02T20:41:35.645286'}
{'id': 220, 'descricao': 'febre coriza tontura', 'timestamp': '2020-04-02T20:41:35.801045'}
{'id': 222, 'descricao': 'diarreia coriza febre', 'timestamp': '2020-04-02T20:41:35.824905'}
{'id': 224, 'descricao': 'diarreia coriza febre', 'timestamp': '2020-04-02T20:41:35.848044'}
{'id': 230, 'descricao': 'tontura febre diarreia', 'timestamp': '2020-04-02T20:41:35.936112'}
{'id': 232, 'descricao': 'febre diarreia tontura', 'timestamp': '2020-04-02T20:41:35.967557'}
jvanz@earth:~/covid19-search> python3 search.py "febre NOT coriza"
{"took": 2, "timed_out": false, "_shards": {"total": 1, "successful": 1, "skipped": 0, "failed": 0}, "hits": {"total": {"value": 100, "relation": "eq"}, "max_score": 1.6611487, "hits": [{"_index": "consultas", $
_type": "_doc", "_id": "51", "_score": 1.6611487, "_source": {"id": 51, "descricao": "febre diarreia tontura", "timestamp": "2020-04-02T20:41:33.339701"}}, {"_index": "consultas", "_type": "_doc", "_id": "230",
"_score": 1.6611487, "_source": {"id": 230, "descricao": "tontura febre diarreia", "timestamp": "2020-04-02T20:41:35.936112"}}, {"_index": "consultas", "_type": "_doc", "_id": "232", "_score": 1.6611487, "_sour$
e": {"id": 232, "descricao": "febre diarreia tontura", "timestamp": "2020-04-02T20:41:35.967557"}}, {"_index": "consultas", "_type": "_doc", "_id": "346", "_score": 1.6611487, "_source": {"id": 346, "descricao"$
 "diarreia febre tontura", "timestamp": "2020-04-02T20:41:37.607830"}}, {"_index": "consultas", "_type": "_doc", "_id": "466", "_score": 1.6611487, "_source": {"id": 466, "descricao": "febre tontura diarreia", $
timestamp": "2020-04-02T20:41:39.108940"}}, {"_index": "consultas", "_type": "_doc", "_id": "36", "_score": 1.5297056, "_source": {"id": 36, "descricao": "tontura febre dor muscular", "timestamp": "2020-04-02T2$
:41:33.124342"}}, {"_index": "consultas", "_type": "_doc", "_id": "38", "_score": 1.5297056, "_source": {"id": 38, "descricao": "dor abdominal diarreia febre", "timestamp": "2020-04-02T20:41:33.150983"}}, {"_in$
ex": "consultas", "_type": "_doc", "_id": "45", "_score": 1.5297056, "_source": {"id": 45, "descricao": "dor muscular febre diarreia", "timestamp": "2020-04-02T20:41:33.252836"}}, {"_index": "consultas", "_type$
: "_doc", "_id": "70", "_score": 1.5297056, "_source": {"id": 70, "descricao": "febre dor muscular tontura", "timestamp": "2020-04-02T20:41:33.607842"}}, {"_index": "consultas", "_type": "_doc", "_id": "110", "$
score": 1.5297056, "_source": {"id": 110, "descricao": "febre tontura dor muscular", "timestamp": "2020-04-02T20:41:34.208261"}}]}}
{'id': 51, 'descricao': 'febre diarreia tontura', 'timestamp': '2020-04-02T20:41:33.339701'}
{'id': 230, 'descricao': 'tontura febre diarreia', 'timestamp': '2020-04-02T20:41:35.936112'}
{'id': 232, 'descricao': 'febre diarreia tontura', 'timestamp': '2020-04-02T20:41:35.967557'}
{'id': 346, 'descricao': 'diarreia febre tontura', 'timestamp': '2020-04-02T20:41:37.607830'}
{'id': 466, 'descricao': 'febre tontura diarreia', 'timestamp': '2020-04-02T20:41:39.108940'}
{'id': 36, 'descricao': 'tontura febre dor muscular', 'timestamp': '2020-04-02T20:41:33.124342'}
{'id': 38, 'descricao': 'dor abdominal diarreia febre', 'timestamp': '2020-04-02T20:41:33.150983'}
{'id': 45, 'descricao': 'dor muscular febre diarreia', 'timestamp': '2020-04-02T20:41:33.252836'}
{'id': 70, 'descricao': 'febre dor muscular tontura', 'timestamp': '2020-04-02T20:41:33.607842'}
{'id': 110, 'descricao': 'febre tontura dor muscular', 'timestamp': '2020-04-02T20:41:34.208261'}
```
