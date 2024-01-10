from elasticsearch import Elasticsearch

elastic_client = Elasticsearch("http://localhost:9200")

mapping = {
    "properties": {
        "my_vector": {
            "type": "dense_vector",
            "dims": 4096,
            "index": 'true',
            "similarity": "cosine"
        },
        "my_text" : {
            "type" : "text"
        }
    }
}

elastic_client.indices.create(index="test_vector", mappings=mapping)