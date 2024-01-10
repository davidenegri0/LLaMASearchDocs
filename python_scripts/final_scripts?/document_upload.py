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

# Read del documento:
# ... Documento d'esempio preso da https://ieeexplore.ieee.org/document/9910561
id = "4testing"
authors = ["Kunal Yadav", "Ping-Hsuan Hsieh", "Anthony Chan Carusone"]
title = "Loop Dynamics Analysis of PAM-4 Mueller-Muller Clock and Data Recovery System"
doi = "10.1109/OJCAS.2022.3211844"
year = "2022"
issue = 3
abstract = "This paper provides a framework for analyzing the loop dynamics of the clock and data recovery (CDR) system of ADC-based PAM-4 receivers, which will assist in extending the timing recovery loop bandwidth. This paper formulates an accurate linear model of linear and signed Mueller–Muller phase detector for baud-rate clock recovery. Different equalization configurations of continuous-time linear equalizer (CTLE) and feed-forward equalizer (FFE) are evaluated from a phase detector performance perspective to enable high CDR loop bandwidth. The impact of loop latency on the timing recovery of ADC-based PAM-4 receivers is also analyzed and demonstrated using accurate behavioral simulations. The analysis and behavioral results show that, to achieve high CDR loop bandwidth with a good jitter tolerance, the phase detector gain to noise ratio should be maximized, and CDR loop latency should be minimized."
keywords = ["Detectors", "Timing", "Bandwidth", "Jitter", "Clocks", "Standards", "Receivers"]

embedded_abstract = embeddings.embed_query(abstract)

paper = {
            "embedding": embedded_abstract,
            'id':id,
            'authors':authors,
            'title':title,
            'doi':doi,
            'year':year,
            'issue':issue,
            'abstract':abstract,
            'keywords':keywords
        }
            
elastic_client.index(index=INDEX_NAME, id=paper['id'], document=paper)