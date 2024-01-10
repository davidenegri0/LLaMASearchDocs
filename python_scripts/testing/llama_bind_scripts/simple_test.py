from llama_cpp import Llama

llm = Llama(model_path="/home/ubuntu/llama_cpp_CPUonly/models/7B/ggml-model-q4_0.gguf", n_ctx=256)

prompt = input("Insert a question for Llama: ")

output = llm(prompt, max_tokens=256)

print(output.get('choices')[0].get('text'))