from elasticsearch import Elasticsearch

INDEX_NAME = "ieee_db"

elastic_client = Elasticsearch("http://localhost:9200")

mapping = {
    "properties": {
        "embedding": {
            "type": "dense_vector",
            "dims": 4096,
            "index": 'true',
            "similarity": "cosine"
        },
        'id' : {
            "type" : "text"
        },
        'authors':{
            "type" : "text"           
        },
        'title':{
            "type" : "text"
        },
        'doi':{
            "type" : "text"
        },
        'year':{
            "type" : "text"
        },
        'issue':{
            "type" : "short"
        },
        'abstract':{
            "type" : "text"
        },
        'keywords':{
            "type" : "text"
        }
    }
}

elastic_client.indices.create(index=INDEX_NAME, mappings=mapping)