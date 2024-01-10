import csv
from elasticsearch import Elasticsearch
from langchain.embeddings import LlamaCppEmbeddings

# Parametri
llama_model_path = "/home/ubuntu/llama_cpp_CPUonly/models/7B/ggml-model-q4_0.gguf"
cvs_source_file_path = "/home/ubuntu/ieee.documents.csv"

# Model start
embeddings = LlamaCppEmbeddings(model_path=llama_model_path)

# Elasticsearch conneto to db
elastic_client = Elasticsearch("http://localhost:9200")

# Nome dell'index
INDEX_NAME = "ieee_db"
# Parametro per impostare il numero di entry da caricare e saltare
ENTRIES_TO_LOAD = 2103
ENTRIES_TO_SKIP = 2088

# Lettura del file e salvataggio su db
with open(cvs_source_file_path, newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    rows = iter(csv_data)
    next(rows)
    print(f"Righe da inserire {ENTRIES_TO_LOAD}")
    for i in range(ENTRIES_TO_LOAD):
        print(f"Riga {i}")
        row = next(rows)
        if(i > ENTRIES_TO_SKIP):
            cols = iter(row)
            id = next(cols)
            authors = []
            for j in range(18):
                author = next(cols)
                if(author!=''): 
                    authors.append(author)
            title = next(cols)
            doi = next(cols)
            year = next(cols)
            issue = next(cols)
            abstract = next(cols)
            keywords = []
            for j in range(27):
                keyword = next(cols)
                if(keyword!=''):
                    keywords.append(keyword)
            
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
            
            print(f"Documento n°{i} (id:{id}) è stato caricato")