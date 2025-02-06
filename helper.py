def extract_response(data):
    # Join the content from the list of dictionaries
    full_content = ''.join(item['content'] for item in data)
    
    # Find the position of the <think> tag and return everything after it
    return full_content
    # think_start = full_content.find('<think>')
    # if think_start != -1:
    #     return full_content[think_start:]
    # return None  # If <think> is not found, return None

def no_response():
    return "I'm sorry, Unable to connect to the model."