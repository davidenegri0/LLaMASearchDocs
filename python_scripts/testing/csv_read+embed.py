import csv
from langchain.embeddings import LlamaCppEmbeddings

# Parametri
llama_model_path = "/home/ubuntu/llama_cpp_CPUonly/models/7B/ggml-model-q4_0.gguf"
cvs_source_file_path = "/home/ubuntu/ieee.documents.csv"
output_file_path = "/home/ubuntu/llama_cpp_CPUonly/python_scripts/testing/abstract_embedding_2.txt"

# Model start
embeddings = LlamaCppEmbeddings(model_path=llama_model_path)

# Lettura CSV
with open(cvs_source_file_path, newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    rows = iter(csv_data)
    next(rows)  #Skip prima riga di definizione tipi di dato
    first_row = next(rows)
    cols = iter(first_row)
    for i in range(23):     #Skip di 23 colonne per campi inutilizzati 
        next(cols)
    abstract = next(cols)

# Calcolo embedding
embedded_abstract = embeddings.embed_query(abstract)
   
with open(output_file_path, 'w') as file:
    file.write(f'{abstract}\n{embedded_abstract}')