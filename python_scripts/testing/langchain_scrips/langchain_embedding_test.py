from langchain.embeddings import LlamaCppEmbeddings

llama_model_path = "/home/ubuntu/llama_cpp_CPUonly/models/7B/ggml-model-q4_0.gguf"
test_string = "Llama"

embeddings = LlamaCppEmbeddings(model_path=llama_model_path)

test_embedding = embeddings.embed_query(test_string)

with open("/home/ubuntu/llama_cpp_CPUonly/python_scripts/langchain_scrips/test.txt", 'w') as file:
    for num in test_embedding:
        file.write(f'{num}\n')