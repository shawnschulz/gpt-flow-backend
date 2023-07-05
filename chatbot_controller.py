#from transformers import pipeline
from optparse import OptionParser
#from transformers import AutoModelForCausalLM, AutoTokenizer
import os
import json
import sys
from llama_cpp import Llama

#work laptop model path /Users/shawnschulz/Programming/llama.cpp/models/7B/ggml-model-q4_0.bin
#pc server model path "/home/shawn/Programming/ai_stuff/llama.cpp/models/30B/ggml-model-q4_0.bin" 


def ask_lora(prompt):
    path_to_model= "/Users/shawnschulz/Programming/llama.cpp/models/7B/ggml-model-q4_0.bin" 
    llm = Llama(model_path=path_to_model)
    output = llm("Instruction: " + prompt + "Output: ", stop=['Instruction'], max_tokens=200, echo=True)
    print("DEBUG: the output of ask-lora before subsetting is:")
    print(output)
    response = output["choices"][0]["text"].split("Output: ",1)[1]
    #save the model again (this could either be extremely important or useless idk lol)
    #f2 = open(memory_dir + 'dataset.json', 'r+b')
    #f2.write(bytes(str(output), 'utf-8'))
    print(response)
    return(response)