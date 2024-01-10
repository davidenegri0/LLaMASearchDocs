from elasticsearch import Elasticsearch

INDEX_NAME = "ieee_db"

elastic_client = Elasticsearch("http://localhost:9200")

elastic_client.indices.delete(index=INDEX_NAME)