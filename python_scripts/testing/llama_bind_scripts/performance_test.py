from llama_cpp import Llama
from time import perf_counter

prompts = [
    "In Greek mythology, who were Hades' parents?",
    "Which country is ruled by the Al Sabah dynasty?",
    "How many black keys are found on a traditional 88-key piano?"
]

# DEBUG_MODE = False

timings_CPU = []
# timings_GPU = []
responses_CPU = []
responses_GPU = []

print("Lista dei prompt:")
for p in prompts:
    print("\t" + p)

llm = Llama(model_path="/home/ubuntu/llama_cpp_CPUonly/models/7B/ggml-model-q4_0.gguf", n_gpu_layers=0)

#subprocess.run("watch -n 5 \"ps u --no-headers | sort -k 6 -n -r >> python_scrips/ps_output.txt\"", shell=True, timeout=500)

for prompt in prompts:
    start = perf_counter()
    output = llm(prompt, max_tokens=-1)
    time = perf_counter() - start
    # if(DEBUG_MODE): 
    #     print(output.get('choices')[0].get('text'))
    timings_CPU.append(time)
    responses_CPU.append(output.get('choices')[0].get('text'))
    
print("\nDi seguito verranno riportati i tempi di esecurzione dei prompt richiesti:\n")
for i in range(0, len(prompts)):
    print(f"Tempi di esecuzione prompt {i}:\tCPU={timings_CPU[i]}")
    
# DA QUI LO SCRIPT ORIGINALE FACEVA IL CONFRONTO CON LA VERSIONE CON ACCELERAZIONE GPU

# llm2 = Llama(model_path="./models/7B/ggml-model-q4_0.gguf", n_gpu_layers=16)

# for prompt in prompts:
#     start = perf_counter()
#     output = llm(prompt, max_tokens=-1)
#     time = perf_counter() - start
#     # if(DEBUG_MODE):
#     #     print(output.get('choices')[0].get('text'))
#     timings_GPU.append(time)
#     responses_GPU.append(output.get('choices')[0].get('text'))

# print("\nDi seguito verranno riportati i tempi di esecurzione dei prompt richiesti:\n")
# for i in range(0, len(prompts)):
#     print(f"Tempi di esecuzione prompt {i}:\tCPU={timings_CPU[i]}\tGPU={timings_GPU[i]}")
    
# f = open("python_scrips/results.txt", 'w')
# f.write("Di seguito verranno riportati i tempi di esecurzione dei prompt richiesti:\n")
# for i in range(0, len(prompts)):
#     f.write(f"""
# Prompt: {prompts[i]}
# || CPU - only ||
# Risposta: {responses_CPU[i]}
# Tempo: {timings_CPU[i]}
# || GPU accelerated ||
# Risposta: {responses_GPU[i]}
# Tempo: {timings_GPU[i]}
#             """)
# f.close()