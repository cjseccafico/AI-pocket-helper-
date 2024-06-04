import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.indices.prompt_helper import PromptHelper
from llama_index.core.node_parser import SentenceSplitter


def setup_environment():
    # Set environment variables
    os.environ['llm'] = 'tinyllama'


def initialize_settings():
    # Initialize and configure the LLM and embedding model
    llm_model = os.getenv('llm')
    llm = Ollama(model=llm_model)
    embed_model = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

    # Initialize prompt helper and sentence splitter
    prompt_helper = PromptHelper(context_window=2048)
    node_parser = SentenceSplitter(chunk_size=300, chunk_overlap=20)

    # Configure global settings for application
    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.prompt_helper = prompt_helper
    Settings.node_parser = node_parser


def load_and_index_data(file_path):
    # Load data from the specified file path
    document = SimpleDirectoryReader(input_files=[file_path]).load_data()

    # Process data (chunking, embedding, indexing) and store them in a vector store index
    return VectorStoreIndex.from_documents(document)


def query_data(query_engine, query):
    # Query the indexed data and return the response
    return query_engine.query(query)


if __name__ == "__main__":
    setup_environment()
    initialize_settings()

    # Assuming the file is stored at a specified path
    file_path = 'data.txt'
    index = load_and_index_data(file_path)

    # Build a query engine from the index
    query_engine = index.as_query_engine()

    # Example query
    response = query_data(query_engine, 'show me my calander dates.')
    print(response)
