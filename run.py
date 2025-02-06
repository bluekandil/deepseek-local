
# Use a pipeline as a high-level helper
from transformers import pipeline
import torch
import time

from helper import extract_response, no_response


try: 
    start_time = time.time()
    messages = [
        {"role": "user", "content": "Who are you."},
    ]
   
    pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", device=0) 
    # device = 0: This refers to the first GPU in your system
    
    print(pipe.device)


    response = pipe(messages)       
    
    # res = extract_response(response)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(response)

except Exception as e:        
    res = no_response()
    print(res)