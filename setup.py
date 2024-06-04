from langchain_community.llms import Ollama
from langchain_community.embeddings import HuggingFaceEmbeddings
from llama_index.core import Settings

# Create an Ollama instance with the model configuration
llm = Ollama(model='tinyllama')

# Use the llm instance directly where needed
Settings.llm = llm

# Configure the embedding model for your settings
Settings.embed_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)
