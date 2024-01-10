from elasticsearch import Elasticsearch

elastic_client = Elasticsearch("http://localhost:9200")

elastic_client.indices.delete(index="test_vector")