from langchain.embeddings import LlamaCppEmbeddings
from elasticsearch import Elasticsearch
import json

llama_model_path = "models/7B/ggml-model-q4_0.gguf"

Dante = [
    "When I had journeyed half of our life's way,",
    "I found myself within a shadowed forest,",
    "for I had lost the path that does not stray.",
    "Ah, it is hard to speak of what it was,",
    "that savage forest, dense and difficult,",
    "which even in recall renews my fear:",
    "so bitter-death is hardly more severe!",
    "But to retell the good discovered there,",
    "I'll also tell the other things I saw."
]

counter = 0

mapping = {
    "properties": {
        "vector": {
            "type": "dense_vector",
            "dims": 4096,
            "index": 'true',
            "similarity": "cosine"
        },
        "quote" : {
            "type" : "text"
        }
    }
}

elastic_client = Elasticsearch("http://localhost:9200")
embeddings = LlamaCppEmbeddings(model_path=llama_model_path, n_gpu_layers=16)

print("\n-----------------\n1: Crea l'index\n2: Elimina l'index\n3: Inserisci l'embedding\n4: VectorSearch\n9: Chiudi\n-----------------\n")

while(True):
    command = int(input("Inserisci il comando:\t"))
    match command:
        case 1:
            elastic_client.indices.create(index="dante_vector_search", mappings=mapping)
            print("\nCreazione indice completata\n")
        case 2:
            # while(counter>0):
            #     counter -= 1
            #     elastic_client.delete(index="dante_vector_search", id="divina"+str(counter))
            elastic_client.indices.delete(index="dante_vector_search")
            print("\nEliminazione indice completata\n")
        case 3:
            if(counter<len(Dante)):
                embedding = embeddings.embed_query(Dante[counter])
                elastic_client.index(
                    index="dante_vector_search",
                    id="divina"+str(counter),
                    document={
                        "vector" : embedding,
                        "quote" : Dante[counter]
                    }
                )
                
                print(f"\nInserimento dell'embedding di \"{Dante[counter]}\" completata\n")
                
                counter +=1
            else:
                print("Dante c'è tutto!")
        case 4:
            search = input("Inserisci ciò che cerchi nella Divina Commedia: ")
            search_embed = embeddings.embed_query(search)
            
            query = {
                "field": "vector",
                "query_vector": search_embed,
                "k": 2,
                "num_candidates": 100
            }
            
            result = elastic_client.knn_search(index="dante_vector_search", knn=query, source=["vector", "quote"])
            result = result['hits']['hits']
            
            print("\nRisultati della ricerca:")
            for r in result:
                print(r['_source']['quote'])
            print("\n")
            
            # with open("python_scripts/result.txt", "w") as outfile:
            #     for r in result:
            #         outfile.write(r['_source']['quote']+"\n")
        case 9:
            exit(0)