import json
from elasticsearch import Elasticsearch
from langchain.embeddings import LlamaCppEmbeddings

# Parametri
llama_model_path = "/home/ubuntu/llama_cpp_CPUonly/models/7B/ggml-model-q4_0.gguf"
# Nome dell'index
INDEX_NAME = "ieee_db"

# Model start
embeddings = LlamaCppEmbeddings(model_path=llama_model_path)

# Elasticsearch conneto to db
elastic_client = Elasticsearch("http://localhost:9200")

abstract = "Web applications have been increasingly deployed on the Internet. How to effectively allocate system resources to meet the Service Level Objectives (SLOs) is a challenging problem for Web application providers. In this article, we propose a scheme for automated performance control of Web applications via dynamic resource allocations. The scheme uses a queueing model predictor and an online adaptive feedback loop that enforces admission control of the incoming requests to ensure the desired response time target is met. The proposed Queueing-Model-Based Adaptive Control approach combines both the modeling power of queueing theory and the self-tuning power of adaptive control. Therefore, it can handle both modeling inaccuracies and load disturbances in a better way. To evaluate the proposed approach, we built a multi-tiered Web application testbed with open-source components widely adopted in industry. Experimental studies conducted on the testbed demonstrated the effectiveness of the proposed scheme."

embedded_abstract = embeddings.embed_query(abstract)

res = elastic_client.search(index=INDEX_NAME, knn={"field": "embedding", "k":3, "num_candidates": 10, "query_vector": embedded_abstract}, pretty=True)

# print(res)

to_print = res["hits"]["hits"]

with open("result.json", "w") as file:
    json.dump(to_print, file, indent=2)