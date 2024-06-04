from langchain_community.llms import Ollama

# Load the model with the phi3 configuration
llm = Ollama(model='phi3')

# Define a sentence to complete
sentence =  ["The capital of Thailand is "]

# Complete the sentence using the generate function
response = llm.generate(sentence)
print(response)
